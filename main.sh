
#Automate publish

pip install twine
clear
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository pypi dist/*