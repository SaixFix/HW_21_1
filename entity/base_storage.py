from abc import ABC, abstractmethod
from typing import Dict

from entity.abstract_storage import AbstractStorage
from exeptions import NoteEnoughSpaceError, NoteEnoughItemsError, UnknownItemError


class BaseStorage(AbstractStorage):
    def __init__(self, items: Dict[str, int], capacity: int):
        self.__items = items
        self.__capacity = capacity

    def add(self, name: str, qnt: int) -> None:
        if self.get_free_space() < qnt:
            raise NoteEnoughSpaceError

        if name in self.__items:
            self.__items[name] += qnt
        else:
            self.__items[name] = qnt

    def remove(self, name: str, qnt: int) -> None:
        if name not in self.__items:
            raise UnknownItemError
        if qnt > self.__items[name]:
            raise NoteEnoughItemsError


        self.__items[name] -= qnt
        if self.__items[name] == 0:
            self.__items.pop(name)


    def get_free_space(self) -> int:
        return self.__capacity - sum(self.__items.values())

    def get_items(self) -> dict:
        return self.__items

    def get_unique_items_count(self) -> int:
        return len(self.__items)
