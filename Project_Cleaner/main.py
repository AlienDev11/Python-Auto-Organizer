import os
import shutil
import sys

File_Formats = set()
All_Files = list()


def main():

    try:
        Arg1 = sys.argv[1]
    except IndexError:
        print("USAGE : main.py FOLDER_LOCATION")

    if os.path.exists(Arg1):
        os.chdir(Arg1)
    else:
        print("ERROR 404 NO FILE FOUND,MAKE SURE THE DIRECTORY EXISTS")

    for files in os.listdir():
        All_Files.append(files)
        if any(files.endswith(n) for n in File_Formats):
            pass
        elif not os.path.isdir(files):
            File_Formats.add(files.split(".")[-1])

    Organize()

def Organize():

    for n in File_Formats:
        if os.path.exists(n + " Files"):
            print("Folder Already Exists")
        else:
            os.mkdir(n + " Files")

    FolderPut()

def FolderPut():

    for j in All_Files:
        if any(j.endswith(k) for k  in File_Formats):
            shutil.move(j,str(j.split(".")[1] + " Files"))




main()
