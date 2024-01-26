import cv2

img=cv2.imread("solar-system.jpg")

rocket=img[120:360,400:500]

img[110:350,390:490]=rocket

mercury="mercury"
cv2.putText(img,mercury,(90,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,200,0))

venus="venus"
cv2.putText(img,venus,(180,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,200,0))

earth="earth"
cv2.putText(img,earth,(270,170),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,200,0))

mars="mars"
cv2.putText(img,mars,(360,250),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,200,0))

juipiter="juipiter"
cv2.putText(img,juipiter,(540,50),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,200,0))

saturn="saturn"
cv2.putText(img,saturn,(770,130),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,200,0))

uranus="uranus"
cv2.putText(img,uranus,(930,280),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,200,0))

neptune="neptune"
cv2.putText(img,neptune,(1100,130),fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,fontScale=1,color=(255,200,0))


cv2.imshow("output",img)

cv2.waitKey(10*1000)


