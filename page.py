import os
import glob

folders = ["./Knowledge", "./Lecture"]

def write_md_file(folder_path):
    with open(f"{folder_path}.md", 'w', encoding='utf8') as f:
        for filename in glob.glob(f"{folder_path}/*"):
            # skip the .md file we're currently writing
            if filename == f"{folder_path}":
                continue

            # extract just the name of the file/folder, without the preceding path
            basename = os.path.basename(filename)

            # check if this is a directory
            if os.path.isdir(filename):
                f.write(f'[{basename}](./{basename})  \n')  # add .md to link
                # Recursively process the subdirectory
                write_md_file(filename)
            else:
                # split the extension from the filename
                name, ext = os.path.splitext(basename)
                if ext == '.md':
                    f.write(f'[{name}](./{name})  \n')

for folder in folders:
    write_md_file(folder)

files_to_update = []
for folder in folders:
    for filename in glob.glob(f"{folder}/**/*.md", recursive=True):
        files_to_update.append(filename)
files_to_update.extend(["./Knowledge.md", "./Lecture.md"])

for filename in files_to_update:
    with open(filename, 'r+', encoding='utf8') as f:
        content = f.read()

        # Get the file name and remove the .md extension for the title
        title = os.path.basename(filename).replace('.md', '')

        # Check if front matter already exists at the start of the file
        if not content.startswith('---'):
            front_matter = f'---\nlayout: default\ntitle: {title}\n---\n\n'
            content = front_matter + content
        else:  # front matter already exists, just need to add/replace title
            lines = content.split('\n')
            title_line_index = next((i for i, line in enumerate(lines) if line.startswith('title:')), None)
            new_title_line = f'title: {title}'

            if title_line_index is not None:
                # replace the existing title line
                lines[title_line_index] = new_title_line
            else:
                # insert a new title line
                lines.insert(2, new_title_line)  # insert title line after 'layout: default'

            content = '\n'.join(lines)

        f.seek(0)  # go back to the start of the file
        f.write(content)
        f.truncate()  # remove any remaining old content after the new content
