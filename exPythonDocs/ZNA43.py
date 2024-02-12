import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# EN: Here are the INIT commands for the "ZNA43" driver
# RU: Тут собраны INIT команды для драйвера "ZNA43"
# 1) EN: Command initialization "ZNA43" driver
#    RU: Команда инициализации драйвера "ZNA43"
MOKO.Driver('ZNA43', 'init', '')

# EN: Here are the SET commands for the "ZNA43" driver
# RU: Тут собраны SET команды для драйвера "ZNA43"
# 1) EN: This command sets the wave type in the "ZNA43" driver
#    RU: Данная команда выставляет тип волны в драйвере "ZNA43"
MOKO.Driver('ZNA43', 'set', f'SCPI = {"SCPI command"}')
MOKO.Driver('ZNA43', 'set', 'RESET')
MOKO.Driver('ZNA43', 'set', 'RST')
MOKO.Driver('ZNA43', 'set', 'TimeOut')
MOKO.Driver('ZNA43', 'set', f'Preset = {"Preset_Name"}')



# 3) EN: This command gets value from "ZNA43" driver
#    RU: Данная считывает значения из драйвера "ZNA43"
value = MOKO.Driver('ZNA43', 'get', f'SCPI = {"SCPI command"}')
value = MOKO.Driver('ZNA43', 'get', 'timeout')
