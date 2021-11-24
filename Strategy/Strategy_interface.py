""" implements an interface for the peyment strategy"""

from abc import ABCMeta, abstractmethod

class IStrategy(object):
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def calculate(self, Employee):
        """ Calculate Employee Type"""