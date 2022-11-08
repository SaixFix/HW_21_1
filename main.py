from typing import Dict

from entity.abstract_storage import AbstractStorage
from entity.delivery import Delivery
from entity.request import Request
from entity.shop import Shop
from entity.store import Store
from exeptions import BaseError

store = Store(
    items={
        'конфета': 10,
        'шкрундель': 10,
    },
    capacity=100
)
shop = Shop(
    items={
        'конфета': 5,
    },
    capacity=20,
    max_unique_items=5
)

storages: Dict[str, AbstractStorage] = {
    'склад': store,
    'магазин': shop,
}


def main():
    while True:
        for storage_name, storage in storages.items():
            print(f'В {storage_name} хранится:\n{storage.get_items()}')

        raw_request: str = input(
            f"Введите запрос в формате 'Доставить 3 печеньки из склад в магазин',"
            f"Введите 'стоп' чтобы закончить"
        )

        if 'стоп' in raw_request:
            break

        try:
            request = Request(request=raw_request, storages=storages)
        except BaseError as error:
            print(error.message)
            continue

        courier = Delivery(request=request, storages=storages)

        try:
            courier.move()
        except BaseError as error:
            print(error.message)
            courier.cansel(error)




if __name__ == '__main__':
    main()
