

class Logger:
    """Логер Синглтон"""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
            cls._instance.log_count = 0
            cls._instance.message = []
        return cls._instance

    def catch(self, func):
        def inner(*args, **kwargs):
            result = func(*args, **kwargs)
            if args:
                self.add(f'Операция: <{func.__name__}>, с данными {args[1:]} и результатом {result}')
            return result
        return inner

    def add(self, message: str):
        """Логирование сообщения"""
        self.log_count += 1
        print(f'{message} | Всего операций {self.log_count}')
