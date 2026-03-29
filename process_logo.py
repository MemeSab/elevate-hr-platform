from PIL import Image

def process_logo(input_path, output_path):
    img = Image.open(input_path).convert("RGBA")
    data = img.getdata()
    new_data = []
    
    for item in data:
        # Check if the pixel is dark (text) or bright (background)
        intensity = (item[0] + item[1] + item[2]) / 3
        if intensity > 200:
            # White background -> fully transparent
            new_data.append((255, 255, 255, 0))
        else:
            # Dark text -> solid white, map darkness to opacity for anti-aliasing
            alpha = int(255 - intensity)
            new_data.append((255, 255, 255, alpha))
            
    img.putdata(new_data)
    img.save(output_path, "PNG")

process_logo("images/about-logo.jpg", "images/logo-white-transparent.png")
