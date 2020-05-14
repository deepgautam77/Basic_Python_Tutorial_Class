import cv2

img = cv2.imread('messi5.jpg',-1)
print(img)

cv2.imshow('image',img)         #show image when running program
cv2.waitKey(0)                  #decides how long to preview shown image in terms of millisecond
cv2.destroyAllWindows()         #closes all processes that ran above it once the program is closed.

cv2.imwrite('messi5_copy.png', img)     #creates a copy of file and changes file type as given ('img' in this line)
