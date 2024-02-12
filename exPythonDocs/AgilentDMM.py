import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# EN: Here are the INIT commands for the AgilentDMM driver
# RU: Тут собраны INIT команды для драйвера AgilentDMM
# 1) EN: Command initialization AgilentDMM driver
#    RU: Команда инициализации драйвера AgilentDMM
MOKO.Driver('AgilentDMM', 'init', '')

# EN: Here are the SET commands for the AgilentDMM driver
# RU: Тут собраны SET команды для драйвера AgilentDMM
# 1) EN: This command sets the measurement range in the AgilentDMM driver
#    RU: Данная команда выставляет диапазон измерения в драйвере AgilentDMM
MOKO.Driver('AgilentDMM', 'set', f'range = {"Value(Значение)"}')
MOKO.Driver('AgilentDMM', 'set', f'range {"Value(Значение)"}')
MOKO.Driver("AgilentDMM", "set", "range = 10.0000")
MOKO.Driver("AgilentDMM", "set", "range = 10.0000m")
MOKO.Driver("AgilentDMM", "set", "range 10.0000")
MOKO.Driver("AgilentDMM", "set", "range 10.0000m")

# 2) EN: This command sets the measurement type in the AgilentDMM driver
#    RU: Данная команда выставляет тип измерения в драйвере AgilentDMM
MOKO.Driver('AgilentDMM', 'set', 'func = VDC')
MOKO.Driver('AgilentDMM', 'set', 'func VDC')
MOKO.Driver('AgilentDMM', 'set', 'func = VAC')
MOKO.Driver('AgilentDMM', 'set', 'func VAC')
MOKO.Driver('AgilentDMM', 'set', 'func = R2')
MOKO.Driver('AgilentDMM', 'set', 'func R2')
MOKO.Driver('AgilentDMM', 'set', 'func = R4')
MOKO.Driver('AgilentDMM', 'set', 'func R4')
MOKO.Driver('AgilentDMM', 'set', 'func = IDC')
MOKO.Driver('AgilentDMM', 'set', 'func IDC')
MOKO.Driver('AgilentDMM', 'set', 'func = IAC')
MOKO.Driver('AgilentDMM', 'set', 'func IAC')

# 3) EN: This command sets the resolution value in the AgilentDMM driver
#    RU: Данная команда выставляет значение разрешения измерения в драйвере AgilentDMM
MOKO.Driver('AgilentDMM', 'set', f'NPLC = {"Value(Значение)"}')
MOKO.Driver('AgilentDMM', 'set', f'NPLC {"Value(Значение)"}')
MOKO.Driver('AgilentDMM', 'set', 'NPLC = 100')
MOKO.Driver('AgilentDMM', 'set', 'NPLC 100')
MOKO.Driver('AgilentDMM', 'set', 'NPLC = MAX')
MOKO.Driver('AgilentDMM', 'set', 'NPLC MAX')
MOKO.Driver('AgilentDMM', 'set', 'NPLC = MIN')
MOKO.Driver('AgilentDMM', 'set', 'NPLC MIN')

# 4) EN: This command sets the filter value in the AgilentDMM driver
#    RU: Данная команда выставляет значение фильтра в драйвере AgilentDMM
MOKO.Driver('AgilentDMM', 'set', f'BAND = {"Value(Значение)"}')
MOKO.Driver('AgilentDMM', 'set', f'BAND {"Value(Значение)"}')
MOKO.Driver('AgilentDMM', 'set', 'BAND = MIN')
MOKO.Driver('AgilentDMM', 'set', 'BAND MIN')
MOKO.Driver('AgilentDMM', 'set', 'BAND = 3')
MOKO.Driver('AgilentDMM', 'set', 'BAND 3')
MOKO.Driver('AgilentDMM', 'set', 'BAND = MAX')
MOKO.Driver('AgilentDMM', 'set', 'BAND MAX')

# 5) EN: This command sets the Timeout of the AgilentDMM driver
#    RU: Данная команда выставляет значение Timeout в драйвере AgilentDMM
MOKO.Driver('AgilentDMM', 'set', f'Timeout = {"Value(Значение)"}')
MOKO.Driver('AgilentDMM', 'set', f'Timeout {"Value(Значение)"}')
MOKO.Driver('AgilentDMM', 'set', 'Timeout = 10000')
MOKO.Driver('AgilentDMM', 'set', 'Timeout 10000')

# 6) EN: This command resets the previous AgilentDMM driver settings
#    RU: Данная команда сбрасывает предыдущие настройки драйвера AgilentDMM
MOKO.Driver('AgilentDMM', 'set', 'Reset')

# EN: Here are the GET commands for the AgilentDMM driver
# RU: Тут собраны GET команды для драйвера AgilentDMM
# 1) EN: This command reads the value from the AgilentDMM and returns it as a string
#    RU: Данная команда считывает значение из прибора AgilentDMM и возвращает его в строчном виде
value = MOKO.Driver("AgilentDMM", "get", "read")

