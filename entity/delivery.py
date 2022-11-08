from typing import Dict


from entity.abstract_storage import AbstractStorage
from entity.request import Request
from exeptions import UnknownItemError, NoteEnoughSpaceError


class Delivery:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.request = request

        self.departure: AbstractStorage = storages[self.request.departure]
        self.destination: AbstractStorage = storages[self.request.destination]

    def move(self):
        self.departure.remove(self.request.items, self.request.quantity)
        print(f'Курьер забирает {self.request.quantity}шт {self.request.items} из {self.request.departure}')

        self.destination.add(self.request.items, self.request.quantity)
        print(f'Курьер доставил {self.request.quantity}шт {self.request.items} в {self.request.destination}')

    def cansel(self, error):
        if error.message == 'Мало места':
            self.departure.add(self.request.items, self.request.quantity)
            print(f'{self.request.quantity}шт {self.request.items} вернулся на склад')








