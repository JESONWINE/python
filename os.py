# coding=utf-8
'''
按照文件的时间顺序建立文件夹分类
'''
import os
import time
from win32com.propsys import propsys, pscon
import shutil
date_list=[]
root_dir='F:\Photo'
def mkdir(path):
    path=path.strip()
    path=path.rstrip("\\")
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print path+'create succ'
        return True
    else:
        print path+'is exit'
        return False


for root, dirs, files in os.walk("C:\Users\Jason\Desktop\TESTT", topdown=False):
    for name in files:
#获取文件创建的时间
        name1=os.path.join(root, name)
        time1=os.path.getctime(name1)
        create_date=time.strftime("%Y%m%d_%H%M%S", time.localtime(time1))
#媒体创建时间
        properties = propsys.SHGetPropertyStoreFromParsingName(name1)
        media_date1 = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
#若无媒体创建时间，则以文件创建时间稳准
        if media_date1 == None:
            date_time=create_date
        else:
            media_date3 = time.strptime(str(media_date1),"%m/%d/%y %H:%M:%S")
            media_date = time.strftime("%Y%m%d_%H%M%S", media_date3)
            date_time=media_date
#创建文件夹并复制文件
        date_dir=time.strftime("%Y%m",time.strptime(date_time,"%Y%m%d_%H%M%S"))
        date_dir=root_dir + '\\' + date_dir[0:4] + '\\' + date_dir
        
        if not (date_dir in date_list) :
            mkdir(date_dir)
            date_list.append(date_dir)
        name2=date_dir+'\\'+date_time+'_'+name
        shutil.copy(name1,name2)

print("task succ")


