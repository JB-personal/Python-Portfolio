# install the qrcode libraries needed
import qrcode

def generate_qrcode(text):


    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=5
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("qrimg.png")

URL = input("Enter your url: ")
generate_qrcode(URL)
# convert link to qr code

# create function that collects the text and converts it into a qr code

# save the qrcode as an image

# run the function