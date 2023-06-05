rmdir -R Lecture -force

New-Item -ItemType Directory -Force -Path ./Lecture # directory must exist
Copy-Item ../Lecture/* ./Lecture -Exclude @(".git",".vs",".obsidian") -Recurse