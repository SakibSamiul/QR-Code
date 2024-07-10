import qrcode as qr

image = qr.make("https://www.linkedin.com/in/samiulsakib97/")

image.save("linkedIn.png")
