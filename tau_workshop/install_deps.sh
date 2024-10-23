# /bin/bash

echo "Installing dependencies";
cd ../;
pip install -r requirements.txt;
pip install pykeops cmake;

# On Google Colab, pykeops works faster than the custom compiled kernel.
# Otherwise - uncomment the following commands:
# cd ./extensions/kernels;
# python setup.py install;