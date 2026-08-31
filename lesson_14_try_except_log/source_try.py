from source_log import logger


def div(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logger.error(f"Помилка ділення на нуль: {e}")
        result = None
    except TypeError as e:
        logger.error(f"Помилка даних: {e}")
        try:
            if not isinstance(a, (int, float)):
                a = float(a)
            if not isinstance(b, (int, float)):
                b = float(b)
            return div(a, b)
        except ValueError as float_err:
            logger.error(f"Неможливо перетворити значення на float: {float_err}")
            return None
    return result


a = 1
b = "0.000000"
result = div(a, b)
logger.info(f"Результат div: {result}")


def sum(a, b):
    try:
        return a + b
    except (ValueError, TypeError):
        logger.error("Do not use different type here")
        return None


result = sum(a, b)
logger.info(result)

logger.info("*" * 88)


def divide_numbers(a, b):
    try:
        res = a / b
    except ZeroDivisionError:
        logger.error("Помилка: Ділення на нуль.")
        return None
    else:
        logger.info(f"Результат ділення {a} на {b}: {res}")
        return res
    finally:
        logger.info("Цей блок завжди виконується, незалежно від того, чи виникла помилка чи ні")


a = 1
b = 1
result = divide_numbers(a, b)
logger.info(f"result {result}")


def check_age(age):
    if age < 0:
        raise ValueError("Вік не може бути від'ємним")
    return age


def check_email(mail: str):
    if not isinstance(mail, str):
        raise TypeError("String type only expected")
    if mail.count("@") < 1:
        raise ValueError("@ expected in mailbox")
    return mail


def sum_2(a, b):
    assert isinstance(a, (int, float)) and isinstance(b, (int, float)), "int, float is expected"
    return a + b


logger.info(check_email("some@gmail.com"))
logger.info(check_email("s@g.c"))
logger.info(check_email("@"))


class TooLargeValueError(Exception):

    def __init__(self, value, limit):
        self.value = value
        self.limit = limit
        message = f"Значення {value} перевищує ліміт {limit}"
        super().__init__(message)


file = None
try:
    file = open("example.log", "r")
    content = file.read()
except Exception as e:
    logger.error(f"Виникла помилка при читанні файлу: {e}")
finally:
    if file is not None:
        file.close()


# =========================================================
# ДОМАШНЄ ЗАВДАННЯ №14: sum_numbers_in_list
# =========================================================
def sum_numbers_in_list(string_list: list):
    """Повертає список сум чисел зі списку строк,
    які складаються з чисел, розділених комою."""
    
    if not isinstance(string_list, list):
        raise ValueError("Аргумент має бути списком!")

    if not string_list:
        raise ValueError("Список не може бути порожнім!")

    result_list = []
    for item in string_list:
        try:
            # Парсимо числа
            numbers = [int(num.strip()) for num in item.split(",")]
            
            # Обчислюємо суму вручну через цикл або builtins.sum, щоб уникнути конфлікту з def sum(a, b)
            total = 0
            for n in numbers:
                total += n
                
            result_list.append(total)
        except AttributeError:
            result_list.append("Не можу це зробити! AttributeError")
        except ValueError:
            result_list.append("Не можу це зробити!")

    return result_list


if __name__ == "__main__":
    print("\n--- Перевірка Домашки 14 ---")
    print(sum_numbers_in_list(["1,2,3", "4,0,6"]))  # [6, 10]
    print(sum_numbers_in_list(["1,2,3", "asas7,8,9", "4,0,6"]))  # [6, 'Не можу це зробити!', 10]
    print(sum_numbers_in_list(["1,2,3,4", 7]))  # [10, 'Не можу це зробити! AttributeError']
