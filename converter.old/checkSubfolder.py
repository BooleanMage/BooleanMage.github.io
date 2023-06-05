import os
import re
def check_subfolder(directory):
    file_paths = []
    pattern = "./.git"
    for root, directories, files in os.walk(directory):
        if(re.match(pattern,root)!=None) :
            continue
        if(len(directories)==0):
            continue
        
        readmePath = os.path.join(root, "README.md")
        if(os.path.exists(readmePath)):
            # print(root+" contain README.md")
            with open(readmePath, "a",encoding="utf-8") as f:
                for dir in directories:
                    f.write("\n")
                    f.write("["+dir+"](./"+dir+"/)  ")
        else:
            header = root.split(os.path.dirname(root))[1][1:]
            with open(readmePath, "w",encoding="utf-8") as f:
                f.write("# "+header)
                f.write("\n")
                for dir in directories:
                    f.write("\n")
                    f.write("["+dir+"](./"+dir+"/)  ")

if __name__ == '__main__':
    check_subfolder("./")