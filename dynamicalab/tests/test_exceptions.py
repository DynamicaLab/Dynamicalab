from nose.tools import raises
import dynamicalab as dl

@raises(dl.DynamicaLabNotImplemented)
def test_raise_not_implemented():
	raise dl.DynamicaLabNotImplemented