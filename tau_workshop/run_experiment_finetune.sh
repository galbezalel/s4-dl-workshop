# /bin/bash

./install_deps.sh;

echo "Extracting dataset";
python download_dataset.py youtubemix;

echo "Fine tuning from v4 checkpoint of original YouTubeMix experiment";
cd ../;
python -m train wandb=null experiment=audio/sashimi-youtubemix train.ckpt=checkpoints/sashimi_youtubemix_v4.pt;