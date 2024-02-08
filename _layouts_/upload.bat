git config --local user.name "LatticeMage"
git config --local user.email "LatticeMage@gmail.com"
git remote set-url origin git@LM:LatticeMage/latticemage_layouts.git

git pull
git add .
git commit -m "upload"
git push
