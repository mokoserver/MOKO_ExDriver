import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# EN: Here are the INIT commands for the FY6900 driver
# RU: Тут собраны INIT команды для драйвера FY6900
# 1) EN: Command initialization FY6900 driver
#    RU: Команда инициализации драйвера FY6900
MOKO.Driver('FY6900', 'init', '')

# EN: Here are the SET commands for the FY6900 driver
# RU: Тут собраны SET команды для драйвера FY6900
# 1) EN: This command sets the wave type in the FY6900 driver
#    RU: Данная команда выставляет тип волны в драйвере FY6900
MOKO.Driver('FY6900', 'set', f'WAVE = {"Type(тип)"}')
MOKO.Driver('FY6900', 'set', f'WAVE {"Type(тип)"}')
MOKO.Driver('FY6900', 'set', 'WAVE = sin')
MOKO.Driver('FY6900', 'set', 'WAVE = ramp')
MOKO.Driver('FY6900', 'set', 'WAVE rectangle')
MOKO.Driver('FY6900', 'set', 'WAVE CMOS')

# 2) EN: This command sets the amplitude value in the FY6900 driver
#    RU: Данная команда выставляет значение амплитуды в драйвере FY6900
MOKO.Driver('FY6900', 'set', f'amplitude = {"Value(Значение)"}')
MOKO.Driver('FY6900', 'set', f'amplitude {"Value(Значение)"}')
MOKO.Driver('FY6900', 'set', 'amplitude = 50k')
MOKO.Driver('FY6900', 'set', 'amplitude = 100')
MOKO.Driver('FY6900', 'set', 'amplitude 250')
MOKO.Driver('FY6900', 'set', 'amplitude 160m')

# 3) EN: This command sets the frequency value in the FY6900 driver
#    RU: Данная команда выставляет значение частоты в драйвере FY6900
MOKO.Driver('FY6900', 'set', f'frequency = {"Value(Значение)"}')
MOKO.Driver('FY6900', 'set', f'frequency {"Value(Значение)"}')
MOKO.Driver('FY6900', 'set', 'frequency = 50k')
MOKO.Driver('FY6900', 'set', 'frequency = 100')
MOKO.Driver('FY6900', 'set', 'frequency 250')
MOKO.Driver('FY6900', 'set', 'frequency 160m')