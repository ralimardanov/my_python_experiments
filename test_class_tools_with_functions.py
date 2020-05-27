# Create class named Tools with some functionality(search, zip, unzip, copy, move, rename, create folder and etc)
# Add some kind of menu to show functionalities used in your class
# You should see the same menu after each used function

import os, shutil, glob, sys
from shutil import copy2, move
from zipfile import ZipFile, is_zipfile
class Tools:
    defloc = os.path.dirname(os.path.realpath(__file__))
    def file_search(self, filename, path=None):
        filesstr = ""
        path = path or self.defloc
        if os.path.exists(path):
            for dirs,subdirs,files in os.walk(path):
                for file in files:
                    if filename in file:
                        filesstr += os.path.join(dirs, file) + "\n"
                for subdir in subdirs:
                    if filename in subdir:
                        filesstr += os.path.join(dirs,subdir) + "\n"
        else:
            raise Exception(f"Something is wrong with your {path}")
        
        if filesstr == "":
            raise Exception(f"{filename} isn't in the local directory of the script")
        return filesstr
        
    def zip(self, filename, path=None):
        name = filename + ".zip"
        path = path or self.defloc
        if str(self.file_search(filename, path)).rstrip("\n") == os.path.join(path,filename):
            zippath = os.path.join(path,name)
            source = os.path.join(path,filename)
            mode = "a" if os.path.exists(zippath) else "w"
            with ZipFile(zippath, mode) as zipObj:
                zipObj.write(source, filename)
                return f"{filename}.zip has been created in {path}"
        else:
            raise Exception(f"Something is wrong with your {path} or {filename}")

    def unzip(self, filename, path=""):
        path = path or self.defloc
        if str(self.file_search(filename, path)).rstrip("\n") == os.path.join(path,filename):
            zippath = os.path.join(path,filename)
            if is_zipfile(zippath):
                with ZipFile(zippath, "r") as unzipObj:
                    unzipObj.extractall(path)
                    return f"{filename} has been extracted in {path}"
            else:
                raise Exception (f"Your file: {filename} is not a zip")
        else:
            raise Exception (f"something is wrong with your path of {filename}")

    def copy(self, source, destination):
            if os.path.isdir(destination): #to prevent path creation in case if path doesn't exist
                try:
                    copy2(source,destination)
                    return f"{source} was copied to {destination}"
                except Exception as error:
                    return str(error)
            else:
                raise Exception ("Please write down right destination path")
 
    def move(self, source, destination):
        if os.path.isdir(destination): 
            try:
                move(source,destination)
                return f"{source} was moved to {destination}"
            except Exception as error:
                return str(error)
        else:
            raise Exception ("Please write down right destination path")
    
    def rename(self, filename, renamedfile, path=None):
        path = path or self.defloc
        if str(self.file_search(filename, path)).rstrip("\n") == os.path.join(path,filename):
            source = os.path.join(path,filename)
            rensource = os.path.join(path, renamedfile)
            os.rename(source, rensource)
            return f"{filename} has been renamed to {renamedfile}"
        else:
            raise Exception (f"something is wrong with your path of {filename}")

    def create_folder(self, foldertocreate, path=None):
        try:
            if not path :
                if not os.path.exists(foldertocreate):
                    os.makedirs(os.path.join(self.defloc,foldertocreate))
                    return f"Folders were created in {self.defloc}"
                return f"Folder already exists in {self.defloc}"
            elif os.path.exists(path):
                if not os.path.exists(foldertocreate):
                    os.makedirs(os.path.join(path,foldertocreate))
                    return f"Folders were created in {path}"
                return f"Folder already exists in {path}"
            else:
                raise Exception("It's not the right path")
        except Exception as error:
            return str(error)
    
    def execute(self,choice):
        if choice == 1:
            print("\nYou need to write down filename and path. In case of empty path, script will look for file in default location of script.")
            filename = input("Write down name of file: ")
            path = input("Write down path, where to search: ")
            result = self.file_search(filename, path)
            print(result)
        elif choice == 2:
            print("\nYou need to write down filename and path. In case of empty path, script will zip file in default location of script.")
            filename = input("Write down name of file: ")
            path = input("Write down path, where to zip file: ")
            result = self.zip(filename, path)
            print(result)
        elif choice == 3:
            print("\nYou need to write down filename and path. In case of empty path, script will unzip file in default location of script.")
            filename = input("Write down name of file: ")
            path = input("Write down path, where to unzip file: ")
            result = self.unzip(filename, path)
            print(result)
        elif choice == 4:
            print("\nYou need to write down full path to your file and destination path.")
            filename = input("Write down full path to your file: ")
            path = input("Write down path, where to copy file: ")
            result = self.copy(filename, path)
            print(result)
        elif choice == 5:
            print("\nYou need to write down full path to your file and destination path.")
            filename = input("Write down full path to your file: ")
            path = input("Write down path, where to move file: ")
            result = self.move(filename, path)
            print(result)
        elif choice == 6:
            print("\nYou need to write down filename, to what rename your file and path, where file is. In case of empty path, script will look and rename file in default location of script.")
            filename = input("Write down name of file: ")
            renamedfile = input("Write down to what you want to rename your file: ")
            path = input("Write down path, where to find and rename your file: ")
            result = self.rename(filename, renamedfile, path)
            print(result)
        elif choice == 7:
            print("\nYou need to write down name of folders and path, where to create them. In case of empty path, script will create folders in default location of script.")
            foldertocreate = input("Write down name of folder/folders (note: write your folders like this - /folder1/folder2/folder and etc): ")
            path = input("Write down path, where to create folder/folders: ")
            result = self.create_folder(foldertocreate, path)
            print(result)
        elif choice == 8:
            print("Bye Bye :)")
            sys.exit()

    def menu(self):
        while True:
            menu = input("""Select your option (note: you should only select number):
            1: file_search
            2: zip 
            3: unzip
            4: copy
            5: move
            6: rename
            7: create_folder
            8: quit
            
            Your input: """)
            if menu.isdigit():
                menu = int(menu)
                if not (1 <= menu <= 8):
                    print("Select one of functions from 1 to 8\n")
                    continue
            else:
                print("Select only numbers!\n")
                continue

            self.execute(menu)