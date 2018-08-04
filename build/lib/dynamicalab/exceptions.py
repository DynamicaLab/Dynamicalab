

__all__ = [
    'DynamicaLabNotImplemented',
]


class DynamicaLabException(Exception):
    """Base class for exceptions in NetworkX."""


class DynamicaLabNotImplemented(DynamicaLabException):
    """Exception raised by algorithms not implemented."""
