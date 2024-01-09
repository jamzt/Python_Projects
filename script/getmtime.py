import os
import datetime
import getmtime

fPath = '/Users/jamz/Documents/GitHub/Python_Projects/script'

for fName in os.listdir(fPath):
    if fName.endswith(".txt") and os.path.isfile(fPath):
        print("{fName}, Modified Time: {m_time}")
        mtime = getmtime(fPath)
        m_time = datetime(mtime).strftime('%Y-%m-%d %H:%M:%S')