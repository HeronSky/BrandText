from PIL import Image, ImageDraw, ImageFont

def render(text, font_size):
    COLOR = "#E50914"     
    STRETCH = 0.75        
    SPACING = 20          
    CURVE = 30         

    text = text.upper()   

    try:
        font = ImageFont.truetype("fonts/Roboto-Bold.ttf", font_size)
    except:
        font = ImageFont.load_default()

    char_images = []
    for char in text:
        temp_w, temp_h = font_size * 2, font_size * 2
        temp = Image.new("RGBA", (temp_w, temp_h), (0, 0, 0, 0))
        ImageDraw.Draw(temp).text((0, 0), char, fill=COLOR, font=font)
        
        bbox = temp.getbbox()
        if bbox:
            img = temp.crop(bbox)
            new_w = max(1, int(img.width * STRETCH))
            img = img.resize((new_w, img.height), Image.Resampling.LANCZOS)
            char_images.append(img)

    total_w = sum(img.width for img in char_images) + (len(char_images) - 1) * SPACING
    max_h = max(img.height for img in char_images)
    combined = Image.new("RGBA", (total_w, max_h), (0, 0, 0, 0))
    
    x_offset = 0
    for img in char_images:
        combined.paste(img, (x_offset, 0))
        x_offset += img.width + SPACING

    W, H = combined.size
    final = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    for x in range(W):
        progress = (x - W/2) / (W/2)
        offset = CURVE * (1 - progress**2)
        
        slice_img = combined.crop((x, 0, x + 1, H))
        new_h = max(1, int(H - offset))
        slice_img = slice_img.resize((1, new_h), Image.Resampling.LANCZOS)
        final.paste(slice_img, (x, 0))

    return final