from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.request import Request


class Delivery:
    def __init__(self, request: Request, storages: Dict[str, AbstractStorage]):
        self.request = request

        self.departure: AbstractStorage = storages[self.request.departure]
        self.destination: AbstractStorage = storages[self.request.destination]

    def move(self):
        self.departure.remove(name=self.request.items, value=self.request.quantity)
        print(f'Курьер забирает {self.request.quantity}шт {self.request.items} из {self.request.departure}')

        self.destination.add(name=self.request.items, value=self.request.quantity)
        print(f'Курьер доставил {self.request.quantity}шт {self.request.items} в {self.request.destination}')


