# from huggingface_hub import snapshot_download
# from huggingface_hub import login

# login(token="hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

# snapshot_download(
#     repo_id="liuhaotian/LLaVA-CC3M-Pretrain-595K",
#     local_dir="/content/drive/MyDrive/LLaVA-CC3M-Pretrain-595K",
#     local_dir_use_symlinks=False 
# )

# from datasets import load_dataset
# ds = load_dataset("liuhaotian/LLaVA-CC3M-Pretrain-595K")

# wget -O /content/drive/MyDrive/LLaVA-CC3M-Pretrain-595K_images.zip <images_zip_download_URL>

from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="liuhaotian/LLaVA-CC3M-Pretrain-595K",
    repo_type="dataset",
    local_dir="/content/drive/MyDrive/",
    local_dir_use_symlinks=False
)