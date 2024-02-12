import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# Команды для set:
#   1. Команда Value. Устанавливает значение переменной Value.
MOKO.Driver("ExDriver", "set", "Value = 5")
#   2. Команда ValueMin. Сравнивает минимальное значение со значением Value. Если Value меньше минимального, то выдается ошибка.
MOKO.Driver("ExDriver", "set", "ValueMin = 4")
#   3. Команда ValueMax. Сравнивает максимальное значение со значением Value. Если Value больше максимального, то выдается ошибка.
MOKO.Driver("ExDriver", "set", "ValueMax = 6")

# Команды для get:
#   1. Команда Value. Получить значение переменной Value.
value = MOKO.Driver("ExDriver", "get", "Value", "string")
#   2. Команда Random. Получить случайное число из диапазона [0,10].
random_value = MOKO.Driver("ExDriver", "get", "Random", "string")
#
