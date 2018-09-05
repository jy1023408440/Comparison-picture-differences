import cv2
import numpy as np
import matplotlib as plt

pp0="1-0.jpg"
pp1="1-3.jpg"
pp2="1-4.jpg"

#读取图片
img_0=cv2.imread(pp0,cv2.IMREAD_ANYCOLOR)
img_1=cv2.imread(pp1,cv2.IMREAD_ANYCOLOR)
img_2=cv2.imread(pp2,cv2.IMREAD_ANYCOLOR)

def progresss(img):
    img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    grayx=cv2.Sobel(img,ddepth=cv2.CV_32F,dx=1,dy=0,ksize=-1)
    grayy=cv2.Sobel(img,ddepth=cv2.CV_32F,dx=0,dy=1,ksize=-1)
    gradinet=cv2.subtract(grayx,grayy)
    gradinet=cv2.convertScaleAbs(gradinet)
    return gradinet


img_0_gray=progresss(img_0)
img_1_gray=progresss(img_1)
img_2_gray=progresss(img_2)
cv2.imshow('img_1_gray',img_1_gray)
cv2.imshow('img_2_gray',img_2_gray)
#图像相减
results_0_1=cv2.subtract(img_2_gray,img_1_gray)

results_0_1=cv2.subtract(results_0_1,img_1_gray)
#cv2.imshow('results_0_1',results_0_1)


# 中值滤波
img_median = cv2.medianBlur(results_0_1, 5)


cv2.imshow('img_median',img_median)
results_0_1=img_median

#形态学腐蚀
results_0_1 = cv2.erode(img_median, None, iterations=3)
#低通滤波
results_0_1 = cv2.blur(results_0_1, (5,5))
#形态学膨胀
results_0_1 = cv2.dilate(results_0_1, None, iterations=4)
#寻找轮廓图像
image,contours,hierarchy = cv2.findContours(results_0_1.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

print(len(contours))
print("###############")
#排除低面积的轮廓
contours2=[]
for contour in contours:
    area=cv2.contourArea(contour)
    print(area)
    if area>400.0:
        contours2.append(contour)
print("###############")
print(len(contours2))

#在图像中画出差异轮廓
cv2.drawContours(img_1,contours2,-1,(0,0,255),3)
cv2.drawContours(img_2,contours2,-1,(0,0,255),3)



#轮廓面积计算函数(所有)
def areaCal(contour):
    area = 0
    for i in range(len(contour)):
        area += cv2.contourArea(contour[i])
    return area
print(areaCal(contours))

cv2.imshow('img',img_1)
cv2.imshow('img2',img_2)
cv2.imshow('img_median',img_median)
cv2.waitKey()
cv2.destroyAllWindows()
