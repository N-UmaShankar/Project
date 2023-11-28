from google.colab import drive
import os

drive.mount('/content/drive')
%cd /content/drive/MyDrive
!unzip /content/drive/MyDrive/TACODataset.zip -d /content/drive/MyDrive/dataset_taco/ && mv /content/drive/MyDrive/dataset_taco/TACODataset/* /content/drive/MyDrive/dataset_taco/ && rm -r /content/drive/MyDrive/dataset_taco/TACODataset
# Define the path to the TACODataset folder
dataset_folder = "/content/drive/MyDrive/dataset_taco"
# Function to count files in a folder
def count_files(folder):
    count = sum([len(files) for root, dirs, files in os.walk(folder)])
    return count
# Count files in images and labels folders
images_count = count_files(os.path.join(dataset_folder, "images"))
labels_count = count_files(os.path.join(dataset_folder, "labels"))
# Print the total count
total_count = images_count + labels_count
print(f"Total number of files in TACODataset: {total_count}")
print(f"Number of images: {images_count}")
print(f"Number of labels: {labels_count}")

import os
import shutil
from sklearn.model_selection import train_test_split

def copy_files(source_folder, destination_folder, file_list, label_extension=".txt"):
    for file in file_list:
        base_name, extension = os.path.splitext(file)
        source_image_path = os.path.join(source_folder, file)
        source_label_path = os.path.join(source_folder, f"{base_name}{label_extension}")
        destination_image_path = os.path.join(destination_folder, file)
        destination_label_path = os.path.join(destination_folder, f"{base_name}{label_extension}")

        # Check if the corresponding label file exists before copying
        if os.path.exists(source_label_path):
            shutil.copy(source_image_path, destination_image_path)
            shutil.copy(source_label_path, destination_label_path)

# Define the root folder
root_folder = "/content/drive/MyDrive/TACODataset"

# Define the folders
images_folder = os.path.join(root_folder, "images")
labels_folder = os.path.join(root_folder, "labels")

# Define the ratios for train, test, and valid sets
train_ratio = 0.7
test_ratio = 0.2
valid_ratio = 0.1

# Get the list of files in the images folder
image_files = os.listdir(images_folder)

# Split the dataset into train, test, and valid sets
train_files, test_valid_files = train_test_split(image_files, test_size=(test_ratio + valid_ratio), random_state=42)
test_files, valid_files = train_test_split(test_valid_files, test_size=(valid_ratio / (test_ratio + valid_ratio)), random_state=42)

# Create train, test, and valid folders
train_images_folder = os.path.join(root_folder, "train", "images")
train_labels_folder = os.path.join(root_folder, "train", "labels")
test_images_folder = os.path.join(root_folder, "test", "images")
test_labels_folder = os.path.join(root_folder, "test", "labels")
valid_images_folder = os.path.join(root_folder, "valid", "images")
valid_labels_folder = os.path.join(root_folder, "valid", "labels")

os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(test_images_folder, exist_ok=True)
os.makedirs(test_labels_folder, exist_ok=True)
os.makedirs(valid_images_folder, exist_ok=True)
os.makedirs(valid_labels_folder, exist_ok=True)

# Copy files to train, test, and valid folders
copy_files(images_folder, train_images_folder, train_files)
copy_files(labels_folder, train_labels_folder, train_files)

copy_files(images_folder, test_images_folder, test_files)
copy_files(labels_folder, test_labels_folder, test_files)

copy_files(images_folder, valid_images_folder, valid_files)
copy_files(labels_folder, valid_labels_folder, valid_files)

print("Dataset split into train, test, and valid sets.")

import os
import shutil
from sklearn.model_selection import train_test_split

def copy_files(source_folder, destination_folder, file_list, label_extension=".txt"):
    for file in file_list:
        base_name, extension = os.path.splitext(file)
        source_image_path = os.path.join(source_folder, file)
        source_label_path = os.path.join(source_folder, f"{base_name}{label_extension}")
        destination_image_path = os.path.join(destination_folder, file)
        destination_label_path = os.path.join(destination_folder, f"{base_name}{label_extension}")

        # Check if the corresponding label file exists before copying
        if os.path.exists(source_label_path):
            shutil.copy(source_image_path, destination_image_path)
            shutil.copy(source_label_path, destination_label_path)

# Define the root folder
root_folder = "/content/drive/MyDrive/dataset_taco"

# Define the folders
images_folder = os.path.join(root_folder, "images")
labels_folder = os.path.join(root_folder, "labels")

# Define the ratios for train, test, and valid sets
train_ratio = 0.7
test_ratio = 0.2
valid_ratio = 0.1

# Get the list of files in the images folder
image_files = os.listdir(images_folder)

# Split the dataset into train, test, and valid sets
train_files, test_valid_files = train_test_split(image_files, test_size=(test_ratio + valid_ratio), random_state=42)
test_files, valid_files = train_test_split(test_valid_files, test_size=(valid_ratio / (test_ratio + valid_ratio)), random_state=42)

# Create train, test, and valid folders
train_images_folder = os.path.join(root_folder, "train", "images")
train_labels_folder = os.path.join(root_folder, "train", "labels")
test_images_folder = os.path.join(root_folder, "test", "images")
test_labels_folder = os.path.join(root_folder, "test", "labels")
valid_images_folder = os.path.join(root_folder, "valid", "images")
valid_labels_folder = os.path.join(root_folder, "valid", "labels")

os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(test_images_folder, exist_ok=True)
os.makedirs(test_labels_folder, exist_ok=True)
os.makedirs(valid_images_folder, exist_ok=True)
os.makedirs(valid_labels_folder, exist_ok=True)

# Copy files to train, test, and valid folders
copy_files(images_folder, train_images_folder, train_files)
copy_files(labels_folder, train_labels_folder, train_files)

copy_files(images_folder, test_images_folder, test_files)
copy_files(labels_folder, test_labels_folder, test_files)

copy_files(images_folder, valid_images_folder, valid_files)
copy_files(labels_folder, valid_labels_folder, valid_files)

print("Dataset split into train, test, and valid sets.")
