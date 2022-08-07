"""
This module demonstrates the use of classes and inheritance
"""
import json

class MyClass:
    """
    A demo class showcasing methods, static methods, class methods, and properties

    Attributes
    ----------
    x : int
        A whole number
    y : int
        Another whole number
    """
    def __init__(self, x: int, y: int) -> None:
        """Called when a new instance of this class is created

        Sets up all attributes and saves them to the instance

        Parameters
        ----------
        x : int
            A whole number
        y : int
            Another whole number
        """        
        self.x = x
        self.y = y

        # Prepending two underscores to a variable makes it so it can only be seen by
        # functions inside the class
        self.__secret = 'Hehehe'

    @property
    def secret(self):
        """A property descriptor that disallows reading a secret from outside the class

        Raises
        ------
        ValueError
            Informs the user they are not permitted to see the secret value
        """        
        raise ValueError('cannot read secret')

    @secret.setter
    def secret(self, new: str):
        """Allows the secret to be changed externally

        Parameters
        ----------
        new : str
            The new secret value
        """        
        self.__secret = new
    
    @classmethod
    def from_json(cls, json_path: str):
        """Creates MyClass using values defined inside a json file

        Parameters
        ----------
        json_path : str
            The file path to your json
        """
        with open(json_path) as f:
            data = json.load(f)

        return cls(**data) # cls is the __init__ method

    @staticmethod
    def add(a: int, b: int) -> int:
        """Adds two numbers

        This function is static, it does not receive self as a parameter

        Parameters
        ----------
        a : int
            Number 1
        b : int
            Number 2

        Returns
        -------
        int
            A added with B
        """
        return a + b
        
    def __int__(self):
        """
        Called when the instance is converted to an integer

        Returns
        =======
        int
            The sum of the `x` and `y` attributes

        Examples
        ========
        .. code-block:: python

            >> my_object = MyClass(5, 1)
            >> print(int(my_object)) #=> 6
        

        """
        return self.add(self.x, self.y)

    def __add__(self, other):
        """
        Called when the instance is added to with the + operator

        Examples
        ========
        .. code-block:: python

            >>> my_object = MyClass(5, 1)
            >>> print(x + 2) #=> 8
        """
        return self.add(int(self), other)

    def this_is_work(self, banana: str) -> str:
        """Does some work

        Will used to drive a banana car

        Parameters
        ----------
        banana : str
            A cool banana

        Returns
        -------
        str
            Peels the banana
        """
        return 'Peeled Banana'

class MyOtherClass(MyClass):
    """
    This class has access to all variables and methods defined in :class:`MyClass`

    Attributes
    ----------
    z : int
        An additional whole number used in this class
    """

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def some_unique_method(self):
        """
        This function is only usable in MyOtherClass
        """        
        pass
