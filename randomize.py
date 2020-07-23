import os
import shutil
import random
import numpy as np


dir = r'D:\PROJECTS\malaria\cell_images\Uninfected'
train_dir = r'D:\PROJECTS\malaria\cell_images\Train\Uninfected'
test_dir = r'D:\PROJECTS\malaria\cell_images\Test\Uninfected'
valid_dir = r'D:\PROJECTS\malaria\cell_images\Validation\Uninfected'



files = [file for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))]
train_count  = np.round(75/100*len(files))
test_count = np.round(23/100*len(files))
valid_count  = np.round(2/100*len(files))
rndnums = list(random.sample(range(0, len(files)), len(files)))
print("len(files)", len(files))

# print("all",len(files))
# print("train",np.round(train*len(files)))
# print("test",np.round(test*len(files)))
# print("valid",np.round(valid*len(files)))
#
# print("sum",np.round(train*len(files)) + np.round(test*len(files)) + np.round(valid*len(files)))

# Amount of random files you'd like to select

##train_files
print(rndnums)

train_file_index = rndnums[0:int(train_count)+1]
train_file_name = [files[i] for i in train_file_index]

test_file_index = rndnums[int(train_count)+1:int(train_count + test_count)+1]
test_file_name = [files[i] for i in test_file_index]

valid_file_index = rndnums[int(train_count + test_count)+1:]
valid_file_name = [files[i] for i in valid_file_index]



for x in train_file_name:
        file = x
        shutil.move(os.path.join(dir, file), os.path.join(train_dir, file))
##test_files
for y in test_file_name:
        file = y
        shutil.move(os.path.join(dir, file), os.path.join(test_dir, file))

##valid_files
for z in valid_file_name:
        file = z
        shutil.move(os.path.join(dir, file), os.path.join(valid_dir, file))