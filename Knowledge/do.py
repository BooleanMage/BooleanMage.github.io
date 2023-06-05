import os
import re

def parse_files(folder_path, pattern, replacement):
    for root, dirs, files in os.walk(folder_path):
        # Exclude the ".git" folder from processing
        if ".git" in dirs:
            dirs.remove(".git")
        
        for file_name in files:
            # Skip files that don't have the ".md" extension
            if not file_name.endswith('.md'):
                continue
            
            file_path = os.path.join(root, file_name)
            
            # Skip files within the ".git" folder
            if ".git" in file_path.split(os.sep):
                continue
            
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            updated_content = re.sub(pattern, replacement, content)
            
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(updated_content)
            
            print(f"Processed: {file_path}")

# Set the default processing folder as the current directory
folder_path = './'

# Specify the pattern to match
pattern = r'- \[\[\]\]'

# Specify the replacement string
replacement = ''

# Call the function to perform the parsing
parse_files(folder_path, pattern, replacement)