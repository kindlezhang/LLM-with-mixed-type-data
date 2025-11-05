import os
from pathlib import Path

# get data directory path
data_base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../data")

data_base_dir = Path(data_base_dir)

# ##################################
# MIMIC-CXR-JPG constants
# ##################################

mimic_cxr_data_dir = data_base_dir / "raw/physionet.org/files/mimic-cxr-jpg/2.1.0"
# mimic_cxr_train_txt = mimic_cxr_data_dir / "train.txt"
# mimic_cxr_valid_txt = mimic_cxr_data_dir / "valid.txt"
mimic_cxr_chexpert_csv = mimic_cxr_data_dir / "mimic-cxr-2.1.0-chexpert.csv"
mimic_cxr_meta_csv = mimic_cxr_data_dir / "mimic-cxr-2.1.0-metadata.csv"
mimic_cxr_text_csv = mimic_cxr_data_dir / "mimic_cxr_sectioned.csv"
mimic_cxr_split_csv = mimic_cxr_data_dir / "mimic-cxr-2.1.0-split.csv"

# Created csv
mimic_cxr_train_csv = mimic_cxr_data_dir / "train.csv"
mimic_cxr_valid_csv = mimic_cxr_data_dir / "valid.csv"
mimic_cxr_test_csv =  mimic_cxr_data_dir / "test.csv"

