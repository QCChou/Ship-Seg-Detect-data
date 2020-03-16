import cv2
import numpy as np
import os
 
img_folder = 'img/' # 文件夹末尾一定要加斜杠/！！！！
label_folder = 'labelTxt/'
 
gt_dst_folder = 'img_gt/'
 
# 从img_folder遍历每一张图的名字，得到img_names
img_names = []
for dirname, subdirs, files in os.walk(img_folder):
    pass
for img_name in files:
    img_names.append(img_name[:5])
# print(img_names)
 
 
for img_name in img_names:
    img = cv2.imread(img_folder + img_name +'.png')
    # 从label_folder打开对应label文件
    label_file = open(os.path.join(label_folder, img_name)+'.txt','r')
    #解析内容
    lines = []
    for line in label_file.readlines()[0:]:
        lines.append(line)
    # print(lines)
    for each in lines:
        elements = each.split()
        coordinates = elements[0:8]            
        coordinates = list(map(int, coordinates))
        # print(coordinates)
        x0 = coordinates[0]
        y0 = coordinates[1]
        x1 = coordinates[2]
        y1 = coordinates[3]
        x2 = coordinates[4]
        y2 = coordinates[5]
        x3 = coordinates[6]
        y3 = coordinates[7]
        pts = np.array([[x0, y0], [x1, y1], [x2,y2], [x3,y3]])
        # pts = np.array([[867, 60], [898, 63], [870, 326],  [839, 323]])
        # print(type(x0))
        # print(pts)
        #画四边形
        img_gt = cv2.polylines(img, [pts], True, (255, 255, 0), 2)
 
        # cv2.imshow('Image', img_gt)
        # cv2.waitKey(1000)
        # cv2.destroyAllWindows()
    # # #保存
    cv2.imwrite(gt_dst_folder + img_name+'.png', img_gt)