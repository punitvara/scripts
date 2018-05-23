'''
1. Find .c file under (test) directory
2. Search lines starting with zassert_
3. Find whether newline character is present at the end of line
4. If yes then remove it
5. No. Then line is split in multiple lines. Look for the line ending with ;
   and remove new line character if any.
'''

import re,os,shutil

def finddir():
    for path, dirs, files in os.walk('./tests/posix/pthread'):  
            for names in files:
                if names.endswith('.c'):
                    #for line in open(os.path.join(path, names), "rw"):
                    with open(os.path.join(path, names), 'r') as f:
                        lines = f.readlines()
                        f.close()
                        f = open(os.path.join(path, names), 'w')
                        flag = 0
                        for line in lines:
                            if (re.findall("zassert_", line) or (flag == 1)):
                                    flag =1
                                    xyz = re.search(r'\\n\"\)\;', line)
                                    if xyz:
                                        line = re.sub(r'\\n\"\)\;', r'");', line)
                                    if re.search(";", line):
                                        flag = 0
                            f.write(line)
                        f.close()

def main():
    print("Hellow wor")
    finddir()

if __name__ == "__main__":
        main()
