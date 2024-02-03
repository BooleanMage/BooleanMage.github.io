cd _shared
./upload.bat
cd ../

git config --local user.name "BooleanMage"
git config --local user.email "BooleanMage@users.noreply.github.com"
git remote set-url origin git@BM:BooleanMage/BooleanMage.github.io.git

git submodule update --recursive --remote

git pull
git add .
git commit -m "upload"
git push
