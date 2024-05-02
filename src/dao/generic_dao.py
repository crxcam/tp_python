
from abc import ABC,abstractmethod
from typing import Generic, Iterable, Optional, TypeVar


T = TypeVar('T')


class GenericDao(Generic[T],ABC):
    @abstractmethod

    def save(self,t:T)->T:
        pass
    
    def delete(self,t:T)->T:
        pass

    def update(self,t:T)->T:
        pass

    def find_all(self,t:T)-> Iterable[T]:
        pass

    def find_by_id(self,id)-> Optional[T]:
        pass