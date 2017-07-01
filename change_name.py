#!/usr/bin/env python
# filename；mkdir.py

import os, re

filenames = os.listdir('D:\\shibingtuji')
for filename in filenames:
    num = re.findall('[(\d*?)]', filename);
    new_name = ''.join(num) + '_shibingtuji.rmvb'
    os.rename(filename, new_name)