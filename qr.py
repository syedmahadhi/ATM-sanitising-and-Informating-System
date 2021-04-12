import cv2
cap = cv2.VideoCapture(0)

def dectector():
    detector = cv2.QRCodeDector()
    while True:
        _, img = cap.read()
        data, vertices_array, _ = detector.detectAndDecode(img)

        if vertices_array is not None:
            if data:
                print("QR Code detected, data:", data)
            cv2.imshow("img", img)
            break
