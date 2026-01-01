import qrcode

data = "https://www.google.com"

qr = qrcode.make(data)

qr.show()   # 👈 direct display, save nahi hoga

print("QR Code displayed successfully")
