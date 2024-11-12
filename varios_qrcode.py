import qrcode 
from qrcode.image.styledpil import StyledPilImage


redes_sociais = {
    "Facebook": "https://www.facebook.com/hashtagprogramacao",
    "Instagram": "https://www.instagram.com/hashtagprogramacao",
    "YouTube": "https://www.youtube.com/@HashtagProgramacao",
    "TikTok": "https://www.tiktok.com/@hashtagprogramacao",
}

for rede_social, url in redes_sociais.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)

    imagem = qr.make_image(
        image_factory=StyledPilImage,
        embeded_image_path="logo.png",
    )

    imagem.save(f"sociais_{rede_social}.png")