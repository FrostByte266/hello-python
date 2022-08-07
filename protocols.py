"""
This module demonstrates the use of duck typing protocols
"""

import time
from typing import Protocol

class Switchable(Protocol):
    def turn_on(self):
        """Turns this item on

        Should perform the action of turning on
        """
        ...

    def turn_off(self):
        """Turns this item off

        Should perform the action of turning off
        """
        ...

class LightSwitch:
    """
    A simple light switch
    """
    def turn_on(self):
        print('Flicking switch on')

    def turn_off(self):
        print('Flicking switch off')

class FootSwitch:
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


