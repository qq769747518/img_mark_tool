# import os
# # # fall-15-cam1-d
# # # video_25
# img_list =os.listdir('./video_25')
# img_name_1=img_list[0]
# img_name_len=len(img_name_1)
# for i in img_list[1:]:
#     if len(i)==img_name_len:
#         img_name_2=i
#         break
# print(img_name_1)
# img_name_1=img_name_1.split('.')[0]
# img_name_2=img_name_2.split('.')[0]
# print(img_name_2,img_name_1)
# same_part=''
# same_part_list=[]
# for index,i in enumerate(img_name_1):
#     if i==img_name_2[index]:
#         same_part+=i
#     if i!=img_name_2[index]:
#         same_part_list.append(same_part)
#         same_part=''
# same_part_list.append(same_part)
# for i in same_part_list:
#     if i != '' and not i.isdigit():
#         flag=i.strip('[0123456789]')
#         break
#
# a=img_name_1.split(flag)
# if a[0]!='':
#     j=0
# else:
#     j=1
#
#
# print(img_list)
# for index, i in enumerate(img_list):
#     img_name=i.split('.')[0]
#     img_list[index] = (i, eval(img_name.split(flag)[j].lstrip('[0]')))
#
# img_list.sort(key=lambda x: x[1])
# import numpy as np
# import cv2 as cv
# img = np.zeros((360,640), dtype=np.uint8)
#
# img = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
# cv.putText(img, "Please select the images to be marked", (2, 175), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 255,255),2)
#
# ret, jpeg = cv.imencode('.jpg', img)
# frame = jpeg.tobytes()
#
# with open('./default.jpg','wb') as f:
#     f.write(frame)



# def a(a):
#     cc=20
#     def b():
#         a()
#         print(cc)
#         return 12
#     return b
#
# @a
# def ss():
#     print(111)
#
# a=ss()
# print(a)

def test():
    msg2 = 'test中的'
    print('====',msg1) # ==== 非test中的
msg1 = '非test中的'
test()
print(msg1) # 非test中的
# print(msg2) # 报错
