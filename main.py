import qrcode

data = "https://www.instagram.com/jaiswalprathu32/"

qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode4.png")

print("qr code created successfully")