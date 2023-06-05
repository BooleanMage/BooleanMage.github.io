git config --local user.name "BooleanMage"
git config --local user.email "BooleanMage@users.noreply.github.com"
git remote set-url origin git@AAL:BooleanMage/BooleanMage.github.io.git

git pull

./Knowledge.ps1
./Lecture.ps1

python ./page.py


git add .
git commit -m "upload"
git push