rmdir -R Knowledge -force

Remove-Item -Path "./Knowledge.md"

New-Item -ItemType Directory -Force -Path ./Knowledge # directory must exist
Copy-Item ../Knowledge/* ./Knowledge -Exclude @(".git",".vs",".obsidian") -Recurse
