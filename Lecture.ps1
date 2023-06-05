rmdir -R Lecture -force
Remove-Item -Path "./Lecture_folder.md"

New-Item -ItemType Directory -Force -Path ./Lecture # directory must exist
Copy-Item ../Lecture/* ./Lecture -Exclude @(".git",".vs",".obsidian") -Recurse

Remove-Item -Path "./Lecture/README.md"