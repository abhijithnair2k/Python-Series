from PIL import Image , ImageDraw ,ImageFont
img = Image.open('download.jpg')
d = ImageDraw.Draw(img)
fnt = ImageFont.truetype("comicbd.ttf",25)
d.text((50,50),"Image Processing",font=fnt,fill=(255,200,432))
img.save('new.jpg')