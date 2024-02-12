import MOKO
import MGPH
import time

Driver = 'HART'

MOKO.Report(f'{Driver}', 'info', 'table', '№#50;T#70')    ### Doesn't work!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def Filling_the_Table(ArrOy):
    t_value = ''
    for i in range(len(ArrOy)):
        t_value = t_value + f'{i + 1};{ArrOy[i]};\\r'

    MOKO.Report(f'{Driver}', 'set', 'table', t_value)

MOKO.Driver(f'{Driver}', 'init', '')

ArrOy = []
ArrOx = []
for i in range(10):
    value = MOKO.Driver(f'{Driver}', 'get', 'value')
    ArrOy[i] = MOKO.Driver(f'{Driver}', 'get', 'Temperature')
    ArrOx[i] = i
    time.sleep(0.2)

MOKO.Driver(f'{Driver}', 'close', '')


MOKO.Plugin('Graph', 'init', '')

time.sleep(4)

MGPH.ClearGraphCommand()

Value_OyOx = [min(ArrOy)-0.1,max(ArrOy)+0.1,min(ArrOx),max(ArrOx)]
Name_OyOx = ["Temperature", "Time"]
Autoscale = "No"
MGPH.AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale)

name = "Temperature"
LineWidth = 2
Color = "FF00FF" #Magenta
Visible = "Yes"
MGPH.AddLineCommand(name, ArrOy, ArrOx,LineWidth,Color,Visible)

Filling_the_Table(ArrOy)

MOKO.EndScript()