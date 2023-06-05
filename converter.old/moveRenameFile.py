import os
import re
import shutil

def get_filepaths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  

    return file_paths 


if __name__ == '__main__':
    full_file_paths = get_filepaths(".")
    pattern = r"(^.*\\)(.*)\.md"

    for f in full_file_paths:
        if f.endswith(".md"):
            matchObj = re.match(pattern, f, flags=0)
            if matchObj:
                try:
                    os.mkdir(matchObj.group(1)+matchObj.group(2))
                except:
                    pass
                os.rename(f, matchObj.group(1)+matchObj.group(2)+"\README.md")
            else:
                pass
    os.rename("./_Tags/README/README.md", "./_Tags/README.md")
    shutil.rmtree("./_Tags/README")
    # os.remove("./_Tags/README")