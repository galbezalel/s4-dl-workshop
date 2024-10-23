import json
import os
import sys
import tempfile
import zipfile

from huggingface_hub import hf_hub_download

def read_dataset_args(key):
    with open("datasets.json", "r") as fp:
        ds_map: dict = json.load(fp)
    return ds_map.get(key)

def create_output_dir():
    # Create an output directory
    output_dir = '../data/'
    os.makedirs(output_dir, exist_ok=True)
    return output_dir

def download_dataset_from_hf(dst: tempfile.TemporaryDirectory, repo_id: str, filename: str) -> None:
    if "HF_TOKEN" not in os.environ:
        raise EnvironmentError("No huggingface token was set, please run set_hf_token.sh before downloading datasets")
    hf_hub_download(repo_id=repo_id, filename=filename, repo_type="dataset", local_dir=dst)

def unarchive_zip(src: tempfile.TemporaryDirectory, dst: str, dst_file: str):
    with zipfile.ZipFile(os.path.join(src, dst_file), 'r') as zip_ref:
        zip_ref.extractall(dst)
    
def main() -> None:
    out_dir = create_output_dir()
    ds_attr = read_dataset_args(sys.argv[1])
    with tempfile.TemporaryDirectory() as tmp:
        download_dataset_from_hf(tmp, ds_attr["repo_id"], ds_attr["file_path"])
        unarchive_zip(tmp, out_dir, ds_attr["file_path"])

if __name__ == "__main__":
    main()