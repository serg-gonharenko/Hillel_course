# Написати декоратор для будь якої функції, що буде зберігати історію викликів функцій у файлі.
# Тобто всі функції що будуть задекоровані цим декоратором з кожним викликом мають записувати у файл
# наступний рядок: {Function name} was called with args {args & kwargs} at {time} and return result {result}

import datetime

def decor_log(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        file = open("log.txt", "a")
        file.write(f"Function {func.__name__} was called with args {args} & kwargs {kwargs} "
                   f"at {datetime.datetime.now()} and return result {res}\n")
        file.close()
        return res
    return wrapper

@decor_log
def add_num(a, b):
    return a+b

print(add_num(2, 3))
