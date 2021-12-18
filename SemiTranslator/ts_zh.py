from translatepy.translators.google import GoogleTranslate
from pprint import pprint
import os
from os import path
import glob, os
import sys
try:
    from os import scandir
except ImportError:
    from scandir import scandir

# DEFAULT PATHS/VARS TO BE USED
gtranslate = GoogleTranslate()
count = 0





# PROMPT FOR GENERATION
print('>>> Umm uh..')    
print('> Executing main process...')

# FIND ALL DIRECTORIES IN THE DEFAULT PATH
# CHEERS TO https://stackoverflow.com/users/68707/ben-hoyt FOR THIS GLORIOUS CODE SNIPPET
def scantree(path):
    """Recursively yield DirEntry objects for given directory."""
    for entry in scandir(path):
        if not entry.name.startswith('.') and entry.is_dir(follow_symlinks=False):
            yield from scantree(entry.path)  # see below for Python 2.x
        else:
            yield entry

if __name__ == '__main__':
    for entry in scantree(sys.argv[1] if len(sys.argv) > 1 else '.'):

        # PRINT ALL THE INI FILES AND COUNT THEM
        if entry.is_file() and entry.name.endswith('.ini'):

            count = count + 1      
            print(count, entry.path)
            # WRITE THE TS IN OUTPUT
            with open(entry.path, encoding="utf8") as file:

                for line in file:
                    DT = "DisplayText:"
                    DDs = "DisplayDescription:"  
                    CUT = line
                    if "displayText:" in line:
                        p = gtranslate.translate(CUT, "Chinese")
                        fs = open('./tst/tst.zh.txt',"a+",encoding="utf-8")
                        tx = f'{p.result} \n'.replace(DT, 'displayText_zh:').replace('\ N', '\n').replace('\ n', '\\n')
                        fs.write(tx)
                        fs.close()
                    if "displayDescription:" in line:
                        p = gtranslate.translate(CUT, "Chinese")
                        fs = open('./tst/tst.zh.txt',"a+",encoding="utf-8")
                        tx = f'{p.result} \n'.replace(DDs, 'displayDescription_zh:').replace('\ N', '\\n').replace('\ n', '\\n')
                        fs.write(tx)
                        fs.close()
                        



                
                
