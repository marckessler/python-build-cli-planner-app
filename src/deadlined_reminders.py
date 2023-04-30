
from abc import ABCMeta, abstractmethod
from collections.abc import Iterable
from abc import ABC
from typing import Iterator
from dateutil.parser import parse 
from datetime import datetime

class DeadlinedMetaReminder (Iterable):
    __metaclass__ = ABCMeta
    def __init_ (self):
        super ().__init__ ()
    
    @abstractmethod
    def is_due (self):
        pass

class DeadlinedReminder (ABC, Iterable):

    @abstractmethod 
    def is_due (self):
        pass

    @classmethod
    def __subclasshook__(cls, subclass):
        if cls is not DeadlinedReminder:
            return NotImplemented

        def attr_in_hierarchy(attr):
            return any (attr in SuperClass.__dict__ for SuperClass in subclass.__mro__)

        if not all(attr_in_hierarchy(attr) for attr in ('__iter__', 'is_due')):
            return NotImplemented

        return True


class DateReminder (DeadlinedReminder):
    def __init__ (self, text, date):
        self.date = parse (date, dayfirst=True)
        self.text = text

    def is_due (self):
        return self.date < datetime.now ()
    
    def __iter__(self) -> Iterator:
        return iter([self.text, self.date.isoformat()])