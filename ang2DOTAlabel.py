import os
import sys
import math
import glob
origin_ann_dir = 'newlabel'  
new_ann_dir = 'labeltxt'
pi=3.141592


# 遍历原txt每一个文件

txtfiles= os.listdir(origin_ann_dir) #得到文件夹下的所有文件名称
s = []
for file in txtfiles: #遍历文件夹
     if not os.path.isdir(file): #判断是否是文件夹，不是文件夹才打开
        f = open(origin_ann_dir+"/"+file) #打开文件
        iter_f = iter(f) #创建迭代器
        #在new_ann_dir新建一个同名txt文件
        new_ann_file = open(os.path.join(new_ann_dir+"/"+file),"a")

        for line in iter_f: #遍历文件，一行行遍历，读取文本
            #split line which is a str
            oldlist = line.split()
            # convert elements from str type to float
            oldlist = list(map(eval, oldlist)) #把‘343.748’转成int为元素的列表
            # 每一行计算坐标值，写入对应txt新label中
            cx = oldlist[0]
            cy = oldlist[1]
            width = oldlist[2]
            height = oldlist[3]
            angle = 0- oldlist[4]

            # 舰艏艉
            bow_x=cx+width/2*math.cos(angle)
            bow_y=cy+width/2*math.sin(angle)
            tail_x=cx-width/2*math.cos(angle)
            tail_y=cy-width/2*math.sin(angle)

            bowA_x=round(bow_x+height/2*math.sin(angle))
            bowA_y=round(bow_y-height/2*math.cos(angle))
 
            bowB_x=round(bow_x-height/2*math.sin(angle))
            bowB_y=round(bow_y+height/2*math.cos(angle))
 
 
            tailB_x=round(tail_x+height/2*math.sin(angle))
            tailB_y=round(tail_y-height/2*math.cos(angle))
 
            tailA_x=round(tail_x-height/2*math.sin(angle))
            tailA_y=round(tail_y+height/2*math.cos(angle))

            #写入新txt这一行
            newline = [bowA_x, bowA_y, bowB_x,bowB_y, tailA_x, tailA_y, tailB_x, tailB_y]

            for num in range(len(newline)):
                new_ann_file.write(str(newline[num]))
                if num % 7 == 0 and num != 0:
                    new_ann_file.write("\n")
                else:
                    new_ann_file.write(" ")
        
        #关闭新文件
        new_ann_file.close()








        
        


# 
