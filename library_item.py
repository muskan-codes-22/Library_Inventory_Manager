from abc import ABC, abstractmethod

class LibraryItem(ABC):

    @abstractmethod
    def to_dict(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
