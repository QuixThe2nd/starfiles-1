

rm -r dist
mkdir dist
python3 setup.py sdist bdist_wheel
git add .
git commit -m "Added FileIO + FilePipe"
git push
echo "Pass: Sokgez-tanci9-qotsez"
# twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*