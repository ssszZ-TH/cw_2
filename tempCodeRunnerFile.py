for y in range(0,blank.shape[0]):
#     for x in range(0,blank.shape[1]):
        
#         if (blank[y,x] > 200):
#             # print("เจอสีขาว ที่ xy",x,y)
#             #blank_output = cv.circle(blank_output, (x,y), 56, 100, 1) #radian color bold
#             ## เเต่ผมต้องการใช้ของตัวเอง
#             r = 50
#             h = x
#             k = y
#             sampling_line=500

#             for y in range(y-r,y+r):
#                 for x in range(x-r,x+r):
#                     if (x-h)**2 + (y-k)**2 > (r**2) and (x-h)**2 + (y-k)**2 < (r**2)+sampling_line:
                        
#                         #หลุดกรอบก็ให้ข้าม
#                         if x<0 or y<0 or y>=594 or x>475:
#                             print("skip",x,y)
#                             continue
                        
#                         print("draw at xy=",x,y)
#                         blank_output[x,y]=128
            

# cv.imwrite("test_step3_display_center.png",blank_output)