from typing import Dict, List

from entity.abstract_storage import AbstractStorage
from exeptions import BadRequestError, UnknownStorageError


class Request:
    def __init__(self, request: str, storages: Dict[str, AbstractStorage]):
        split_request: List[str] = request.strip().lower().split(' ')
        if len(split_request) != 7:
            raise BadRequestError

        self.quantity = int(split_request[1])
        self.items = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]

        if self.departure not in storages or self.destination not in storages:
            raise UnknownStorageError
