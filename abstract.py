"""
This module demonstrates the use of abstract base classes
"""
from abc import ABC, abstractmethod
import time

class Switchable(ABC):
    """
    Describes a device that can be switched on or off

    This class is abstract and cannot be instantiated directly
    """

    @abstractmethod
    def turn_on(self):
        """Turns this item on

        Should perform the action of turning on
        """
        pass

    @abstractmethod
    def turn_off(self):
        """Turns this item off

        Should perform the action of turning off
        """
        pass


class LightSwitch(Switchable):
    """
    A simple light switch
    """
    def turn_on(self):
        print('Flicking switch on')

    def turn_off(self):
        print('Flicking switch off')

class FootSwitch():
    """
    A foot activated switch
    """
    def turn_on(self):
        """
        Happens when the switch is stepped on
        """        
        print('Stepping on switch')

    def turn_off(self):
        """
        Happens when the switch is stepped off
        """        
        print('Stepping off switch')

def flicker(device: Switchable):
    """Flickers a switch

    Turns a switch on, then off after 5 seconds

    Parameters
    ----------
    device : Switchable
        The device to flicker

    Raises
    ------
    TypeError
        Raised if the device is not switchable
    """    
    if not isinstance(device, Switchable):
        raise TypeError('Device must be Switchable')

    device.turn_on()
    time.sleep(5)
    device.turn_off()
