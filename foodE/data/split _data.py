import os
import shutil


path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
parent_path = f'{path}/raw_data'

# Create folder for train and test folder
if not os.path.isdir(parent_path):
    os.makedirs(parent_path)

train_path = f'{parent_path}/train'
test_path = f'{parent_path}/test'

# Create folder for train and test
if not os.path.isdir(train_path):
    os.makedirs(train_path)
if not os.path.isdir(test_path):
    os.makedirs(test_path)

# Create each subfolder in train and test
food_path = f'{path}/food-101/images'
for folder_name in os.listdir(food_path):
    train_subdir = os.path.join(train_path,folder_name)
    test_subdir = os.path.join(test_path,folder_name)

    os.makedirs(train_subdir,exist_ok=True)
    os.makedirs(test_path,exist_ok=True)

    all_files = os.listdir(os.path.join(food_path,folder_name))
    files = [file for file in all_files if file.endwith("jpeg")]

    train_files = files[:900]
    test_files = files[:900]

    for file in train_files:
        src = os.path.join(food_path,folder_name,file)
        dst = os.path.join(train_subdir,file)
        shutil.copy(src,dst)

    for file in test_files:
        src = os.path.join(food_path,folder_name,file)
        dst = os.path.join(test_subdir,file)
        shutil.copy(src,dst)
"""


# Set the path to your parent folder
parent_folder_path = "/path/to/parent/folder"

# Set the paths to the train and test parent folders
train_folder_path = "/path/to/train/folder"
test_folder_path = "/path/to/test/folder"

# Loop through each subdirectory in the parent folder
for subdirectory_name in os.listdir(parent_folder_path):
    # Create paths to the subdirectories in the train and test folders
    train_subdirectory_path = os.path.join(train_folder_path, subdirectory_name)
    test_subdirectory_path = os.path.join(test_folder_path, subdirectory_name)

    # Create the subdirectories in the train and test folders
    os.makedirs(train_subdirectory_path, exist_ok=True)
    os.makedirs(test_subdirectory_path, exist_ok=True)

    # Get a list of all the image file names in the current subdirectory
    image_file_names = os.listdir(os.path.join(parent_folder_path, subdirectory_name))

    # Shuffle the image file names randomly
    random.shuffle(image_file_names)

    for file in train_files:
    src = os.path.join(parent_folder, folder, file)
    dst = os.path.join(train_dir, file)
    shutil.copy(src, dst)"""
