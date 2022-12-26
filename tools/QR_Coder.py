import qrcode
from random import randint
from resources.config import database

def create_qr_code_img(code: str, id_user: int):
    # имя конечного файла
    filename = f"..TestTask/resources/qr_codes/{id_user}.png"
    # генерируем qr-код
    img = qrcode.make(code)
    # сохраняем img в файл
    img.save(filename)

def create_qr_code():
    prefix = database["QR_PREFIX"]
    code = randint(1000, 99999)
    result = prefix + str(code)
    return result