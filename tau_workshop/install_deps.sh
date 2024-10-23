# /bin/bash

echo "Installing dependencies";
cd ../
pip install -r requirements.txt;
pip install pykeops cmake;
cd ./extensions/kernels;
python setup.py install;