import shutil, os, datetime
import pathlib, glob


#VARIABLE AND CONSTANTS AND ARRAYS
size_dirs = [
    "less than 1Mb",
    "less than 10Mb",
    "less than 20Mb",
    "More than 20Mb",
]


print("Welcome to your file organiser.\nThis is just an example of how much you can do with automation by python.")
print("How would you like to organise your files today. They will be kept neatly in seperate folders.\n")
print("Type 1 to organize your files in folders according to their size (<1mb, <10mb, <20mb, >20mb")
print("Type 2 to organize your files in folders according to their date modified.")

while True:
    try:
        type_organise = int(input("Enter your choice: "))
        if (type_organise == 1 or type_organise == 2):
            break
        print("Invalid Input. Retry with a valid input.")
    except ValueError:
        print("Please enter a number.")

cwd = os.getcwd()

files = [f for f in os.listdir(cwd) if os.path.isfile(os.path.join(cwd, f))]

if (type_organise == 1):
    for dirs in size_dirs:
        new_dir = os.path.join(cwd, dirs)
        os.mkdir(new_dir)
    for file in files:
        file_path = os.path.join(cwd, file)
        if (os.path.getsize(file_path) < 1048577):
            move_path = os.path.join(cwd, size_dirs[0])
            shutil.copy(file_path, move_path)
        elif (os.path.getsize(file_path) < 10485761 and os.path.getsize(file_path) > 1048576):
            move_path = os.path.join(cwd, size_dirs[1])
            shutil.copy(file_path, move_path)
        elif (os.path.getsize(file_path) < 20971521 and os.path.getsize(file_path) > 10485760):
            move_path = os.path.join(cwd, size_dirs[2])
            shutil.copy(file_path, move_path)
        elif (os.path.getsize(file_path) > 20971520):
            move_path = os.path.join(cwd, size_dirs[3])
            shutil.copy(file_path, move_path)
    for file in files:
        file_path = os.path.join(cwd, file)
        os.unlink(file_path) 
else:
    # List all files in the home directory
    files = glob.glob(os.path.expanduser("~/*"))
    # Sort by modification time (mtime) ascending and descending
    sorted_by_mtime_ascending = sorted(files, key=lambda t: os.stat(t).st_mtime)
    sorted_by_mtime_descending = sorted(files, key=lambda t: -os.stat(t).st_mtime)

