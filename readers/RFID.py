import threading
from threading import Thread, Event
from serial_tool import serial

from resources.config import PORT_RFID

import serial

# REMOVE IMPORT
from resources import config
import time

'''
    ?как ждать данные, не нагружая CPU?
    while True:
        while ser.inWaiting() == 0:
            pass
        #необходимая работа с данными...


        import serial
import config

port_RFID = serial.Serial(config.PORT_RFID, timeout=None)

exitFlag = True

while exitFlag:
    if port_RFID.inWaiting() > 0:
        input_rfid = port_RFID.readline().replace(b'\r\n', b'').decode("utf-8")
        print(input_rfid)
        if input_rfid == '87 A9 D7 00 00 00 00 00':
            print('Admin. is_open() : ', )
            port_RFID.close()
            exitFlag = False
'''







# class ControlThread(Thread):
#     def __init__(self, group=None, target=None, name=None,
#                  args=(), kwargs={}, Verbose=None):
#         Thread.__init__(self, group, target, name, args, kwargs)
#         self.stop_event = Event()
#
#     def stopped(self):
#         return self.stop_event.is_set()
#
#     def sleep(self, seconds):
#         self.stop_event.wait(seconds)
#
#     def stop(self):
#         self.stop_event.set()
#
#
# class QrReaderThread(ControlThread):
#     pass
#
#
# # Класс должен просто подключаться и создавать поток
# class QrReader:
#     def __init__(self, port=None, baudrate=None, timeout=None):
#         self.thr = None
#         self._serial_port = port
#         self._baudrate = baudrate
#         self._timeout = timeout
#
#         self.port = self.__get_port()
#
#     def get_thread(self, target, *args):
#         self.thr = threading.Thread(target=target, args=args,
#                                     name=f'thr-Qr[{threading.active_count()}]')
#         return self.thr
#
#     def __get_port(self):
#         try:
#             port = serial.Serial(port=self._serial_port, baudrate=self._baudrate, timeout=self._timeout)
#             return port
#         except serial.SerialException as var:
#             # Log
#             print('Com Port Not Open Error : ', var)
#             return 5
#
#     def close(self):
#         self.port.close()
#
#
# def func(num):
#     print(num)
#     time.sleep(2)
#
#
# qr = QrReader(config.PORT_QR, config.BAUDRATE_QR, config.TIMEOUT_QR)
#
# if qr.port != 5:
#     qr.close()