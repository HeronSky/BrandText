from styles import g,n

def start():
    user_text = input("Enter text: ")
    user_style = input("Enter style (G/N): ").upper()

    if user_style == "G":
        final_image = g.render(user_text, 240)
    elif user_style == "N":
        final_image = n.render(user_text, 240)
    else:
        print("Error:// Invalid style.")
        return
    
    save_path = f"brandtext_{user_text}.png"
    final_image.save(save_path)
    print(f"Saved to: {save_path}")

if __name__ == "__main__":
    start()