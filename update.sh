

rm -r dist
mkdir dist
python3 setup.py sdist bdist_wheel
git add .
git commit -m "fixed"
git push
echo "Pass: gomkom-refmE2-mafqex"
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*