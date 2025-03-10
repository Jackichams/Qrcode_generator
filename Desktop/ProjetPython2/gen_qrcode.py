from platform import version

import qrcode
from qrcode.console_scripts import error_correction
from qrcode.constants import ERROR_CORRECT_L

qr = qrcode.QRCode(
    version =3,
    error_correction=ERROR_CORRECT_L,
    box_size=3,
    border=5
)

qr.add_data(input("entrez un lien : "))
qr.make(fit=True)
img = qr.make_image(fill_color="grey", back_color="white")
img.save('qrcode.png')