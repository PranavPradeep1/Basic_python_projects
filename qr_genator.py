import qrcode
import os

def generate_qr_code(data, file_name="qrcode_output.png", folder="qrcodes"):
    """
    Logic: Generates a QR code image from data and saves it to a folder.
    """
    # Create directory if it doesn't exist
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    # Configure the QR code parameters
    qr = qrcode.QRCode(
        version=1, # 1 is the smallest (21x21 matrix)
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    # Create the image (RGB)
    img = qr.make_image(fill_color="black", back_color="white")
    
    path = os.path.join(folder, file_name)
    img.save(path)
    return path

def main():
    print("--- 📱 Python QR Code Generator ---")
    
    link = input("Enter the URL or text to encode: ")
    name = input("Enter the filename (e.g., my_qr.png): ")

    if not name.endswith(".png"):
        name += ".png"

    try:
        saved_path = generate_qr_code(link, name)
        print(f"\nSuccess! Your QR code is saved at: {saved_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()