import os
import time
from win32com.propsys import propsys, pscon

for root, dirs, files in os.walk("G:\PYTHON", topdown=False):
    
    for name in files:
        name1=os.path.join(root, name)
        time1=os.path.getmtime(name1)
        properties = propsys.SHGetPropertyStoreFromParsingName(name1)
        media_date1 = properties.GetValue(pscon.PKEY_Media_DateEncoded).GetValue()
        print media_date1

'''
    print("test1")
    print(files)
    for name in dirs:
        print(os.path.join(root, name))
    print("test2")
    print(dirs)
'''