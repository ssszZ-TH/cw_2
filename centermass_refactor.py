import numpy as np
import cv2 as cv
#import spa มานั่งทำ

def denoise_auto(noisy_image):
    try:
        return cv.cuda.fastNlMeansDenoising(noisy_image, None, 31, 7, 21)
    except:
        return cv.fastNlMeansDenoising(noisy_image, None, 31, 7, 21)
    
def get_tresh(img):
    blur = cv.GaussianBlur(img, (5, 5), cv.BORDER_DEFAULT)
    ret, thresh = cv.threshold(blur, 200, 255, cv.THRESH_BINARY_INV)
    return thresh

def get_contours(img_tresh):
    contours, hierarchies = cv.findContours(
    img_tresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    return contours

def get_outline(img_thresh,contours):
    outline = np.zeros(img_thresh.shape[:2],dtype='uint8')
    cv.drawContours(outline, contours, -1, (255, 0, 0), 1)
    return outline


if __name__=="__main__":
    image = cv.imread("./Circle_Objects.png",cv.IMREAD_GRAYSCALE)
    image = np.array(image, dtype="uint8")
    
    #ถ้าเอาไป denoise เเล้วมันจะ thresh hold ไม่ได้ 
    #image = denoise_auto(image)
    #cv.imwrite(filename="./removed_noise.png",img=image)
    
    image = get_tresh(image)
    cv.imwrite("./thresh.png",image)
    contours = get_contours(image)
    image_outline = get_outline(image,contours)
    cv.imwrite("./img_outline.png",image)
    
    for i in contours:
        M = cv.moments(i)
        if M['m00'] != 0:
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            #image_out = cv.drawContours(image, [i], -1, (0, 255, 0), 2)
            image_out = cv.circle(image, (cx, cy), 7, (0, 0, 255), -1)
            #image_out = cv.putText(image, "center", (cx - 20, cy - 20),
            #           cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        else:
            print("no m[m00]")
        print(f"x: {cx} y: {cy}")

    cv.imwrite("output.png",image_out)