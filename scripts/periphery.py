from resources import config

def check_qr():
    #qr_reader = QrReader(config.PORT_QR, config.BAUDRATE_QR, config.TIMEOUT_QR)

    if qr_reader.port == 5:
        # Log
        print('Com Port Not Open Error')
        return 0
    else:
        qr_reader.close()
        # Log
        print('Qr-Code scanner is ready to go.')
        return 1