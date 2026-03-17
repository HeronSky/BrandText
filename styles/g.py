from PIL import Image,ImageDraw,ImageFont

def render(text,font_size):
    colors = ["#4285F4","#EA4335","#FBBC05","#4285F4","#34A853","#EA4335"]
    try:
        font_en = font_num = ImageFont.truetype("fonts/GoogleSansFlex.ttf",font_size)
        font_zh = ImageFont.truetype("fonts/NotoSansTC-Bold.ttf",font_size)
    except:
        font_en = font_num = font_zh = ImageFont.load_default()
        
    new_width = len(text) * font_size * 3
    new_height = font_size * 3
    canva = Image.new("RGBA",(int(new_width),int(new_height)),(255,255,255,0))
    draw = ImageDraw.Draw(canva)

    current_x = current_y = 100

    for i in range(len(text)):
        if text[i].isdigit():
            target_font = font_num
        elif not text[i].isascii():
            target_font=font_zh      
        else:
            target_font=font_en            

        draw.text((current_x,current_y),text[i],fill=colors[i % len(colors)],font=target_font)

        bbox = draw.textbbox((0,0),text[i],font=target_font)
        char_w = bbox[2] - bbox[0]
        current_x += char_w

    crop_bbox = canva.getbbox()
    if crop_bbox:
        left,top,right,bottom = crop_bbox
        margin = 20 
        new_bbox = (left - margin, top - margin, right + margin, bottom + margin)
        return canva.crop(new_bbox) 
    return canva