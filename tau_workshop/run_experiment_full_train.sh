# /bin/bash

./install_deps.sh;

echo "Extracting dataset";
python download_dataset.py youtubebigband;

echo "Running complete training";
cd ../../;
python -m train wandb=null experiment=audio/sashimi-youtubemix dataset=youtube_bigband
