import cv2

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("Error opening the camera. ")
    exit(0)
while True:
    ret , frame = cap.read()
    
    cv2.imshow('VideoCapture', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cap.destroyAllWindows()