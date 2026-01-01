import qrcode

data = input("Enter text/Link for QR code: ")

if not data.strip():   # strip() removes leading and trailing whitespace
  print("Input can not be empty")
else:
  qr = qrcode.make(data)
  qr.save("QR_Code_image.png")
  qr.show()   

print("QR Code displayed succaessfully and saved as QR_Code_image.png")
