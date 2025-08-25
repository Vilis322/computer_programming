import os

main_dir = "file_management"
if not os.path.exists(main_dir):
    os.mkdir(main_dir)

file1_path = os.path.join(main_dir, "file1.txt")
file2_path = os.path.join(main_dir, "file2.txt")

with open(file1_path, "w", encoding="utf-8") as file1:
    file1.write("It is file 1")
with open(file2_path, "w", encoding="utf-8") as file2:
    file2.write("It is file 2")

print("Directory contents:", os.listdir(main_dir))

if os.path.exists(file1_path):
    os.remove(file1_path)

sub_dir = os.path.join(main_dir, "sub_directory")
if not os.path.exists(sub_dir):
    os.mkdir(sub_dir)

new_file2_path = os.path.join(sub_dir, "file2.txt")
if os.path.exists(file2_path):
    os.rename(file2_path, new_file2_path)

if os.path.exists(new_file2_path):
    os.remove(new_file2_path)

if os.path.exists(sub_dir):
    os.rmdir(sub_dir)

if os.path.exists(main_dir):
    os.rmdir(main_dir)

