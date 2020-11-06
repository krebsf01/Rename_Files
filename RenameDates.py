# Rename Dates

import re, os, shutil
from pathlib import Path


dataPattern = re.compile('''
^(.*?)
((0|1)?\d)           #MM
(\.|-)               #sep
((0|1|2|3)?\d)       #DD
(\.|-)               #sep
((19|20)\d{2})       #YYYY
(.*?)$
''', re.VERBOSE)

p = Path('C:/Users/thikr/OneDrive/Documentos')
All = os.listdir(p)

for fileName in All:
    if os.path.isfile(Path(p/fileName)):
        americanDate = dataPattern.search(fileName)
        if not americanDate == None:
            Start = americanDate.group(1)
            MM = americanDate.group(2) 
            DD = americanDate.group(5) 
            YYYY = americanDate.group(8)
            End = americanDate.group(10)
            shutil.move(Path(p/fileName), Path(p / f'{Start}{DD}.{MM}.{YYYY}{End}'))
    
