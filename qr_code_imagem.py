import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H) # para poder adicionar imagens
qr.add_data("https://www.google.com.br")

imagem = qr.make_image(image_factory=StyledPilImage, embeded_image_path="logo.png")

imagem.save("Qrcode_logo.png")