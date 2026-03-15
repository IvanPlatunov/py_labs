import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret: break
    h,w,_ = frame.shape
    cx_frame = w // 2
    cy_frame = h // 2
    x1 = cx_frame - 100
    y1 = cy_frame - 100
    x2 = cx_frame + 100
    y2 = cy_frame + 100
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
    if center != None and x1<center[0]<x2 and y1<center[1]<y2:
        cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),3)
    else: 
         cv2.rectangle(frame,(x1,y1),(x2,y2),(0,0,255),3)
    cv2.imshow("Image", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()