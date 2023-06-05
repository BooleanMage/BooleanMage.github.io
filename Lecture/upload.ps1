git config --local user.name "LatticeMage"
git config --local user.email "LatticeMage@users.noreply.github.com"
git remote set-url origin git@LM:LatticeMage/Lecture.git

git pull
git add .
git commit -m "upload"
git push


cd ../LatticeMage.github.io/
./upload.ps1
cd ../Lecture