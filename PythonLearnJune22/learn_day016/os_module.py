import os

file_path_x = "/RISHI/H2K/FileIO/demofile_x.txt"

if os.path.exists(file_path_x):
    print("File Exists")
    os.remove(file_path_x)

dir_path = "/RISHI/H2K/FileIO/Apr2022"
if os.path.exists(dir_path):
    os.rmdir(dir_path)
else:
    os.mkdir(dir_path)

root_dir_path = "/RISHI/H2K/FileIO"
target_dir_path = "/RISHI/H2K/FileIO/csv"
list_of_files = os.listdir(root_dir_path)

if not os.path.exists(target_dir_path):
    os.mkdir(target_dir_path)


for eachFile in list_of_files:
    if eachFile.find(".csv") > -1:
        print(eachFile)
        os.replace(root_dir_path+"/"+eachFile, target_dir_path+"/"+eachFile)
