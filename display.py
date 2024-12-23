
from PIL import Image, ImageDraw, ImageFont
def display(text = "你好,世界!"):
    image = Image.new("RGB", (1200, 800), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype('simhei.ttf', size=36)
    draw.text((600, 400), text, font=font, anchor="mm", fill=(0, 0, 0))
    image.show()
display('L import Image, ImageDraw, ImageFont')