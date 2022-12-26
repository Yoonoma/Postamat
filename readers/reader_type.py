from threading import Thread
from enum import Enum
import serial
from loguru import logger


# class Reader:
#     def __init__(self, port: str):
#         # порт
#         self.ser = None
#         self.event = threading.Event()
#
#         self.reader_init(port)
#         self.thr = threading.Thread(target=self._read, name=f"reader-[{port}]", daemon=False).start()
#
#     def reader_init(self, port: str):
#         self.ser = serial.Serial()
#         self.ser.port = port
#         self.ser.baudrate = 9600
#         self.ser.bytesize = serial.EIGHTBITS
#         self.ser.stopbits = serial.STOPBITS_ONE
#         self.ser.parity = serial.PARITY_NONE
#         self.ser.timeout = 1
#
#         try:
#             self.ser.open()
#             logger.debug(f"Open serial port[{port}]")
#         except serial.serialutil.SerialException as opening_error:
#             logger.error(f"Cannot open serial port[{port}] : {opening_error}")
#             return
#
#
#     def _read(self, ):
#         if self.ser.isOpen():
#             while True:
#                 try:
#                     # считать данные, если в буфере сканера есть данные
#                     if self.ser.inWaiting() > 0:
#                         data = self.ser.readline().replace(b'\r\n', b'').decode("utf-8")
#
#                         print(data)
#
#                 except serial.SerialException as error_read:
#                     logger.error(f"Error with ser.readline : {error_read}")
#                     return
#         else:
#             logger.error(f"Serial port [{self.ser}] - not open!")
#
#     def __del__(self):
#         try:
#             self.ser.close()
#             logger.info(f"Closed serial port[{self.ser.port}]")
#         except serial.SerialException as error_closed:
#             logger.error(f"Error Serial port[{self.ser.port}] closing: [{error_closed}]")


class Reader(Thread):
    def __init__(self, name_reader: str, device: Enum, func_scanner_handler):
        super().__init__(name=name_reader, daemon=True)
        self.ser = None
        self.deivce = device
        self.data = ""
        self.handler = func_scanner_handler
        self._reader_init(self.deivce.value)
        self.start()

    def run(self):
        logger.debug(f"Start scanner [{self.deivce}]")
        self._read()

    def scan_key(self):
        self.data = ""
        while not self.data:
            pass
        return self.data

    def _reader_init(self, port):
        self.ser = serial.Serial()
        self.ser.port = port
        self.ser.baudrate = 9600
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.parity = serial.PARITY_NONE
        self.ser.timeout = 1

        try:
            self.ser.open()
            logger.debug(f"Open serial port[{port}]")
        except serial.serialutil.SerialException as opening_error:
            logger.error(f"Cannot open serial port[{port}] : {opening_error}")
            raise

    def _read(self):
        if self.ser.isOpen():
            while True:
                try:
                    # считать данные, если в буфере сканера есть данные
                    if self.ser.inWaiting() > 0:
                        self.data = self.ser.readline().replace(b'\r\n', b'').decode("utf-8")
                        self.handler(self.data, self.deivce)

                except serial.SerialException as error_read:
                    logger.error(f"Error with ser.readline : {error_read}")
                    return
        else:
            logger.error(f"Serial port [{self.ser}] - not open!")

    def __del__(self):
        try:
            self.ser.close()
            logger.info(f"Closed serial port[{self.ser.port}]")
        except serial.SerialException as error_closed:
            logger.error(f"Error Serial port[{self.ser.port}] closing: [{error_closed}]")
