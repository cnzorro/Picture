#!/usr/bin/env python
# coding: utf-8

# In[20]:


# Importing Image module from PIL package 
from PIL import Image 
import os

# 初始化
path1='/test/BgColor'    #文件夹
path2='/test/Body'
path3='/test/Clothes'
path4='/test/Decorate'
path5='/test/Eye'
path6='/test/Face'
path7='/test/Hat'
path8='/test/Head'
path9='/test/Mouth'
path10='/test/Nose'
path11='D:/test/Finish'
path12='/test/temp'

img1=os.listdir(path1)  #文件夹path
img2=os.listdir(path2)
img3=os.listdir(path3)
img4=os.listdir(path4)
img5=os.listdir(path5)
img6=os.listdir(path6)
img7=os.listdir(path7)
img8=os.listdir(path8)
img9=os.listdir(path9)
img10=os.listdir(path10)
img11=os.listdir(path11)
img12=os.listdir(path12)

#列表初始化
list_p=[] 
list_f=[]

#将文件夹及path分别初始化，排除空文件夹
if img1:
    list_f.append(img1)
    list_p.append(path1)
if img2:
    list_f.append(img2)
    list_p.append(path2)
if img3:
    list_f.append(img3)
    list_p.append(path3)
if img4:
    list_f.append(img4)
    list_p.append(path4)
if img5:
    list_f.append(img5)
    list_p.append(path5)
if img6:
    list_f.append(img6)
    list_p.append(path6)
if img7:
    list_f.append(img7)
    list_p.append(path7)
if img8:
    list_f.append(img8)
    list_p.append(path8)
if img9:
    list_f.append(img9)
    list_p.append(path9)
if img10:
    list_f.append(img10)
    list_p.append(path10)

#合并图片函数
def combine(fig1,fig2,road1,road2):
    i=0
    for fi1 in fig1:
        for fi2 in fig2:        
            i=i+1
            a=str(i)
            im=Image.open(road1+"/"+fi1)
            ig=Image.open(road2+"/"+fi2)
            im.paste(ig,(0,0),ig)
            im.save(path11+"/"+a+".png")
    return 

#拷贝文件函数
def copyfile(file,path): 
    i=0
    for imf in file:
        i=i+1
        a=str(i)
        im=Image.open(path+"/"+imf)
        im.save(path12+"/"+a+".png")
    return

print("开始")  

if len(list_f)<2:
    print("文件为空！ 停止执行！")
else:
    #先将第一个图片组拷贝至临时文件夹temp
    copyfile(list_f[0],list_p[0])
    img11=os.listdir(path11)  #更新文件夹列表
    img12=os.listdir(path12)  #更新文件夹列表    
    #删除已处理完成的第一个图片组
    del list_f[0]
    del list_p[0]
    
    for j in range(len(list_f)):
        combine(img12,list_f[j],path12,list_p[j])  
        img11=os.listdir(path11)  #gen新文件夹列表
        img12=os.listdir(path12)  #跟新文件夹列表
        copyfile(img11,path11)    #将文件拷贝至temp文件夹
        img11=os.listdir(path11)  #跟新文件夹列表
        img12=os.listdir(path12)  #跟新文件夹列表
        print(int(((j+1)/(len(list_f)))*100),'%', end='   ')
            
print("OK")


# In[ ]:





# In[ ]:





# In[ ]:




