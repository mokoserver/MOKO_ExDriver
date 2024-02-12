'''     Данная библиотека функций служит для осуществления HTTP запросов на MOKO SE.

        26.02.2021 Библиотека переименована в MOKO для удобства разработчиков

        Версия библиотеки: 1.5 от 23.06.2021. Изменен формат post-запросов для драйверов.

        Версия документации: 1.2 от 03.02.2020.
        
        Версия измененая 24.01.2022 для корректной работы старта/паузы/стопа
 
        Для работы этой библиотеки требуются библиотеки **requests** и **json**.

'''

import requests
from time import sleep
import json
import sys

requests = requests.Session()

_UrlStageWrite = 'http://localhost:55001/MOKOSE/stage/stagewrite'

_UrlDriverWrite = 'http://localhost:55001/MOKOSE/system/driverwrite'
_UrlDriverRead = 'http://localhost:55001/MOKOSE/system/driverread'

_UrlPluginWrite = 'http://localhost:55001/MOKOSE/system/pluginwrite'
_UrlPluginRead = 'http://localhost:55001/MOKOSE/system/pluginread'

_UrlMessengerWrite = 'http://localhost:55001/MOKOSE/system/messengerwrite'
_UrlMessengerRead = 'http://localhost:55001/MOKOSE/system/messengerread'

_UrlReportWrite = 'http://localhost:55001/MOKOSE/system/reportwrite'
_UrlReportRead = 'http://localhost:55001/MOKOSE/system/reportread'

_UrlProgramWrite = 'http://localhost:55001/MOKOSE/system/programwrite'
_UrlProgramRead = 'http://localhost:55001/MOKOSE/system/programread'

_UrlUtilityWrite = 'http://localhost:55001/MOKOSE/system/utilitywrite'
_UrlUtilityRead = 'http://localhost:55001/MOKOSE/system/utilityread'

_UrlProjectStateRead = 'http://localhost:55001/MOKOSE/status/projectstate'

_UrlPSAPWrite = 'http://localhost:55004/Server/plugin/WRITE/'
_UrlPSAPRead = 'http://localhost:55004/Server/plugin/READ/'

_Messenger_CurrentType = 0

_Driver_CurrentName = 0
_Driver_CurrentType = 0
_Driver_CurrentCommand = 0

_ReadTimeout = -1


###################################################################################################################

    ##          ##          ####        ##########      ##        ##     
    ####      ####         ##  ##           ##          ####      ##
    ## ##    ## ##        ##    ##          ##          ## ##     ##
    ##  ##  ##  ##       ##      ##         ##          ##  ##    ##
    ##   ####   ##      ############        ##          ##   ##   ##
    ##    ##    ##      ##        ##        ##          ##    ##  ##
    ##          ##      ##        ##        ##          ##     ## ##
    ##          ##      ##        ##        ##          ##      ####
    ##          ##      ##        ##    ##########      ##       ###

###################################################################################################################


###################################################################################################################

    ##########      ##################          ####     
    ##                      ##                 ##  ##
    ##                      ##                ##    ##  
    ##                      ##               ##      ## 
    ##########              ##              ############
            ##              ##              ##        ##
            ##              ##              ##        ##
            ##              ##              ##        ##
    ##########              ##              ##        ##          

###################################################################################################################

# Stage - функция, осуществляющая запись строки в Stage (даёшь рекурсию)
# stage_string - Строка, записываемая в Stage
# type - Тип строки в Stage (Info, Error, Plugin, Driver, Report, Warning). По умолчанию Info.
def Stage(stage_string, type='info'):
    """ 
    Функция осуществляет запись строки в Stage.

    :param str stage_string: Строка, записываемая в Stage.
    :param str type: Тип строки в Stage (**Info**, **Error**, **Plugin**, **Driver**, **Report**, **Warning**). По умолчанию **Info**.
    :return: Функция возвращает код статуса HTTP запроса
    :rtype: *int*

    **Пример:**

    **1.**
    Нам нужно записать строку **'Hello, World!'** в Stage. Для этого напишем следующую команду:

    >>> Stage('Hello, World!')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"string": "Hello World!", "type":"info"}'``

    В Stage программы MOKO SE должна появиться информационная строка:

    ``Hello World!``

    Функция должна вернуть следующее значение:

    ``200``

    Иначе не выполняется либо возвращает код состояния HTTP запроса. Например:

    ``400``

    А в терминале:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``    
    
    **2.**
    Нам нужно записать строку ошибки **'ERROR! Wrong request type!'** в Stage. 
    
    Если мы указываем тип выводимой строки, то команда будет иметь следующий вид:
    
    >>> Stage('ERROR! Wrong request type!', 'ERROR')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"string": "ERROR IN PYTHON LIBRARY! Wrong request type!", "type":"ERROR"}'``

    В Stage программы MOKO SE должна появиться строка ошибки:

    ``ERROR! Wrong request type!``

    А также функция должна вернуть следующее значение:

    ``200``

    Иначе не выполняется либо возвращает код состояния HTTP запроса. Например:

    ``404``

    А в терминале:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

'+str(name)+'
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза

    URL = _UrlStageWrite
    text_to_send = '{"string" :"'+str(stage_string)+'", "type":"'+str(type)+'"}'
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    response = requests.post(URL, headers=headers, data=text_to_send.encode('utf-8'))
    print(response.content)

#    response = requests.post(URL, json={"string":stage_string, "type":type})
#    print(response.content)
    return response.status_code

def StageParam(param, value):
    
    return

###################################################################################################################

    #####           #######         ##########
    ##   ##         ##     ##           ##
    ##     ##       ##      ##          ##    
    ##      ##      ##     ##           ##    
    ##      ##      #######             ##
    ##      ##      ####                ##
    ##     ##       ## ##               ##
    ##   ##         ##   ##             ##
    #####           ##     ##       ##########

###################################################################################################################

# Driver - функция, осуществляющая работу с драйвером
# name - имя драйвера
# mode - тип команды ('get', 'set', 'init', 'close')
# command - команда, которую записывает драйвер в управляемый прибор
# valuetype (только для type = 'get') - тип данных, получаемый из драйвера. По умолчанию void
def Driver(name, mode, command, valuetype='void'):
    """ 
    Функция осуществляет работу с драйвером.

    :param str name: Имя драйвера
    :param str mode: Тип команды (**'get'**, **'set'**, **'init'**, **'close'**)
    :param str command: Команда, которую записывает драйвер в управляемый прибор
    :param str valuetype: **(только для mode = 'get')** Тип данных, получаемых из драйвера. По умолчанию *void*.
    :return: Функция возвращает *None* (если mode = **'set'**) либо принятые с драйвера данные (если mode = **'get'**)
    :rtype: Возвращаемый тип данных меняется в зависимости от полученных из драйвера значений

    **Пример:**

    **1.**
    Нам нужно проиницилизировать драйвер прибора SMBV100A. Для этого напишем следующую команду:

    >>> Driver('SMBV100A', 'init', '')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "SMBV100A", "type": "init", "command": ""}'``

    На экране должно появиться окно инициализации драйвера(выбор интерфейса).

    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **2.**
    Нам нужно сбросить прибор SMBV100A. Для этого напишем следующую команду:

    >>> Driver('SMBV100A', 'set', 'reset')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "SMBV100A", "type": "set", "command": "reset"}'``

    Драйвер должен сбросить настройки прибора SMBV100A.

    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **3.**
    Нам нужно прочитать значение тестового окошка тестового драйвера. Для этого напишем следующую команду:

    >>> Driver('Test', 'get', 'test', 'bool')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "Test", "type": "get", "command": "test"}'``

    На экране должно отобразиться окно с надписью 'Test' и двумя кнопками 'OK' и 'Cancel'. 

    В зависимости от нажатой кнопки драйвер и функция должны вернуть:

    ``True('OK') либо False('Cancel').``

    В случае какой-либо ошибки функция не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:
    
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``
    
    А если не ввести `valuetype`, то функция не отработает, о чём оповестит в терминале и Stage программы MOKO SE.
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    ProjectState()
    if ((mode.lower() == 'get') and (valuetype.lower() == 'void')):
        Stage("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request", 'error')
        print("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request")
        return None
    if ((mode.lower() != 'get') and (mode.lower() != 'set') and (mode.lower() != 'init') and (mode.lower() != 'close')):
        Stage("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode))
        return None
    URLWrite = _UrlDriverWrite
    URLRead = _UrlDriverRead

    command_to_send = '{"name":"' + str(name) + '","type":"' + str(mode) + '","command":"' + str(command) + '"}'
    headers = {'Content-Type': 'application/json; charset=utf-8'}
    #json = {"name": name, "type": mode, "command": command}
    response = requests.post(URLWrite, headers=headers, data=command_to_send.encode('utf-8'))
    print(response.content)
    
    timeout = 0
    badresponse_timeout = 0
    drvstatus = 'none'
    while ((drvstatus.lower() != 'ready') and (badresponse_timeout < 10)):
        response = requests.get(URLRead)
        # Проверка состояния проекта: Старт/Стоп/Пауза
        ProjectState()
        if (response.status_code != 200):
            Stage("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code), 'error')
            print("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code) + '\n' + str(10 - badresponse_timeout) + ' tries left')
            badresponse_timeout += 1
        else:
            y = json.loads(response.content)
            drvstatus = y.get('driverstatus')
            if (mode.lower() == 'get'):
                drvdata = y.get('driverdata')
            timeout += 1
            #Stage('Wait ' + str(timeout))
        sleep(0.05)

    if (badresponse_timeout >= 10):
        Stage("ERROR IN PYTHON LIBRARY! Function exit because of bad responses", 'error')
        print("ERROR IN PYTHON LIBRARY! Function exit because of bad responses")
        value = None
        return value

    if ((drvstatus.lower() == 'ready') and (mode.lower() == 'get')):
        #Stage(drvdata)
        ind = drvdata.find(';')
        if (ind == -1):
            drvdata = drvdata + ';'
        ind = drvdata.rfind(';')
        if (ind != (len(drvdata)-1)):
            drvdata = drvdata + ';'
        value = ParseValue(drvdata, valuetype)
        return value

    value = None
    return value

###################################################################################################################

    #######         ##                  ##         ##
    ##     ##       ##                  ##         ##
    ##      ##      ##                  ##         ##
    ##     ##       ##                  ##         ##
    #######         ##                  ##         ##
    ##              ##                  ##         ##
    ##              ##                  ##         ##
    ##              ##                  ##         ##
    ##              #############       #############         

###################################################################################################################

# Plugin - функция, осуществляющая работу с плагином
# name - имя плагина
# mode - тип команды ('get', 'set', 'init')
# command - команда, которую отправляем в плагин.
# valuetype (только для type = 'get') - тип данных, получаемый из плагина
def Plugin(name, mode, command, valuetype='void'):

    """ 
    Функция осуществляет работу с плагином.

    :param str name: Имя плагина
    :param str mode: Тип команды (**'get'**, **'set'**, **'init'**)
    :param str command: Команда, которую отправляем в плагин.
    :param str valuetype: (только для mode = **'get'**) Тип данных, получаемых из плагина. По умолчанию *void*.
    :return: Функция возвращает *None* (если mode = **'set'**) либо принятые с плагина данные (если mode = **'get'**)
    :rtype: Возвращаемый тип данных меняется в зависимости от полученных из плагина значений

    **Пример:**

    **1.**
    Нам нужно проинициализировать плагин NMEA0183. Для этого напишем следующую команду:

    >>> Plugin("NMEA0183", "init", "")

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "NMEA0183", "type": "init", "command": ""}'``

    На экране должно появиться окно плагина.

    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **2.**
    Нам нужно сбросить протоколы плагина NMEA0183. Для этого напишем следующую команду:

    >>> Plugin("NMEA0183", "set", "ProtocolReset=True")

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "NMEA0183", "type": "set", "command": "ProtocolReset=True"}'``

    Плагин NMEA0183 должен сбросить протоколы.

    Функция должна вернуть следующее значение:

    ``None``
    
    Иначе не выполняется, либо отображает в программе MOKO SE какую-то ошибку, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **3.**
    Нам нужно прочитать время определения координат из плагина NMEA0183. Для этого напишем следующую команду:

    >>> Plugin('NMEA0183', 'get','CoordinatesValidTime', 'float')

    В случае успешного выполнения в терминале должна появиться следующая строка:
        
    ``b'{"name": "NMEA0183", "type": "get", "command": "CoordinatesValidTime"}'``

    Функция должна вернуть следующее значение некоторое время в секундах:

    ``0 (но для данной команды плагина NMEA0183 это признак ошибки при работе)``

    либо, например: 

    ``17.56``

    В случае какой-либо ошибки функция не выполняется, либо отображает какую-то ошибку, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``
    
    А если не ввести *valuetype*, то функция не отработает, о чём оповестит в терминале и Stage программы MOKO SE.

    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    ProjectState()
    if ((mode.lower() == 'get') and (valuetype.lower() == 'void')):
        Stage("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request", 'error')
        print("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request")
        return None
    if ((mode.lower() != 'get') and (mode.lower() != 'set') and (mode.lower() != 'init')):
        Stage("ERROR IN PYTHON LIBRARY! Wrong request type! " +  str(mode), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong request type! " +  str(mode))
        return None
    URLWrite = _UrlPluginWrite
    URLRead = _UrlPluginRead

    response = requests.post(URLWrite, json={"name":name,"type":mode,"command":command})	
    print(response.content)
       
    timeout = 0
    badresponse_timeout = 0
    plgstatus = 'none'   
    while ((plgstatus.lower() != 'ready') and (badresponse_timeout < 10)):
        response = requests.get(URLRead)
        # Проверка состояния проекта: Старт/Стоп/Пауза
        ProjectState()
        if (response.status_code != 200):
            Stage("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code), 'error')
            print("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code) + '\n' + str(10 - badresponse_timeout) + ' tries left')
            badresponse_timeout += 1
        else:
            y = json.loads(response.content)
            plgstatus = y.get('pluginstatus')
            if (mode.lower() == 'get'):
                plgdata = y.get('plugindata')
            timeout += 1
            #Stage('Wait ' + str(timeout))
        sleep(0.05)

    if (badresponse_timeout >= 10):
        Stage("ERROR IN PYTHON LIBRARY! Function exit because of bad responses", 'error')
        print("ERROR IN PYTHON LIBRARY! Function exit because of bad responses")
        value = None
        return value

    if ((plgstatus.lower() == 'ready') and (mode.lower() == 'get')):
        #Stage(plgdata)
        ind = plgdata.find(';')
        if (ind == -1):
            plgdata = plgdata + ';'
        ind = plgdata.rfind(';')
        if (ind != (len(plgdata)-1)):
            plgdata = plgdata + ';'
        value = ParseValue(plgdata, valuetype)
        return value

    value = None
    return value


###################################################################################################################

#######          ############            ###             #######
##     ##       ##                     ##   ##           ##     ##
##      ##      ##                    ##     ##          ##      ##
##     ##       ##                   ##       ##         ##     ##
#######          ###########        #############        #######
##                         ##       ##         ##        ##
##                         ##       ##         ##        ##
##                         ##       ##         ##        ##
##              ############        ##         ##        ##

###################################################################################################################

# PSAP- полная копия функции Plugin, но предназначенная для работы с Modem
# Plugin - функция, осуществляющая работу с плагином
# name - имя плагина
# mode - тип команды ('get', 'set', 'init')
# command - команда, которую отправляем в плагин.
# valuetype (только для type = 'get') - тип данных, получаемый из плагина
def PSAP(name, mode, command, valuetype='void'):


    if ((mode.lower() == 'get') and (valuetype.lower() == 'void')):
        Stage("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request", 'error')
        print("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request")
        return None
    if ((mode.lower() != 'get') and (mode.lower() != 'set') and (mode.lower() != 'init')):
        Stage("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode))
        return None
    URLWrite = _UrlPSAPWrite
    URLRead = _UrlPSAPRead

    response = requests.post(URLWrite, json={"name": name, "type": mode, "command": command})

    timeout = 0
    badresponse_timeout = 0
    plgstatus = 'none'
    while ((plgstatus.lower() != 'ready') and (badresponse_timeout < 10)):
        response = requests.get(URLRead)
        # Проверка состояния проекта: Старт/Стоп/Пауза
        ProjectState()
        if (response.status_code != 200):
            Stage("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code), 'error')
            print("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code) + '\n' + str(
                10 - badresponse_timeout) + ' tries left')
            badresponse_timeout += 1
        else:
            y = json.loads(response.content)
            print(y)
            plgstatus = y.get('status')
            if (mode.lower() == 'get'):
                plgdata = y.get('data')
            timeout += 1
            # Stage('Wait ' + str(timeout))
        sleep(0.1)

    if (badresponse_timeout >= 10):
        Stage("ERROR IN PYTHON LIBRARY! Function exit because of bad responses", 'error')
        print("ERROR IN PYTHON LIBRARY! Function exit because of bad responses")
        value = None
        return value

    if ((plgstatus.lower() == 'ready') and (mode.lower() == 'get')):
        # Stage(plgdata)
        ind = plgdata.find(';')
        if (ind == -1):
            plgdata = plgdata + ';'
        ind = plgdata.rfind(';')
        if (ind != (len(plgdata) - 1)):
            plgdata = plgdata + ';'
        value = ParseValue(plgdata, valuetype)
        return value

    value = None
    return value

###################################################################################################################

    ##          ##      ############        ##########
    ####      ####      ##                  ##        
    ## ##    ## ##      ##                  ##        
    ##  ##  ##  ##      ##                  ##        
    ##   ####   ##      ########            ##########
    ##    ##    ##      ##                          ##
    ##          ##      ##                          ##
    ##          ##      ##                          ##
    ##          ##      ############        ##########

###################################################################################################################

# Messenger - функция, осуществляющая появление на экране всплывающего сообщения с опциональным полем для ввода данных
# mode - тип команды ('get', 'set')
# head - заголовок сообщения
# body - содержание сообщения
# valuetype (только для type = 'get') - тип данных, получаемый из cообщения
# delaytime (если необходимо) - время задержки в секундах.
def Messenger(mode, head, body, valuetype='void', delaytime='void'):
    """ 
    Функция осуществляет появление на экране всплывающего сообщения с опциональным полем для ввода данных

    :param str mode: Тип команды (**'get'**, **'set'**)
    :param str head: Заголовок сообщения.
    :param str body: Содержание сообщения.
    :param str valuetype: **(только для mode = 'get')** Тип данных, получаемых из сообщения. По умолчанию *void*.
    :param str delaytime: *(если необходимо)* Время задержки в секундах.
    :return: Функция возвращает *None* (если mode = **'set'**) либо введённые в окне сообщения данные (если mode = **'get'**)
    :rtype: Возвращаемый тип данных меняется в зависимости от полученных из сообщения значений

    **Пример:**

    **1.**
    Нам нужно отобразить сообщение для пользователя, которое просит присоединить прибор и запустить плагин NMEA0183. Для этого напишем следующую команду:

    >>> Messenger('set', 'Info', 'Please connect the device and launch NMEA0183 plugin.')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"type": "set", "head": "Info", "body": "Please connect the device and launch NMEA0183 plugin."}'``
    
    На экране должно появиться окно с сообщением, в котором в заголовке будет написано 'Info', а в теле - 'Please connect the device and launch NMEA0183 plugin.'.
    
    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **2.**
    Нам нужно отобразить сообщение для пользователя, чтобы он ввёл некоторое число. Для этого напишем следующую команду:

    >>> Messenger('get', 'First number', 'Please, enter the first number', 'int')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"type": "get", "head": "First number", "body": "Please, enter the first number"}'``

    На экране должно появиться окно с сообщением, в котором в заголовке будет написано 'First number', а в теле - 'Please, enter the first number.'. Также это сообщение будет иметь поле для ввода данных.
    
    Функция должна вернуть введённое число, например:
        
    ``123``

    Иначе не выполняется, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    А если не ввести *valuetype*, то функция не отработает, о чём оповестит в терминале и Stage программы MOKO SE.
    
    **3.**
    Нам нужно отобразить сообщение о задержке выполнения скрипта на 15 минут.

    Если нам необходима задержка в сообщении, то это делается как в следующем примере: 

    >>> MOKO.Messenger('set', 'Info', 'Please, wait for 15 minutes', 'void', str(15*60))

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"type": "set", "head": "Info", "body": "Please, wait for 15 minutes", "time": "900"}'``

    На экране должно появиться окно с сообщением, в котором в заголовке будет написано 'Info', а в теле - 'Please, wait for 15 minutes.'. 
    
    Также должен появиться таймер, отсчитывающий 15 минут.

    В случае какой-либо ошибки функция не выполняется, либо в терминале отобразится, например, следующая строка:
        
    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    ProjectState()
    if ((mode.lower() == 'get') and (valuetype.lower() == 'void')):
        Stage("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request", 'error')
        print("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request")
        return None
    if ((mode.lower() != 'get') and (mode.lower() != 'set')):
        Stage("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode))
        print("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode))
        return None
   # if (valuetype.lower() == 'void') : valuetype =string    
    URLWrite = _UrlMessengerWrite
    URLRead = _UrlMessengerRead    
    
    if (delaytime == 'void'):
        text_to_send = '{"type":"'+str(mode)+'","head":"'+str(head)+'","body":"'+str(body)+'","value":"'+str(valuetype)+'"}'
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(URLWrite, headers=headers, data=text_to_send.encode('utf-8'))
    else:
        text_to_send = '{"type":"'+str(mode)+'","head":"'+str(head)+'","body":"'+str(body)+'","time":"'+str(delaytime)+'"}'
        headers = {'Content-Type': 'application/json; charset=utf-8'}
        response = requests.post(URLWrite, headers=headers, data=text_to_send.encode('utf-8'))
        #response = requests.post(URLWrite, json={"type":mode,"head":head,"body":body,"time":str(delaytime)})
    print(response.content)

    timeout = 0
    badresponse_timeout = 0
    msgstatus = 'none'
    while ((msgstatus.lower() != 'ready') and (badresponse_timeout < 10)):
        response = requests.get(URLRead)
        # Проверка состояния проекта: Старт/Стоп/Пауза
        ProjectState()           
        if (response.status_code != 200):
            Stage("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code), 'error')
            print("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code) + '\n' + str(10 - badresponse_timeout) + ' tries left')
            badresponse_timeout += 1
        else:
            y = json.loads(response.content)
            msgstatus = y.get('messengertatus')
            if (mode.lower() == 'get'):
                msgdata = y.get('messengerdata')
            timeout += 1
            #Stage('Wait ' + str(timeout))
        sleep(0.05)

    if (badresponse_timeout >= 10):
        Stage("ERROR IN PYTHON LIBRARY! Function exit because of bad responses")
        print("ERROR IN PYTHON LIBRARY! Function exit because of bad responses")
        value = None
        return value

    if ((msgstatus.lower() == 'ready') and (mode.lower() == 'get')):
        #Stage(msgdata)
        ind = msgdata.find(';')
        if (ind == -1):
            msgdata = msgdata + ';'
        ind = msgdata.rfind(';')
        if (ind != (len(msgdata)-1)):
            msgdata = msgdata + ';'
        if ((valuetype.lower() != 'boolean') and (valuetype.lower() != 'string')):
            valuetype = 'string'
        value = ParseValue(msgdata, valuetype)
        return value

    value = None
    return value

###################################################################################################################

    ######          ############        #######
    ##    ##        ##                  ##     ##
    ##     ##       ##                  ##      ##
    ##   ##         ##                  ##     ##
    ## ##           ######              ####### 
    ####            ##                  ##
    ## ##           ##                  ##
    ##   ##         ##                  ##
    ##     ##       ############        ##

###################################################################################################################

# Report - функция, осуществляющая работу с данными в отчёте
# name - название для записываемых в отчёт данных и имя закладки в документе-шаблоне Word
# mode - тип команды (пока что только 'set') 
# kind - в каком виде данные записываются в отчёт(string - строка и table - таблица)
# data - записываемые в отчёт данные
# valuetype (только для type = 'get') - тип данных, получаемый из отчёта
def Report(name, mode, kind, data, valuetype='void'):
    """ 
    Функция осуществляет работу с данными в отчёте.

    :param str name: Название для записываемых в отчёт данных и имя закладки в документе-шаблоне Word
    :param str mode: Тип команды (пока что только **'set'**)
    :param str kind: В каком виде данные записываются в отчёт(**string** - строка и **table** - таблица)
    :param str data: Записываемые в отчёт данные
    :param str valuetype: (только для mode = 'get') Тип данных, получаемых из отчёта. По умолчанию *void*.
    :return: Функция возвращает *None* (если mode = **'set'**) либо полученные из отчёта данные (если mode = **'get'**)
    :rtype: Возвращаемый тип данных меняется в зависимости от полученных из отчёта значений

    **Пример:**

    **1.**
    Нам нужно вывести строку *'FgsFds'* в отчёт. Для этого напишем следующую команду:

    >>> Report("rep1",'set', 'string', 'FgsFds')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "rep1", "type": "set", "kind": "string", "data": "FgsFds"}'``

    В программе MOKO SE во вкладке 'Report' в таблице 'Report names' должен появиться элемент 'rep1'. По нажатию на этот элемент в таблице 'Reports' должна появиться строка *FgsFds*.
    
    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``

    **2.**
    Нам нужно вывести 3 строки в таблицу отчёта. Для этого напишем следующую команду:

    >>> Report("rep2",'set', 'table', 'FgsFds, fgsfds, etc')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    ``b'{"name": "rep2", "type": "set", "kind": "table", "data": "FgsFds, fgsfds, etc"}'``
    
    В программе MOKO SE во вкладке 'Report' в таблице 'Report names' должен появиться элемент 'rep2'. По нажатию на этот элемент в таблице 'Reports' три столбца в одной строке должны заполниться значениями соответственно 'FgsFds', 'fgsfds' и 'etc'.
    
    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``
    
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    ProjectState()
    if ((mode.lower() == 'get') and (valuetype.lower() == 'void')):
        Stage("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request", 'error')
        print("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request")
        return None
    if ((mode.lower() != 'get') and (mode.lower() != 'set') and (mode.lower() != 'info') and (mode.lower() != 'clear') and (mode.lower() != 'delete') and (mode.lower() != 'save')):
        Stage("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong request type! " + str(mode))
        return None
    if ((kind.lower() != 'table') and (kind.lower() != 'string') and (kind.lower() != 'picture') and (kind.lower() != 'strings')):
        Stage("ERROR IN PYTHON LIBRARY! Wrong report kind! " + str(kind), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong report kind! " + str(kind))
        return None
    URLWrite = _UrlReportWrite
    URLRead = _UrlReportRead
    
    text_to_send = '{"name":"'+str(name)+'","type":"'+str(mode)+'", "kind":"'+str(kind)+'", "data":"'+str(data)+'"}'

    headers = {'Content-Type': 'application/json; charset=utf-8'}

    response = requests.post(URLWrite, headers=headers, data=text_to_send.encode('utf-8'))
    print(response.content)
    
    timeout = 0
    badresponse_timeout = 0
    repstatus = 'none'
    prjectstate = 'none'
 
    while ((repstatus.lower() != 'ready') and (badresponse_timeout < 10)):
        response = requests.get(URLRead)
        # Проверка состояния проекта: Старт/Стоп/Пауза
        ProjectState()
        if (response.status_code != 200):
            Stage("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code), 'error')
            print("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code) + '\n' + str(10 - badresponse_timeout) + ' tries left')
            badresponse_timeout += 1
        else:
            y = json.loads(response.text)
            repstatus = y.get('reportstatus')
            if (mode.lower() == 'get'):
                repdata = y.get('reportdata')
            timeout += 1
            #Stage('Wait ' + str(timeout))
        sleep(0.05)

    if (badresponse_timeout >= 10):
        Stage("ERROR IN PYTHON LIBRARY! Function exit because of bad responses", 'error')
        print("ERROR IN PYTHON LIBRARY! Function exit because of bad responses")
        value = None
        return value

    if ((repstatus.lower() == 'ready') and (mode.lower() == 'get')):
        #Stage(repdata)
        ind = repdata.find(';')
        if (ind == -1):
            repdata = repdata + ';'
        ind = repdata.rfind(';')
        if (ind != (len(repdata)-1)):
            repdata = repdata + ';'
        value = ParseValue(repdata, valuetype)
        return value

    value = None
    return value

###################################################################################################################

    ##         ##   ##################      
    ##         ##           ##          
    ##         ##           ##          
    ##         ##           ##  
    ##         ##           ##
    ##         ##           ##
    ##         ##           ##
    ##         ##           ##
    #############           ##

###################################################################################################################

# Utility - функция, осуществляющая работу с утилитой
# name - имя утилиты
# mode - тип команды ('get', 'set')
# command - команда, которую отправляем в утилиту.
# valuetype (только для type = 'get') - тип данных, получаемый из утилиты
def Utility(name, mode, command, valuetype='void'):

    """ 
    Функция осуществляет работу с утилитой.

    :param str name: Имя утилиты
    :param str mode: Тип команды (**'get'**, **'set'**)
    :param str command: Команда, которую отправляем в утилиту.
    :param str valuetype: (только для mode = **'get'**) Тип данных, получаемых из утилиты. По умолчанию *void*.
    :return: Функция возвращает *None* (если mode = **'set'**) либо принятые с утилиты данные (если mode = **'get'**)
    :rtype: Возвращаемый тип данных меняется в зависимости от полученных из утилиты значений

    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    ProjectState()
    if ((mode.lower() == 'get') and (valuetype.lower() == 'void')):
        Stage("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request", 'error')
        print("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request")
        return None
    if ((mode.lower() != 'get') and (mode.lower() != 'set') and (mode.lower() != 'init')):
        Stage("ERROR IN PYTHON LIBRARY! Wrong request type! " +  str(mode), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong request type! " +  str(mode))
        return None
    URLWrite = _UrlUtilityWrite
    URLRead = _UrlUtilityRead

    text_to_send = '{"name" :"' + str(name) + '", "type":"' + str(mode) + '", "command":"' + str(command) + '"}'
    headers = {'Content-Type': 'application/json; charset=utf-8'}

    response = requests.post(URLWrite, headers=headers, data=text_to_send.encode('utf-8'))

    #response = requests.post(URLWrite, json={"name":name,"type":mode,"command":command})
    print(response.content)
       
    timeout = 0
    badresponse_timeout = 0
    utlstatus = 'none' 
    while ((utlstatus.lower() != 'ready') and (badresponse_timeout < 10)):
        response = requests.get(URLRead)
        # Проверка состояния проекта: Старт/Стоп/Пауза
        ProjectState()
        if (response.status_code != 200):
            Stage("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code), 'error')
            print("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code) + '\n' + str(10 - badresponse_timeout) + ' tries left')
            badresponse_timeout += 1
        else:
            y = json.loads(response.content)
            utlstatus = y.get('utilitystatus')
            if (mode.lower() == 'get'):
                utldata = y.get('utilitydata')
            timeout += 1
            #Stage('Wait ' + str(timeout))
        sleep(0.05)

    if (badresponse_timeout >= 10):
        Stage("ERROR IN PYTHON LIBRARY! Function exit because of bad responses", 'error')
        print("ERROR IN PYTHON LIBRARY! Function exit because of bad responses")
        value = None
        return value

    if ((utlstatus.lower() == 'ready') and (mode.lower() == 'get')):
        #Stage(utldata)
        ind = utldata.find(';')
        if (ind == -1):
            utldata = utldata + ';'
        ind = utldata.rfind(';')
        if (ind != (len(utldata)-1)):
            utldata = utldata + ';'
        value = ParseValue(utldata, valuetype)
        return value

    value = None
    return value


###################################################################################################################

    #######         ######          #############
    ##     ##       ##    ##        ##         ##
    ##      ##      ##     ##       ##         ##
    ##     ##       ##   ##         ##         ##
    #######         ## ##           ##         ##
    ##              ####            ##         ##
    ##              ## ##           ##         ##
    ##              ##   ##         ##         ##
    ##              ##     ##       #############

###################################################################################################################    

# program - функция, осуществляющая управление программой MOKO SE (скриптами, проектами и т.д.)
# name - название типа, которым нужно управлять ('script', 'project', etc.)
# mode - тип команды (пока что только 'set') 
# command - команда, которую посылаем в MOKO SE
# valuetype (только для type = 'get') - получаемый тип данных
def Program(name, mode, command, valuetype='void'):
    """ 
    Функция осуществляет управление программой MOKO SE (скриптами, проектами и т.д.)

    :param str name: название типа, которым нужно управлять ('script', 'project', etc.)
    :param str mode: тип команды (пока что только **'set'**).
    :param str command: Команда, которую посылаем в MOKO SE.
    :param str valuetype: (только для mode = 'get') Тип возвращаемых данных. По умолчанию *void*.
    :return: Функция возвращает *None* (если mode = **'set'**) либо полученные данные (если mode = **'get'**)
    :rtype: Возвращаемый тип данных меняется в зависимости от полученных из отчёта значений

    **Пример:**

    **1.**
    Нам нужно дать серверу знать, что скрипт окончен. для этого напишем следующую команду:

    >>> Program('script', 'set', 'done')

    В случае успешного выполнения в терминале должна появиться следующая строка:

    b'{"name": "script", "type": "set", "command": "done"}'
    
    Функция должна вернуть следующее значение:

    ``None``

    Иначе не выполняется, либо в терминале отобразится, например, следующая строка:

    ``b'<!DOCTYPE html><html><head><title>Bad Request</title></head><body><h2>Access Error: 400 -- Bad Request</h2><pre>Bad Request</pre></body></html>'``
    """
    # Проверка состояния проекта: Старт/Стоп/Пауза
    ProjectState()
    if ((mode.lower() == 'get') and (valuetype.lower() == 'void')):
        Stage("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request", 'error')
        print("ERROR IN PYTHON LIBRARY! Return value type is not specified for GET request")
        return None
    if ((mode.lower() != 'get') and (mode.lower() != 'set') and (mode.lower() != 'init') and (mode.lower() != 'close')):
        Stage("ERROR IN PYTHON LIBRARY! Wrong request type! " +  str(mode), 'error')
        print("ERROR IN PYTHON LIBRARY! Wrong request type! " +  str(mode))
        return None
    URLWrite = _UrlProgramWrite
    URLRead = _UrlProgramRead

    response = requests.post(URLWrite, json={"name":name,"type":mode,"command":command})	
    print(response.content)
       
    timeout = 0
    badresponse_timeout = 0
    progstatus = str("none")
    while ((progstatus.lower() != "ready") and (badresponse_timeout < 10)):
        response = requests.get(URLRead)
        # Проверка состояния проекта: Старт/Стоп/Пауза
        ProjectState()
        if (response.status_code != 200):
            Stage("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code), 'error')
            print("ERROR IN PYTHON LIBRARY! Bad response code! " + str(response.status_code) + '\n' + str(10 - badresponse_timeout) + ' tries left')
            badresponse_timeout += 1
        else:
            y = json.loads(response.content)
            progstatus = y.get('programstatus')
            if (mode.lower() == 'get'):
                progdata = y.get('programdata')
            timeout += 1
            #Stage('Wait ' + str(timeout))
        sleep(0.05)

    if (badresponse_timeout >= 10):
        Stage("ERROR IN PYTHON LIBRARY! Function exit because of bad responses", 'error')
        print("ERROR IN PYTHON LIBRARY! Function exit because of bad responses")
        value = None
        return value

    if ((progstatus.lower() == 'ready') and (mode.lower() == 'get')):
        #Stage(progdata)
        ind = progdata.find(';')
        if (ind == -1):
            progdata = progdata + ';'
        ind = progdata.rfind(';')
        if (ind != (len(progdata)-1)):
            progdata = progdata + ';'
        value = ParseValue(progdata, valuetype)
        return value

    value = None
    return value

def ProgramParam(name, param, valuetype):
    URLRead = _UrlProgramRead + '/' + str(name) + '=' + str(param)

    response = requests.get(URLRead)	
    print(response.content)
    return

def EndScript(command='done'):
    """ 
    **Обязательная** функция, которая должна быть в конце каждого скрипта. Даёт знать серверу, что скрипт закончен.
    """
    res = Program('script','set',command)
    return res

def Script_CancelNumber(number):
    if (number.isdigit):
        res = Program('script','set','canceled = number ' + str(number))
    else:
        print('ERROR IN PYTHON LIBRARY! Wrong parameter for Cancel Number command! ' + str(number))
        res = Stage('ERROR IN PYTHON LIBRARY! Wrong parameter for Cancel Number command! ' + str(number),'error')
    return res

def Script_CancelName(name):
    res = Program('script','set','canceled = name ' + str(name))
    return res

###################################################################################################################

    ##        ##    ############    ##              ######
    ##        ##    ##              ##              ##    ##
    ##        ##    ##              ##              ##    ##
    ##        ##    ##              ##              ##  ##
    ############    ######          ##              ####
    ##        ##    ##              ##              ##
    ##        ##    ##              ##              ##
    ##        ##    ##              ##              ##
    ##        ##    ############    #############   ##        

###################################################################################################################

# ParseValue - функция, которая парсит полученные данные из других функций с mode = 'get' под указанный тип данных valuetype
# data - данные для парсинга
# valuetype - тип данных, который должен получиться на выходе
def ParseValue(data, valuetype='void'):
    # если вдруг дефолтное или пустое значение valuetype на входе
    # то возвращаем None с занесением в Stage и терминал
    if ((valuetype == 'void') or (valuetype == '')):
        Stage('ERROR IN PYTHON LIBRARY! Type is not specified', 'error')
        print('ERROR IN PYTHON LIBRARY! Type is not specified') 
        return None
    if valuetype.lower() == 'arraystring':
        value = (data.split(';'))
        if value[-1] == '' and data[-1] == ';':
            value.pop(-1)
        return value
    # если нет разделителя ";"
    # то возвращаем None с занесением в Stage и терминал
    ind = data.find(';')
    if (ind == -1):
        Stage('ERROR IN PYTHON LIBRARY! Bad data received! ' + data, 'error')
        print('ERROR IN PYTHON LIBRARY! Bad data received! No ";" at the end! ' + data) 
        return None

    # если разделитель есть и это последний символ в строке
    if ((ind == data.rfind(';')) and (ind == (len(data)-1))):
        # разделение строки на подстроки (чтоб примерно одинаковая схема была у одномерного массива/строки/etc.)
        spl = data.split(';',maxsplit=1)
        #если

        if (valuetype.lower() == 'string'):
            result = spl[0]
            return result
        indcomma = data.find(',')

        if (indcomma == -1):
            indperiod = data.find('.')
            val = spl[0]

            if (indperiod == -1):
                if ((val.lower() == "true") or (val.lower() == "false")):
                    if (val.lower() == "true"):
                        result = True
                    if (val.lower() == "false"):
                        result = False
                else:
                     result = int(val)
                return result
            else:
                result = float(val)
                return result
        else:
            arr = spl[0].split(',')

            result = [ ]
            
            for x in arr:
                if (x != ""):
                    indperiod = x.find('.')
                
                    if (indperiod == -1):
                        if ((x.lower() == "true") or (x.lower() == "false")):
                            if (x.lower() == "true"):
                                result.append(True)
                            if (x.lower() == "false"):
                                result.append(False)
                        else:
                            result.append(int(x))
                    else:
                        result.append(float(x))

            return result
    else:
        spl = data.split(';')
        result = []

        for x in spl:
            if (x != ""):
                indcomma = x.find(',')
                rarr = []
                if (indcomma == -1):
                    indperiod = x.find('.')
                    val = x

                    if (indperiod == -1):
                        if ((val.lower() == "true") or (val.lower() == "false")):
                            if (val.lower() == "true"):
                                rarr.append(True)
                            if (val.lower() == "false"):
                                rarr.append(False)
                        else:
                            rarr.append(int(x))
                    else:
                        rarr.append(float(val))

                else:
                    arr = x.split(',')
            
                    for x in arr:
                        if (x != ""):
                            indperiod = x.find('.')
                
                            if (indperiod == -1):
                                if ((x.lower() == "true") or (x.lower() == "false")):
                                    if (x.lower() == "true"):
                                        rarr.append(True)
                                    if (x.lower() == "false"):
                                        rarr.append(False)
                                else:
                                    rarr.append(int(x))
                            else:
                                rarr.append(float(x))
                result.append(rarr)
        return result

    return

#ProjectState - предназначена для проверки старта/паузы/стопа
def ProjectState():
    URLPSRead = _UrlProjectStateRead
    serverstate = requests.get(URLPSRead)
    JSONprojectstate = json.loads(serverstate.content)
    projectstate = JSONprojectstate.get('projectstate')
    while (projectstate.lower() != 'run'):
        sleep(0.05)
        serverstate = requests.get(URLPSRead)
        JSONprojectstate = json.loads(serverstate.content)
        projectstate = JSONprojectstate.get('projectstate')
        if (projectstate.lower() == 'stop'):
            sys.exit()
            Stage("sys.exit() not work")
    return