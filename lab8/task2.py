import cv2
import numpy as np
cap = cv2.VideoCapture(0)
count = 0
while True:
    ret, frame = cap.read()
    if not ret: break
    h,w,_ = frame.shape
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    cont, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    center = None
    if cont:
        largest_cont = max(cont, key=cv2.contourArea)
        M = cv2.moments(largest_cont)
        if M["m00"] > 0:
            cx = int(M["m10"]/M["m00"])
            cy = int(M["m01"]/M["m00"])
            center = (cx, cy)
            cv2.circle(frame,center,5,(0,255,255),-1)
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()