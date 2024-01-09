import os

fName = 'file1.txt'

fPath = '/Users/jamz/Documents/GitHub/Python_Projects/script'

abPath = os.path.join(fPath, fName)
print(abPath) 

import datetime

for fName in os.listdir(fPath):
        if fName.endswith(".txt") and os.path.isfile(fPath):
            mtime = getmtime(fPath)
            
            m_time = datetime(mtime).strftime('%Y-%m-%d %H:%M:%S')
        
            print("{fName}, Modified Time: {m_time}")