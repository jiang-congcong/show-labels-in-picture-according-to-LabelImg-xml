#coding=utf-8
import xml.dom.minidom
import cv2
import os

path_xml = "D://1//xml"#windows系统用双斜线
filelist = os.listdir(path_xml)
path = "D://1//"

for files in filelist:
    filename = os.path.splitext(files)[0]  # 读取文件名
    #print(i)
    path1 = path+"xml//"+filename+".xml" #读取所有xml文件
    path2 = path+"img//"+filename+".jpg" #读取所有图片文件
    print(path1)
    dom = xml.dom.minidom.parse(path1)
    root = dom.documentElement

    xleft = dom.getElementsByTagName('xmin')
    xright = dom.getElementsByTagName('xmax')
    ytop = dom.getElementsByTagName('ymin')
    ybutton = dom.getElementsByTagName('ymax')
    len1 = len(xleft)#计算所有label的个数

    img = cv2.imread(path2)

    for i in range(len1):
        x_left = xleft[i].firstChild.data
        x_right = xright[i].firstChild.data
        y_top = ytop[i].firstChild.data
        y_button = ybutton[i].firstChild.data
        #print(x_left, y_top, x_right, y_button)
        cv2.rectangle(img, (int(x_left), int(y_top)), (int(x_right), int(y_button)), (0, 255, 0), 3)  #依次将label画到图片上

    path3 = path + "img_1//"+filename +"_1.jpg" #存图片的文件路径

    cv2.imwrite(path3, img)
    #cv2.imshow("251", img)
    cv2.waitKey(0)