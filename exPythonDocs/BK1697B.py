import sys
sys.path.append("C:\\MOKO SE\\PythonLibrary")

import MOKO

# EN: Here are the INIT commands for the FY6900 driver
# RU: Тут собраны INIT команды для драйвера FY6900
# 1) EN: Command initialization BK1697B driver
#    RU: Команда инициализации драйвера BK1697B
MOKO.Driver('BK1697B', 'init', '')

# EN: Here are the SET commands for the FY6900 driver
# RU: Тут собраны SET команды для драйвера FY6900
# 1) EN: This command sets the VDC value in the BK1697B driver
#    RU: Данная команда выставляет значение VDC в драйвере BK1697B
MOKO.Driver('BK1697B', 'set', f'VDC = {"Value(Значение)"}')
MOKO.Driver('BK1697B', 'set', f'VDC {"Value(Значение)"}')
MOKO.Driver('BK1697B', 'set', 'VDC = 250k')
MOKO.Driver('BK1697B', 'set', 'VDC = 100')
MOKO.Driver('BK1697B', 'set', 'VDC 30m')
MOKO.Driver('BK1697B', 'set', 'VDC 120')

# 2) EN: This command sets the IDC value in the BK1697B driver
#    RU: Данная команда выставляет значение IDC в драйвере BK1697B
MOKO.Driver('BK1697B', 'set', f'IDC = {"Value(Значение)"}')
MOKO.Driver('BK1697B', 'set', f'IDC {"Value(Значение)"}')
MOKO.Driver('BK1697B', 'set', 'IDC = 130')
MOKO.Driver('BK1697B', 'set', 'IDC = 1k')
MOKO.Driver('BK1697B', 'set', 'IDC 3')
MOKO.Driver('BK1697B', 'set', 'IDC 60m')

# 3) EN: This command sets the output values of the driver in ON or OFF mode
#    RU: Данная команда выставляет значения выхода драйвера в режиме ON или OFF
MOKO.Driver('BK1697B', 'set', 'OUTPUT = ON')
MOKO.Driver('BK1697B', 'set', 'OUTPUT ON')
MOKO.Driver('BK1697B', 'set', 'OUTPUT = OFF')
MOKO.Driver('BK1697B', 'set', 'OUTPUT OFF')

