import cv2

img = cv2.imread('dob.jpg')

while True:
    cv2.imshow('Dog',img)
    
    #If we wait 1 millisecond AND we have pressed the esc key
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.destroyAllWindows()