import os
import dotenv
from enum import Enum

dotenv.load_dotenv("../TestTask/resources/.env")

# [Сupboard]
cupboard = {
    "count_cells": 21,
    "window_width": 800,  # 1024,
    "window_height": 800  # 1280
}

ADMIN_KEY = os.environ["ADMIN_KEY"]

# [Database]
PWD_DB = '../TestTask/resources/metki.db'  # os.path.dirname(sys.modules['__main__'].__file__)

database = {
    "header_User": ["ID метки", "Ключ метки", "RFID-Код", "QR-Код", "Взята ли метка"],
    "QR_PREFIX": "INXPG"  # Необходим для отличия между qr-кодами для id-меток и id-пользователей
}

class TablesDatabase(Enum):
    user = "User"


# [Состояния сканера]
class ScannerState(Enum):
    expectation = 0
    standby = -1
    user = 1
    admin = 2
    read_only_qr = 5
    read_only_rfid = 10
    new_user = 15


class Device(Enum):
    # [QR]
    QR = '/dev/ttyACM1'
    # [RFID]
    RFID = '/dev/ttyACM0'


# [GPIO]
gpio_config = {
    "addresses_buttons_mcp": {
        1: (0x27, 'GPIOB', 0b00000001),
        2: (0x27, 'GPIOB', 0b00000010),
    },
    "addresses_locks_mcp": {
        1: (0x27, 'GPIOA', 0b00000001),
        2: (0x27, 'GPIOA', 0b00000010),
    },

    "_addresses_locks_mcp": {  # addresses_buttons_mcp
        1: (0x20, 'GPIOB', 0b00001000),  # b3    000
        2: (0x23, 'GPIOA', 0b00000100),  # a2    011
        3: (0x23, 'GPIOB', 0b00000001),  # b0    011
        4: (0x23, 'GPIOB', 0b01000000),  # b6    011
        5: (0x24, 'GPIOA', 0b00000100),  # a2    100
        6: (0x20, 'GPIOB', 0b00010000),  # b4    000
        7: (0x23, 'GPIOA', 0b00000010),  # a1    011
        8: (0x23, 'GPIOB', 0b00001000),  # b3    011
        9: (0x23, 'GPIOB', 0b10000000),  # b7    011
        10: (0x24, 'GPIOB', 0b10000000),  # b7    100
        11: (0x20, 'GPIOB', 0b00100000),  # b5    000
        12: (0x23, 'GPIOA', 0b00100000),  # a5    011
        13: (0x23, 'GPIOA', 0b01000000),  # a6    011
        14: (0x23, 'GPIOB', 0b00100000),  # b5    011
        15: (0x24, 'GPIOA', 0b01000000),  # a6    100
        16: (0x23, 'GPIOA', 0b00001000),  # a3    011
        17: (0x23, 'GPIOA', 0b10000000),  # a7    011
        18: (0x23, 'GPIOB', 0b00000100),  # b2    011
        19: (0x23, 'GPIOB', 0b00010000),  # b4    011
        20: (0x24, 'GPIOA', 0b10000000),  # a7    100
        21: (0x24, 'GPIOB', 0b00010000),  # Service cell
    },
    "_addresses_buttons_mcp": {  # addresses_locks_mcp
        1: (0x20, 'GPIOA', 0b10000000),  # a7    000
        2: (0x20, 'GPIOB', 0b01000000),  # b6    000
        3: (0x21, 'GPIOB', 0b00000001),  # b0    001
        4: (0x20, 'GPIOA', 0b01000000),  # a6    000
        5: (0x20, 'GPIOB', 0b00000001),  # b0    000
        6: (0x20, 'GPIOA', 0b00001000),  # a3    000
        7: (0x20, 'GPIOA', 0b00100000),  # a5    000
        8: (0x21, 'GPIOA', 0b00000100),  # a2    001
        9: (0x20, 'GPIOA', 0b00010000),  # a4    000
        10: (0x20, 'GPIOB', 0b10000000),  # b7    000
        11: (0x20, 'GPIOA', 0b00000010),  # a1    000
        12: (0x21, 'GPIOB', 0b10000000),  # b7    001
        13: (0x21, 'GPIOA', 0b00010000),  # a4    001
        14: (0x20, 'GPIOA', 0b00000100),  # a2    000
        15: (0x21, 'GPIOA', 0b10000000),  # a7    001
        16: (0x20, 'GPIOB', 0b00000010),  # b1    000
        17: (0x21, 'GPIOB', 0b00000100),  # b2    001
        18: (0x21, 'GPIOA', 0b01000000),  # a6    001
        19: (0x20, 'GPIOB', 0b00000100),  # b2    000
        20: (0x21, 'GPIOB', 0b01000000),  # b6    001
        21: (0x21, 'GPIOB', 0b00000010),  # Service cell
    },

    # "service_cell_l": (0x20, 'GPIOB', 0b00000100),
    # "service_cell_b": (0x20, 'GPIOA', 0b00010000),
    "bus": 0,  # /dev/i2c-0
    "time_loopl_ms": 1000,
    "time_open_lock_s": 0.1,
    "open_cell_numbers": [],
    "long_open_cell_numbers": [],
    "test": [],
    "addr_map": {
        0x00: 'IODIRA', 0x01: 'IODIRB', 0x02: 'IPOLA',
        0x03: 'IPOLB', 0x04: 'GPINTENA', 0x05: 'GPINTENB',
        0x06: 'DEFVALA', 0x07: 'DEVFALB', 0x08: 'INTCONA',
        0x09: 'INTCONB', 0x0a: 'IOCON', 0x0b: 'IOCON',
        0x0c: 'GPPUA', 0x0d: 'GPPUB', 0x0e: 'INTFA',
        0x0f: 'INTFB', 0x10: 'INTCAPA', 0x11: 'INTCAPB',
        0x12: 'GPIOA', 0x13: 'GPIOB', 0x14: 'OLATA',
        0x15: 'OLATB',
    },
    "time_to_close_cell_ms": 100,
    "error": [],
    "time_to_init_again_s": 600,
}

gpio_config["reg_map"] = {value: key for key, value in gpio_config["addr_map"].items()}
