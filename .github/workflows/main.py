import pyqrcode
import png
import cv2
from pyzbar.pyzbar import decode
import webbrowser

# -- QR Code Generator --
def create_qr_code(data, filename='qr.png'):
    qr = pyqrcode.create(data)
    qr.png(filename, scale=6)
    print(f"QR code created and saved as {filename}")

# -- Barcode/QR Scanner from Image --
def scan_codes_from_image(image_path):
    image = cv2.imread(image_path)
    codes = decode(image)
    for code in codes:
        code_data = code.data.decode('utf-8')
        code_type = code.type
        print(f"Detected {code_type}: {code_data}")
        if code_data.startswith("http"):
            webbrowser.open(code_data)

# -- Barcode/QR Scanner from Webcam --
def scan_codes_from_webcam():
    cap = cv2.VideoCapture(0)
    print("Starting webcam scanning. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        codes = decode(frame)
        for code in codes:
            code_data = code.data.decode('utf-8')
            code_type = code.type
            print(f"Detected {code_type}: {code_data}")
            (x, y, w, h) = code.rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'{code_type}: {code_data}', (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
            if code_data.startswith("http"):
                webbrowser.open(code_data)
        cv2.imshow('QR and Barcode Scanner', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Example usage
if __name__ == '__main__':
    # Create a QR code
    create_qr_code('https://example.com', 'example_qr.png')
    # Scan from an image file
    # scan_codes_from_image('barcode_or_qr.png')
    # Scan using the webcam
    # scan_codes_from_webcam()
