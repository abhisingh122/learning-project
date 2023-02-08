# Qrcode generator

import pyqrcode

content = "This is my content"
url=pyqrcode.create(content)
url.png("myqr.png", scale=5)
print("QR code is generated successfully")

