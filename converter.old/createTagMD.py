import os
import re

def get_filepaths(directory):
    file_paths = []

    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)

    return file_paths





if __name__ == '__main__':
    full_file_paths = get_filepaths(".")
        # tags = {tag:filepaths}
    tags = {}
    # get all tags 
    pattern = re.compile(r"\[\[(.*)\]\]")   
    for path in full_file_paths:
        if path.endswith(".md"):
            with open(path,"r",encoding="utf-8") as f:
                text = f.read()
                matchObj = pattern.findall(text)
                if len(matchObj)==0:
                    pass
                else:
                    for tag in matchObj:
                        try:
                            tags[tag].append(path)
                        except KeyError:
                            tags[tag] = []
                            tags[tag].append(path)

    # create ./_Tags/README.md
    try:
        os.mkdir("./_Tags")
    except:
        pass
    with open("./_Tags/README.md", "w", encoding="utf-8") as f:
        f.write("# _Tags\n")
        if '' in tags:
            tags.pop('')
        else:
            pass
            
        for tag in tags:
            f.write("* "+tag+"\n")
            for path in tags[tag]:
                pattern = re.compile(r"(.*[$\\])(.*)(.md)") 
                matchObj = re.match(pattern, path, flags=0)
                path = path[1:-3].replace(" ", "%20")
                path = path.replace("\\", "/")
                title = "["+matchObj.group(2)+"]"
                url = "\t* "+title+"(" + "/Knowledge" +path+")\n" 
                f.write(url)