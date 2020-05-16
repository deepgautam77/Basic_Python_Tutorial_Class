import cv2

img = cv2.imread('messi5.jpg',-1)
print(img)

cv2.imshow('image',img)         #show image when running program
k = cv2.waitKey(0)                  #decides how long to preview shown image in terms of millisecond

if k==27:                           #27 is code for ESC key.
    cv2.destroyAllWindows()         #closes all processes that ran above it once the program is closed.
elif k==ord('s'):                   #if someone presses s, program will make a copy of that image in png format.
    cv2.imwrite('messi5_copy.png', img)     #creates a copy of file and changes file type as given ('img' in this line)
    cv2.destroyAllWindows()