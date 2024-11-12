import qrcode

imagem = qrcode.make("https://www.youtube.com/@HashtagProgramacao")
imagem.save("qrcode.png")