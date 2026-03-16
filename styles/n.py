from PIL import Image,ImageDraw,ImageFont

def render(text,font_size,curve=30):
    COLOR = "#E50914"     
    STRETCH = 0.75      
    SPACING = int(font_size * 0.1) 
    CURVE = curve         

    text = text.upper()   

    try:
        font = ImageFont.truetype("fonts/Roboto-Bold.ttf",font_size)
    except:
        font = ImageFont.load_default()

    char_images = []
    for char in text:
        left,top,right,bottom = font.getbbox(char)
        w,h = int(right - left),int(bottom - top)
        
        temp = Image.new("RGBA",(max(w,1),max(h,1)),(0,0,0,0))
        ImageDraw.Draw(temp).text((-left,-top),char,fill=COLOR,font=font)
        
        new_w = max(1, int(temp.width * STRETCH))
        temp = temp.resize((new_w,temp.height),Image.Resampling.LANCZOS)
        char_images.append(temp)


    total_w = sum(img.width for img in char_images) + (len(char_images) - 1) * SPACING
    max_h = max(img.height for img in char_images)
    combined = Image.new("RGBA",(total_w,max_h + CURVE),(0,0,0,0))
    
    x_offset = 0
    for img in char_images:
        combined.paste(img,(x_offset,0))
        x_offset += img.width + SPACING

    W, H = combined.size
    final = Image.new("RGBA",(W, H),(0,0,0,0))
    for x in range(W):
        progress = (x-W/2)/(W/2)
        offset = CURVE * (progress**2) 
        
        slice_img = combined.crop((x,0,x+1,H))
        final.paste(slice_img, (x, int(offset)))

    return final