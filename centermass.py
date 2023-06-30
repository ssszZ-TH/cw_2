import cv2 as cv
import numpy as np
#import ssszZ มาช่วยสปาเก็ตตี้ทำ

# change it with your absolute path for the image
image = cv.imread("./input_img.png")
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

blur = cv.GaussianBlur(gray, (5, 5),
					cv.BORDER_DEFAULT)
ret, thresh = cv.threshold(blur, 200, 255,
						cv.THRESH_BINARY_INV)

cv.imwrite("test_step1_thresh.png",thresh)

contours, hierarchies = cv.findContours(
	thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

blank = np.zeros(thresh.shape[:2],
				dtype='uint8')

cv.drawContours(blank, contours, -1,
				(255, 0, 0), 1)

cv.imwrite("test_step2_contours.png", blank)



#blank เป็นตัว check เขียนค่าออกไปที่ blankoutput
blank_output=blank
img_h,img_w = blank.shape
for y in range(0,img_h):
    for x in range(0,img_w):
        
        if (blank[y,x] > 200):
            # print("เจอสีขาว ที่ xy",x,y)
            #blank_output = cv.circle(blank_output, (x,y), 56, 100, 1) #radian color bold
            ## เเต่ผมต้องการใช้ของตัวเอง
            r = 3
            h = x
            k = y
            sampling_line=500

            for y in range(y-r,y+r):
                for x in range(x-r,x+r):
                    if (x-h)**2 + (y-k)**2 > (r**2) and (x-h)**2 + (y-k)**2 < (r**2)+sampling_line:
                        
                        #หลุดกรอบก็ให้ข้าม
                        if x<0 or y<0 or y>=594 or x>475:
                            print("skip",x,y)
                            continue
                        
                        print("draw at xy=",x,y)
                        blank_output[x,y]=128
            

cv.imwrite("test_step3_display_center.png",blank_output)