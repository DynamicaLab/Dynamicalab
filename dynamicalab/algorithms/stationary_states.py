from scipy.integrate import odeint
import scipy as sp
import numpy as np

def __well_mixed_2SIS_dynamics__(r, t, infc_rate, coupled_infc_rate, rec_rate, coupled_rec_rate):
    S, I1, I2, I12 = r
    Sdt = rec_rate*I1 + rec_rate*I2 - infc_rate*( S*I1 + S*I2 + 2*S*I12 )
    I1dt = coupled_rec_rate*rec_rate*I12 - rec_rate*I1 + infc_rate*( S*I1 + S*I12 - coupled_infc_rate*I1*I2 - coupled_infc_rate*I1*I12)
    I2dt = coupled_rec_rate*rec_rate*I12 - rec_rate*I2 + infc_rate*( S*I2 + S*I12 - coupled_infc_rate*I1*I2 - coupled_infc_rate*I2*I12)
    I12dt = infc_rate*coupled_infc_rate*( I1*I12 + I2*I12 + 2*I1*I2 ) - 2*coupled_rec_rate*rec_rate*I12
    return np.array([Sdt, I1dt, I2dt, I12dt], float)


def __well_mixed_SIS_dynamics__(r, t, infc_rate, rec_rate):
    S, I = r
    Sdt = rec_rate*I - infc_rate*S*I
    Idt = infc_rate*S*I - rec_rate*I
    return np.array([Sdt, Idt], float)


def __well_mixed_SIR_dynamics__(r, t, infc_rate, rec_rate):
    S, I, R = r
    Sdt = -infc_rate*I*S
    Idt = infc_rate*I*S - rec_rate*I
    Rdt = rec_rate*I
    return np.array([Sdt, Idt, Rdt])


def __well_mixed_2SIR_dynamics__(r, t, infc_rate, coupled_infc_rate):
    S, A, B, AB, a, b, Ab, aB, ab = r
    Sdt = -infc_rate*(A + Ab + B + aB + 2*AB)*S
    Adt = infc_rate*(A + Ab + AB)*S - A - infc_rate*coupled_infc_rate*(B + AB + aB)*A
    Bdt = infc_rate*(B + aB + AB)*S - B - infc_rate*coupled_infc_rate*(A + AB + Ab)*B
    ABdt = infc_rate*coupled_infc_rate*(B + AB + aB)*A + infc_rate*coupled_infc_rate*(A + AB + Ab)*B - 2*AB
    adt = A - infc_rate*coupled_infc_rate*(B + aB + AB)*a
    bdt = B - infc_rate*coupled_infc_rate*(A + Ab + AB)*b
    Abdt = AB + infc_rate*coupled_infc_rate*(A + Ab + AB)*b - Ab
    aBdt = AB + infc_rate*coupled_infc_rate*(B + aB + AB)*a - aB
    abdt = aB + Ab
    return np.array([Sdt, Adt, Bdt, ABdt, adt, bdt, Abdt, aBdt, abdt], float)


def __quenched_SIS_dynamics__(r, t, infc_rate, adjacency_matrix):
    rdt = -r + infc_rate*(1-r)*(adjacency_matrix @ r)
    return rdt


def __quenched_2SIS_dynamics__(r, t, infc_rate, coupled_infc_rate, adjacency_matrix):
    r = r.reshape(4,int(len(r)/4))
    A = adjacency_matrix
    sdt = r[1] + r[2] - infc_rate*r[0]*((A @ r[1]) + (A @ r[2]) + 2*(A @ r[3]))
    r1dt = -r[1] - coupled_infc_rate*infc_rate*r[1]*((A @ r[2]) + (A @ r[3])) + r[3] + infc_rate*r[0]*((A @ r[1]) + (A @ r[3]))
    r2dt = -r[2] - coupled_infc_rate*infc_rate*r[2]*((A @ r[1]) + (A @ r[3])) + r[3] + infc_rate*r[0]*((A @ r[2]) + (A @ r[3]))
    r12dt = -2*r[3] + coupled_infc_rate*infc_rate*r[1]*((A @ r[2]) + (A @ r[3])) + coupled_infc_rate*infc_rate*r[2]*((A @ r[1]) + (A @ r[3]))
    
    rdt = np.array([sdt,r1dt,r2dt,r12dt], float)
    rdt = rdt.reshape(np.prod(np.shape(rdt)))
    return rdt


def stationary_states_SIS(mean_field_type, init_cond, *args, sensibility=1e-5, tmax=100, tcount=100):
    """This function calculates the stationary states of a SIS dynamics. it integrates the dynamical system with sp.odeint, then returns the last value calculated at a certain threshold given by the sensibility parameter.
    
    **Parameters**
    
    mean_field_type : string
        A string of the mean field type. It can be either 'well_mixed_2SIS', 'well_mixed_SIS', 'quenched_SIS' or 'quenched_2SIS'.

    init_cond : np.array
        An array containing the initial value of each variable.

    sensibility : float : (default=1e-5)
        The stationary state is considered attained when the derivatives are at this value.

    tmax : integer : (default=100)
        Integer that gives the maximum value of the sp.linspace made to integrate the dynamics.

    tcount : integer : (default=100)
        Integer that gives the number of iterations made in every tmax.

    *args : various type
        Any additional arguments to call the dynamics.


    **Returns**

    stat_states : np.array
        Array containing the value of every variable at the stationary state.


    **Dynamics**

    *well_mixed_SIS* : Well mixed mean field of a classical SIS dynamic.
        The extra aguments are: 
            - infc_rate : float that gives the rate of infection.
            - rec_rate : float that gives the recovery rate.
        The variables in the output are : [S, I]

    *well_mixed_2SIS* : Well mixed mean field of a SIS dynamics with two interacting diseases.
        The extra arguments are:
            - infc_rate : float that gives the rate of infection.
            - coupled_infc_rate : float that gives the modification to the infection rate induced by the interaction between the two diseases.
            - rec_rate : float that gives the recovery rate.
            - coupled_rec_rate : float that gives the modification to the recovery rate induced by the interaction between the two diseases.
        The variables in the output are : [S, I1, I2, I12]
            S means that the node is susceptible to both diseases.
            I1,I2 means that the node is infected by disease 1,2.
            I12 means that the node is infected by both diseases.

    *quenched_SIS* : Quenched mean field of a classical SIS dynamic.
        The extra arguments are:
            - infc_rate : float that gives the rate of infection.
            - adjacency_matrix : np.array that gives the adjacency matrix of the system.
        Each variable in the output is the probability to be infected of a single node.

    *quenched_2SIS* : Quenched mean field of a SIS dynamics with two interacting diseases.
        The extra arguments are:
            - infc_rate : float that gives the rate of infection.
            - coupled_infc_rate : float that gives the modification to the infection rate induced by the interaction between the two diseases.
            - adjacency_matrix : np.array that gives the adjacency matrix of the system.
        The output is a 4xN matrix. The rows give the probability of being [S, I1, I2, I12] of a single node.

    .. warning::

      For quenched_2SIS, init_cond must be one-dimensional, so it might need to be reshaped before calling the function. The output must also be reshaped (see example).


    **Example**
    

    .. code:: python

        import dynamicalab.algorithms as algo
        import numpy as np

        # Value of the extra parameters of the dynamics
        infc_rate = 0.5
        coupled_infc_rate = 2
        rec_rate = 1
        coupled_rec_rate = 1
        adjacency_matrix = np.array([[0,1,1,1,1,1],[1,0,1,1,1,1],[1,1,0,1,1,1],[1,1,1,0,1,1],[1,1,1,1,0,1],[1,1,1,1,1,0]], float)

        # Value of the initial conditions
        well_mixed_init_cond = [0.98, 0.01, 0.01, 0]
        quenched_init_cond = np.array([[0,0,1,1,1,1],[1,0,0,0,0,0],[0,1,0,0,0,0],[0,0,0,0,0,0]], float)

        # Initial conditions must be one dimensional
        quenched_init_cond =  quenched_init_cond.reshape(np.prod(np.shape(quenched_init_cond)))

        # Calculating the stationary states
        well_mixed_stat_state = algo.stationary_states_SIS('well_mixed_2', well_mixed_init_cond, 5*infc_rate, coupled_infc_rate, rec_rate, coupled_rec_rate)
        quenched_stat_state = algo.stationary_states_SIS('quenched_2', quenched_init_cond, infc_rate, coupled_infc_rate, adjacency_matrix)

        # Reshaping the output for quenched_2SIS
        quenched_stat_state = quenched_stat_state.reshape(4, int(len(quenched_stat_state)/4))

        # Printing the result
        print('Well-mixed:[S, I1, I2, I12]* =', well_mixed_stat_state)
        print('Quenched:[S_1, S_2, ..., S_6]* =', quenched_stat_state[0]
        print('[I1]* =', quenched_stat_state[1])
        print('[I2]* =', quenched_stat_state[2])
        print('[I12]* =', quenched_stat_state[3])


    """
    assert mean_field_type in {'well_mixed_2', 'well_mixed', 'quenched', 'quenched_2'}, 'This dynamic is not implemented.'

    if mean_field_type == 'well_mixed_2':
        func = __well_mixed_2SIS_dynamics__
    elif mean_field_type == 'well_mixed':
        func = __well_mixed_SIS_dynamics__
    elif mean_field_type == 'quenched':
        func = __quenched_SIS_dynamics__
    elif mean_field_type == 'quenched_2':
        func = __quenched_2SIS_dynamics__
    
    report_times = sp.linspace(0,tmax,tcount)
    condition = False
    while condition==False:
        sol = odeint(func, init_cond, report_times, args=args)
        if np.all(func(sol[tcount-1], 0, *args) < sensibility) and np.all(func(sol[tcount-1], 0, *args) > -sensibility):
            stat_states = sol[tcount-1]
            condition=True
        else:
            init_cond = sol[tcount-1]
    return stat_states


def stationary_states_SIR(mean_field_type, init_cond, *args, sensibility = 1e-5, tmax = 100, tcount=100):
    """This function calculates the stationary states of a SIR dynamics. it integrates the dynamical system with sp.odeint, then returns the last value calculated at a certain threshold given by the sensibility parameter.
          
    **Parameters**
    
    mean_field_type : string
        A string of the mean field type. It can be either 'well_mixed' or 'well_mixed_2'.
    
    init_cond : np.array
        An array containing the initial value of each variable.

    sensibility : float : (default=1e-5)
        The stationary state is considered attained when the derivatives are at this value.

    tmax : integer : (default=100)
        Integer that gives the maximum value of the sp.linspace made to integrate the dynamics.

    tcount : integer : (default=100)
        Integer that gives the number of iterations made in every tmax.

    *args : various type
        Any additional arguments to call the dynamics
    

    **Returns**

    stat_states : np.array
        Array containing the value of every variable at the stationary state.


    **Dynamics**

    *well_mixed_SIR* : Well mixed mean field of a classical SIR dynamic.
        The extra aguments are: 
            - infc_rate : float that gives the rate of infection.
            - rec_rate : float that gives the recovery rate.
        The variables in the output are : [S, I, R]
    

    *well_mixed_2SIR* : Well mixed mean field of a SIR dynamics with two interacting diseases.
        The extra arguments are:
            - infc_rate : float that gives the rate of infection.
            - coupled_infc_rate : float that gives the modification to the infection rate induced by the interaction between the two diseases.
        The variables in the output are : [S, A, B, AB, a, b, Ab, aB, ab].
            S means that the node is susceptible to both diseases.
            A,B means that the node is infected by disease A,B.
            AB means that the node is infected by both diseases.
            a,b means the node recovered from disease A,B and is susceptible to the other disease.
            Ab,aB means the node is infected by disease A,B and is recovered from disease B,A.
            ab means the node has recovered from both diseases.


    **Example**

    .. code:: python

        import dynamicalab.algorithms as algo
        import numpy as np
        np.set_printoptions(suppress=True)  # To remove scientific notation from the arrays

        # Value of the extra parameters of the dynamics
        infc_rate = 2
        coupled_infc_rate = 2

        # Value of the initial conditions
        init_cond = [0.98, 0.01, 0.01, 0, 0, 0, 0, 0, 0]

        # Calculating the stationary states
        well_mixed_stat_state = algo.stationary_states_SIR('well_mixed_2', init_cond, infc_rate, coupled_infc_rate)

        # Printing the result
        print('2SIR:[S, A, B, AB, a, b, Ab, aB, ab]* =', well_mixed_stat_state)

    """
    assert mean_field_type in {'well_mixed', 'well_mixed_2'}, 'This dynamic is not implemented.'
    if mean_field_type == 'well_mixed':
        func = __well_mixed_SIR_dynamics__
    elif mean_field_type == 'well_mixed_2':
        func = __well_mixed_2SIR_dynamics__
    
    report_times = sp.linspace(0,tmax,tcount)
    condition = False
    while condition==False:
        sol = odeint(func, init_cond, report_times, args=args)
        if np.all(func(sol[tcount-1], 0, *args) < sensibility) and np.all(func(sol[tcount-1], 0, *args) > -sensibility):
            stat_states = sol[tcount-1]
            condition=True
        else:
            init_cond = sol[tcount-1]
    return stat_states