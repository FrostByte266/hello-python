"""
This module demonstrates the creation of a metaclass
"""

class CapsMeta(type):
    """
    This metaclass will convert all attribute names to UPPER CASE

    Parameters
    ==========
        name : str
            The name of the class
        bases : Tuple[str]
            The base classes (if any)
        attrs : Dict[str, Any]
            Dictionary mapping attribute name to value

    """
    def __new__(cls, name, bases, attrs):
        capital_attrs = {}

        for k, v in attrs.items():
            capital_attrs[k.upper()] = v

        return super().__new__(cls, name, bases, capital_attrs)

