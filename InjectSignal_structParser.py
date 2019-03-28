import struct
import ctypes
import re
from CAN_structs import *
import time,subprocess
from subprocess import Popen,PIPE
import win32com.client
import datetime
from sets import Set
from itertools import izip_longest

# Operations:
READ_MSG = 1
SEND_MSG = 2

WAIT_MS_STEP = 100
CAN_LOG_INTERVAL_MS = 1000


def canInit():
    global comLib
    comClient = win32com.client
    try:
        comLib = comClient.GetObject('VirtualGPS.LibVirtualGPS')
        print 'Initialization succeeded\n'
    except:
        print 'Initialization failed.'
        comLib = comClient.Dispatch ('VirtualGPS.LibVirtualGPS')
        comLib = None


def get_arguments(args):
    default_interval = 1000
    args_amount      = 6
    return tuple(i[0] for i in izip_longest(args, range(args_amount), fillvalue=default_interval))


def send_signals(test_case):
    
    for operation in test_case:
        (delay_sec, operationType, CAN_ID, callback, args, send_interval) = get_arguments(operation)
        
        if operationType == SEND_MSG:
            time.sleep(delay_sec)
            try:
                comLib.CANPeriodicMessageStop(CAN_ID);
                comLib.CANSendPeriodicMessageStart('STR', CAN_ID, callback(args), send_interval, 1);
                # comLib.CANSendPeriodicMessageUpdate(CAN_ID, callback(args))
            except:
                print '\nCAN ID not found: {}'.format(CAN_ID)
                break
        elif operationType == READ_MSG:
            expected_signals = Set(callback(args).split(','))
            wait_ms_remaining = delay_sec * 1000
            got_match = False
            all_received_can = Set()
            
            # time_start = datetime.datetime.now().time().strftime('%H.%M.%S')
            while wait_ms_remaining > 0 and not got_match:
                wait_ms_remaining -= WAIT_MS_STEP
                time.sleep(WAIT_MS_STEP * 0.001)
                time_end   = datetime.datetime.now().time().strftime('%H.%M.%S')
                time_start = (datetime.datetime.now() - datetime.timedelta(milliseconds=CAN_LOG_INTERVAL_MS)).time().strftime('%H.%M.%S')
                try:
                    msg = comLib.logCANGet(time_start, time_end, ['{}'.format(CAN_ID)])
                    time_start = time_end
                    can_list = Set([i.split(':')[-1] for i in msg])
                    all_received_can.update(can_list)
                    for can in can_list:
                        received_signals = Set(comLib.CANGetSignalData(CAN_ID, can.replace(str(CAN_ID), '').strip()).split(' '))
                        if len(expected_signals.difference(received_signals)) == 0:
                            got_match = True
                            print '\t\tOK'
                            break
                except:
                    print '\nCAN ID not found: {}'.format(CAN_ID)
                    break
            
            if not got_match:
                print '\t\tFAILED'
                print '\t\tReceived CANs:'
                for can_msg in all_received_can:
                    print '\t\t\t{}'.format(can_msg)
                    # print '\t{}'.format(comLib.CANGetSignalData(CAN_ID, can_msg.replace(str(CAN_ID), '').strip()))
                break


def execute_test(test_case):
    if comLib is not None:
        send_signals(test_case)

canInit()
