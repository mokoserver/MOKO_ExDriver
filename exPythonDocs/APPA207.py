import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO


# EN: Here are the INIT commands for the APPA207 driver
# RU: Тут собраны INIT команды для драйвера APPA207
# 1) EN: Command initialization APPA207 driver
#    RU: Команда инициализации драйвера APPA207
MOKO.Driver('APPA207', 'init', '')

# EN: Here are the GET commands for the APPA207 driver
# RU: Тут собраны GET команды для драйвера APPA207
# 1) EN: This command reads the value from the APPA207 and returns it as a string
#    RU: Данная команда считывает значение из прибора APPA207 и возвращает его в строчном виде
value = MOKO.Driver('APPA207', 'get', 'read')
