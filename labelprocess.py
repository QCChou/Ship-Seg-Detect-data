import os
# 本脚本将原来的label文件里rotation坐标值读取出来，转换，写入。每一张图片为一个标注文件，每一行为一个物体。

# 1. 读旧的label文件，存入一个巨大的list中
with open('RotationRegionLabels.txt') as file:
    for line in file:
        # 2. 按空格split，并存入新的list    
        oldlist = line.split()
        # 3. 读 oldlist[1]，即物体的数量
        n = int(oldlist[1])
        first = 12
        # 4. 读坐标并存入新的list
        newline = []
        newline.append(oldlist[0])

        for i in range(n):
            ci = first + i * 15
            cj = ci
            for j in range(5):
                newline.append(oldlist[cj])
                cj += 1
        nfilename = newline[0][:-4]
        
        newline.pop(0)
        newline = list(map(eval, newline)) #把‘343.748’转成int为元素的列表

        newfile = open(os.path.join('./newlabel/'+nfilename+".txt"),"a")
        for num in range(len(newline)):
            newfile.write(str(newline[num]))
            if num % 5 == 4:
                newfile.write("\n")
            else:
                newfile.write(" ")
        
        newfile.close()





