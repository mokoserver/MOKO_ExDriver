import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# EN: Here are the INIT commands for the "example SCPI" driver
# RU: Тут собраны INIT команды для драйвера "example SCPI"
# 1) EN: Command initialization "example SCPI" driver
#    RU: Команда инициализации драйвера "example SCPI"
MOKO.Driver('SCPI', 'init', '')

# EN: Here are the SET commands for the "example SCPI" driver
# RU: Тут собраны SET команды для драйвера "example SCPI"
# 1) EN: This command sets the wave type in the "example SCPI" driver
#    RU: Данная команда выставляет тип волны в драйвере "example SCPI"
MOKO.Driver('SCPI', 'set', f'SCPI = {"SCPI command"}')
MOKO.Driver('SCPI', 'set', 'RESET')
MOKO.Driver('SCPI', 'set', 'RST')
MOKO.Driver('SCPI', 'set', 'TimeOut')
MOKO.Driver('SCPI', 'set', f'Preset = {"Preset_Name"}')



# 3) EN: This command gets value from "example SCPI" driver
#    RU: Данная считывает значения из драйвера "example SCPI"
value = MOKO.Driver('SCPI', 'get', f'SCPI = {"SCPI command"}')
value = MOKO.Driver('SCPI', 'get', 'timeout')
