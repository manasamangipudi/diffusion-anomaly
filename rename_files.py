import os
import nibabel as nib
import numpy as np
files_path = "BraTS2020_TrainingData"
#
# files = os.listdir(files_path)
# files.remove("000065")
# for each in files:
#     print(each)
#     channels = ["flair", "seg", "t1", "t1ce", "t2"]
#     index = 85
#     for every in channels :
#         old_file_name = os.path.join(files_path, each, "BraTS20_Training_" + each[3:] + "_" + every + ".nii")
#         print()
#         old_flair = nib.load(old_file_name).get_fdata()
#         old_flair = np.array(old_flair)[:,:, index]
#         new_file_name = "brats_train_" + each[3:] + "_" + every + "_" + f"{index:03}" +"_w.nii.gz"
#         ni_image = nib.Nifti1Image(old_flair, affine=np.eye(4))
#         nib.save(ni_image, os.path.join(files_path, each, new_file_name))
#         os.remove(old_file_name)

img = nib.load('data/brats/training/000004/brats_train_001_flair_083_w.nii.gz').get_fdata()
print(img.shape)

img = nib.load('data/brats/training/000004/brats_train_001_seg_083_w.nii.gz').get_fdata()
print(img.shape)

img = nib.load('data/brats/training/000004/brats_train_001_t1_083_w.nii.gz').get_fdata()
print(img.shape)

img = nib.load('data/brats/training/000004/brats_train_001_t1ce_083_w.nii.gz').get_fdata()
print(img.shape)
img = nib.load('data/brats/training/000004/brats_train_001_t2_083_w.nii.gz').get_fdata()
print(img.shape)