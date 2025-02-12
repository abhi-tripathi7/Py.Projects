import qrcode

def generate_qr_code(data, file_name):
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR Code, 1 is the smallest
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,  # size of each box in pixels
        border=4,  # thickness of the border (minimum is 4)
    )
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(file_name)
    print(f"QR Code saved as {file_name}")

# Example usage
if __name__ == "__main__":
    data = "https://www.google.com"  # Replace with your data
    file_name = "qrcode.png"  # Replace with your desired filename
    generate_qr_code(data, file_name)
