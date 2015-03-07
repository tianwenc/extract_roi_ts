# extract voxelwise timeseries from the specified ROI and images

import os
import numpy as np
import nibabel as nib

subject_list = '/mnt/mabloo1/apricot1_share6/network_interaction/network_nonstationary/group_78subjects/subjects/hcp_78subjects.txt'
roi_file = '/mnt/mandarin2/Public_Data/Parcellation_Insula/rsfMRI/Local_Data/ROIs/rInsula_AAL.nii'
data_dir = '/mnt/mandarin1/Public_Data/HCP/data_test_validate'
sub_dir = 'MNINonLinear/Results/rfMRI_REST1_LR'
img_name = 'msrfMRI_REST1_LR'
result_dir = '/fs/apricot1_share6/parcellation/data/rInsula_AAL/hcp_78subjects'
result_prefix = 'rInsula_AAL'

with open(subject_list) as f:
    subjects = f.readline().split('\r')

num_subj = len(subjects)

if not os.path.exists(result_dir):
    os.makedirs(result_dir)

roi_img = nib.load(roi_file)
roi_d = roi_img.get_data()
vox_idx = roi_d != 0

for subj in subjects:
    subj_data_dir = os.path.join(data_dir, subj, sub_dir)
    zip_file = os.path.join(subj_data_dir, ''.join([img_name, '*.gz']))
    if os.path.isfile(zip_file):
        os.system(''.join(['gunzip -fq ', zip_file]))
    subj_img_file = os.path.join(data_dir, subj, sub_dir, img_name+'.nii')
    subj_img = nib.load(subj_img_file)
    subj_d = subj_img.get_data()
    roi_ts = subj_d[vox_idx,:]
    roi_ts_file = os.path.join(result_dir, result_prefix+'_'+img_name+'_'+subj+'.txt')
    np.savetxt(roi_ts_file, roi_ts)
    

        
     