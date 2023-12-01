import os

folder_path = input("Enter the path to the folder where you want to change file names: ")
fragment_to_remove = input("Enter the fragment you want to remove from file names: ")

files = os.listdir(folder_path)

for file in files:
    old_path = os.path.join(folder_path, file)
    
    if os.path.isfile(old_path):
        new_file_name = file.replace(fragment_to_remove, '')
        new_path = os.path.join(folder_path, new_file_name)
        
        os.rename(old_path, new_path)
        
print("File names have been changed.")