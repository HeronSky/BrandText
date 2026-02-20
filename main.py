from PIL import Image,ImageDraw,ImageFont

text = input("Enter the text to be drawn:")

style = "G"

font_size = 240

font_zh = ImageFont.truetype("fonts/NotoSansTC-Bold.ttf",font_size)

if style == "G":
    colors = ["#4285F4", "#EA4335", "#FBBC05", "#4285F4", "#34A853", "#EA4335"]
    font_en = ImageFont.truetype("fonts/GoogleSansFlex_120pt-Medium.ttf",font_size)
    font_num = ImageFont.truetype("fonts/GoogleSansFlex_120pt-Medium.ttf",font_size)



new_width = len(text) * font_size * 3
new_height = font_size * 3
canva = Image.new("RGBA", (int(new_width), int(new_height)), (255, 255, 255, 0))
draw = ImageDraw.Draw(canva)

current_x = 100 
current_y = 100


for i in range(len(text)):
    if text[i].isdigit():
        target_font = font_num
        offset_y = 0       
        letter_spacing = 0  
    elif not text[i].isascii():
        target_font = font_zh      
        offset_y = 0               
        letter_spacing = 0
    else:
        target_font = font_en       
        offset_y = 0                
        letter_spacing = 0         


    draw.text((current_x, current_y + offset_y), text[i], fill=colors[i % len(colors)], font=target_font)

    bbox = draw.textbbox((0, 0), text[i], font=target_font)
    char_w = bbox[2] - bbox[0]
    current_x += char_w + letter_spacing

crop_bbox = canva.getbbox()

if crop_bbox:
    left,top,right,bottom =crop_bbox
    margin = 20 
    new_bbox = (left-margin,top-margin,right+margin,bottom+margin)
    
    final_logo = canva.crop(new_bbox) 
    final_logo.save(f"brandtext_{text}.png")
