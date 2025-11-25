
from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="liuhaotian/LLaVA-CC3M-Pretrain-595K",
    repo_type="dataset",
    local_dir="/content/drive/MyDrive/LLaVA-CC3M-Pretrain-595K",
    local_dir_use_symlinks=False
)

# unzip -q images.zip -d images/