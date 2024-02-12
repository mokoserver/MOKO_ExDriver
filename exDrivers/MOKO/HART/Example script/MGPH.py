import MOKO

def WriteGraphCommand():
    #Отобразить данные на графике
    MOKO.Plugin('Graph', 'set', "Write Graph")

def AddLineCommand(name: object, ArrOy: object, ArrOx: object, LineWidth: object, Color: object, Visible: object) -> object:
    #Добавление линии
    MOKO.Plugin('Graph', 'set', f"Add Line={name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")
    MOKO.Plugin('Graph', 'set', "Write Graph")

def ChangeLineCommand(numLine, name, ArrOy, ArrOx,LineWidth,Color,Visible):
    #Изменить параметры уже добавленной линии
    MOKO.Plugin('Graph', 'set', f"Change Line={numLine};{name};{ArrOy};{ArrOx};{LineWidth};{Color};{Visible}")

def DeleteLineCommand(numLine):
    #Команда "All" - удаление всех линий
    #Можно указывать как одну линию, так и массив с номерами линий для удаления
    MOKO.Plugin('Graph', 'set', f"Delete Line={numLine}")

def HideLineCommand(numLine):
    #Команда: "All" - скрыть все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами линий для скрытия
    MOKO.Plugin('Graph', 'set', f"Hide Line={numLine}")

def ShowLineCommand(numLine):
    #Команда: "All" - показать все линии, которые есть на графике, также
    #Можно указывать как одну линию, так и массив с номерами\именами линий для отображения
    #Опция "Only" - показать только те линии, номера которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line={numLine}")

def ShowLineOnlyCommand(numLine):
    #Опция "Only" - показать только те линии, номера или имена которых были переданы,т.е. если на графике отображено
    #много линий, а нужно, чтобы на графике остались только конкретные, то используется эта опция
    MOKO.Plugin('Graph', 'set', f"Show Line=Only;{numLine}")

def AddGraphSettCommand(Value_OyOx, Name_OyOx, Autoscale):
    #Добавление подписей осей + min/max значения осей
    #Установка Autoscale: "Yes", "No", "Only Ox", "Only Oy"
    MOKO.Plugin('Graph', 'set', f"Add Graph Settings={Value_OyOx};{Name_OyOx};{Autoscale}")

def AutoscaleCommand(command):
    #Команды: "No" - отключить Autoscale осей
    #         "Yes" - включить Autoscale осей
    #         "Only Ox" - включить Autoscale только для оси Ox
    #         "Only Oy" - включить Autoscale только для оси Оy
    MOKO.Plugin('Graph', 'set', f"Autoscale={command}")

def ScreenshotWindowCommand():
    #Сделать скриншот фронтальной панели программы и сохранить в папку
    MOKO.Plugin('Graph', 'set', f"Screenshot Window")

def ScreenshotGraphCommand():
    #Graph - сделать скриншот только графика
    MOKO.Plugin('Graph', 'set', f"Screenshot Graph")

def GetScreenshotWindow():
    #Сделать скриншот фронтальной панели программы и сохранить в папку
    screen = MOKO.Plugin('Graph', 'get', f"ScreenshotWindow", 'string')
    return screen

def GetScreenshotGraph():
    #Graph - сделать скриншот только графика
    screen = MOKO.Plugin('Graph', 'get', f"ScreenshotGraph", 'string')
    return screen

def LegendCommand():
    #Показать легенду или скрыть
    MOKO.Plugin('Graph', 'set', "Legend")

def ClearGraphCommand():
    #Очистить график
    MOKO.Plugin('Graph', 'set', "Clear Graph")