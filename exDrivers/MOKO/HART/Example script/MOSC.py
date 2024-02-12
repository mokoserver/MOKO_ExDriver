'''
        MOKO Server Control
        This library contains functions for controlling MOKO SE functions, reports and utilities
        Many of these functions are the legacy of MOKO's previous projects
        First version from 26.02.2021
        The library was renamed to MOSC.py 15.03.2021

        The library depends on MOKO.py
'''

import MOKO
from time import sleep, monotonic

#####################################
#                FORMATTING
#####################################

round_3 = '{:.' + str(3) + 'f}'

def stars(word):
    """Заполняет строку звездочками"""
    formated_string = '{:*^60}'.format(word)
    return formated_string


def center_50(message):  # Align text with * filling
    return ('{:*^50}'.format(message))


def Stage_Header(test_name, GOST_point):
    MOKO.Stage(center_50('*'))
    MOKO.Stage(center_50(' Measurements of ' + test_name + ' '))
    MOKO.Stage(center_50(' check point ' + GOST_point + ' '))
    MOKO.Stage(center_50('*'))
    MOKO.Stage("")
    return


def format_header(header):  # formats the headers in the report by length
    h = header.split('\\n')
    len_max = 0
    for i in h:
        len(i)
        if len(i) > len_max:
            len_max = len(i)
    return header + '#' + str(len_max * 7.5) + ';'

################################################
#                SCRIPT CONTROLL AND STATE
################################################

# Delay script execution time
def Delay(minutes):
    MOKO.Stage('Delay script execution time for ' + str(minutes) + ' minutes')
    MOKO.Messenger('set', 'Info', "Please, wait for " + str(minutes) + " minutes while taking a measurement", 'void',
                   str(minutes * 60))
    return


def Done():
    MOKO.Report('ScriptState', 'set', 'string', 'Done')
    return


def Passed():
    MOKO.Report('ScriptState', 'set', 'string', 'Passed')
    return


def Failed():
    MOKO.Report('ScriptState', 'set', 'string', 'Failed')
    return


def ScriptState():
    state = MOKO.Report('ScriptState', 'get', 'string', 'string', 'string')
    if state == 'Done':
        MOKO.EndScript('done')
    elif state == 'Passed':
        MOKO.EndScript('passed')
    else:
        MOKO.EndScript('failed')
    return


#####################################
#                TREE & HESH
#####################################

def status_tree(HESH):
    MOKO.Program('tree', 'set', 'select = ' + HESH)
    status = MOKO.Program('tree', 'get', 'hesh ' + HESH, 'string')
    if status != 'canceled':
        return True
    return False


#####################################
#                UTILITY CONTROL
#####################################

def Report_Chek_Forcibly(report_name, utility, report_type='string'):
    NEM = 'And nothing else matters'
    Report = MOKO.Report(report_name, 'get', report_type, report_type, report_type)
    if Report.startswith(NEM):
        Report = MOKO.Utility(utility, 'get', report_name, report_type)
        if Report == '':
            Report = MOKO.Messenger('get', 'Please, enter the value', 'Enter the value of ' + report_name, report_type)
        MOKO.Report(report_name, 'set', report_type, Report)
    MOKO.Utility(utility, 'set', report_name + ' ' + Report)
    return Report


def Report_to_Utility(report_name, utility, report_type='string'):
    ECM = 'Empty case in memory'
    Report = MOKO.Report(report_name, 'get', report_type, report_type, report_type)
    if not Report.startswith(ECM):
        MOKO.Utility(utility, 'set', report_name + ' ' + Report)
    return Report


def Utility_to_Report(report_names, utility, report_type='string'):
    if report_type == 'strings':
        reports_names = ''
        data_reports = ''
        for i in report_names:
            reports_names += i + ';'
            report = MOKO.Utility(utility, 'get', i, 'string')
            data_reports += report + ';'
        MOKO.Report(reports_names, 'set', report_type, data_reports)
    else:
        report = MOKO.Utility(utility, 'get', report_names, 'string')
        MOKO.Report(report_names, 'set', report_type, report)
        return report
    return data_reports


#####################################
#                REPORTS
#####################################

# Function getting array of elements and createing tabular report, elements of array set to string
def table_report(reportName, result):
    dataString = str('')
    for i in result:
        element = str(i)
        dataString += (element + ';')
    dataString = dataString[0:-1]
    MOKO.Report(reportName, 'set', 'table', dataString)
    return


#####################################
#       Test iteration structure
#####################################

# Test function should have standard input & output:
# input -- [list of input parameters], HESH
# output -- [list of output parameters, where [0] element is a result of trial 'Good'/'Normal'/'Bad']
def iteration_structure(test_function, iterations = 3): # Decorator of iteration function
    def wrapper(input_paremeters, test_hesh):   # Wrapper of the function
        test_result = 0
        if status_tree(test_hesh):      # Checking up hesh
            test_iterator = 0           # Setting test iteration counter to 0
            while test_iterator < iterations:    # While cycle for trial
                # Here should be actual trial block, but in this example a user will choose trial's result
                test_result = test_function(input_paremeters, test_hesh)
                # This part sets up script's status after trial's result check, but you can use your local variable
                if test_result[0] == 'Good':
                    Done()
                    test_iterator = iterations
                elif test_result[0] == 'Normal':
                    Passed()
                    test_iterator = iterations
                # Here comes the iteration part, if trial's result is unsatisfactory
                elif test_result[0] == 'Bad':
                    Failed()
                    test_iterator += 1  # Incrementing iteration counter
                    if test_iterator == iterations:
                        # Asking the user for reiteration of the trial
                        reiteration = MOKO.Messenger('get', 'Test result is unsatisfactory', 'Would you like to restart?', 'boolean')
                        if reiteration:
                            test_iterator = 0
        return test_result
    return wrapper