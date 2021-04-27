from key import *
import qrcode
from threading import Timer

class QR:
    def __init__(self):
        self.url = 'https://berodimas.netlify.app/'
        self.key = Key(self.url)
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )

    def key_generator(self):
        pass

    def qr_generator(self):
        # Timer(5, self.qr_generator).start()
        key = Key()
        print(key)
        self.qr.add_data(key)
        self.qr.make(fit=True)
        img = self.qr.make_image(fill='black', back_color='white')
        img.save('qr.png')
        self.qr.clear()

if __name__ == "__main__":
    qr = QR()
    qr.qr_generator()
