# This py file is used to make a classification for mimic data according to the table.

import pandas as pd
import  numpy as np
from constants import *
from utils import extract_mimic_text

extract_text = False

np.random.seed(2025)

def main():
    if extract_text:
        extract_mimic_text()
    metadata_df = pd.read_csv(mimic_cxr_meta_csv)
    metadata_df = metadata_df[["dicom_id", "subject_id",
                               "study_id", "ViewPosition"]].astype(str)
    metadata_df["study_id"] = metadata_df["study_id"].apply(lambda x: "s"+x)
    # Only keep frontal images
    metadata_df = metadata_df[metadata_df["ViewPosition"].isin(["PA", "AP"])]

    text_df = pd.read_csv(mimic_cxr_text_csv)
    text_df.dropna(subset=["impression", "findings"], how="all", inplace=True)
    text_df = text_df[["study", "impression", "findings"]]
    text_df.rename(columns={"study": "study_id"}, inplace=True)

    split_df = pd.read_csv(mimic_cxr_split_csv)
    split_df = split_df.astype(str)
    split_df["study_id"] = split_df["study_id"].apply(lambda x: "s"+x)
    # TODO: merge validate and test into test.
    split_df["split"] = split_df["split"].apply(
        lambda x: "valid" if x == "validate" or x == "test" else x)

    chexpert_df = pd.read_csv(mimic_cxr_chexpert_csv)
    chexpert_df[["subject_id", "study_id"]] = chexpert_df[[
        "subject_id", "study_id"]].astype(str)
    chexpert_df["study_id"] = chexpert_df["study_id"].apply(lambda x: "s"+x)

    master_df = pd.merge(metadata_df, text_df, on="study_id", how="left")
    master_df = pd.merge(master_df, split_df, on=["dicom_id", "subject_id", "study_id"], how="inner")
    master_df.dropna(subset=["impression", "findings"], how="all", inplace=True)
    
    n = len(master_df)
    master_data = master_df.values

    root_dir = str(mimic_cxr_data_dir).split("/")[-1] + "/files"
    path_list = []
    for i in range(n):
        row = master_data[i]
        file_path = "%s/p%s/p%s/%s/%s.jpg" % (root_dir, str(
            row[1])[:2], str(row[1]), str(row[2]), str(row[0]))
        path_list.append(file_path)
        
    master_df.insert(loc=0, column="Path", value=path_list)

    # Create labeled data df
    labeled_data_df = pd.merge(master_df, chexpert_df, on=[
                               "subject_id", "study_id"], how="inner")
    labeled_data_df.drop(["dicom_id", "subject_id", "study_id",
                          "impression", "findings"], axis=1, inplace=True)

    train_df = labeled_data_df.loc[labeled_data_df["split"] == "train"]
    train_df.to_csv(mimic_cxr_train_csv, index=False)
    test_df = labeled_data_df.loc[labeled_data_df["split"] == "valid"]
    test_df.to_csv(mimic_cxr_test_csv, index=False)
    # test_df = labeled_data_df.loc[labeled_data_df["split"] == "test"]
    # test_df.to_csv(mimic_cxr_test_csv, index=False)

    # master_df.drop(["dicom_id", "subject_id", "study_id"],
    #                axis=1, inplace=True)

    # Fill nan in text
    master_df[["impression"]] = master_df[["impression"]].fillna(" ")
    master_df[["findings"]] = master_df[["findings"]].fillna(" ")
    master_df.to_csv(mimic_cxr_master_csv, index=False)

if __name__ == "__main__":
    main()