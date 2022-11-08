class BaseError(Exception):
    message = 'Что-то пошло не так'


class NoteEnoughSpaceError(BaseError):
    message = 'Мало места'


class NoteEnoughItemsError(BaseError):
    message = 'Не достаточно товара'


class TooManyDifferentItems(BaseError):
    message = 'Слишком много разных товаров'


class BadRequestError(BaseError):
    message = 'Неправильно составлен запрос'


class UnknownStorageError(BaseError):
    message = 'Не верно указан склад'
