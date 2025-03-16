import sys
from pathlib import Path
from colorama import Fore

def main():

    try: 
        args = sys.argv
        if(len(args) == 1):
            raise Exception("Specify folder path!")

        folder_path = Path(args[1])

        if (not folder_path.exists()):
            raise FileNotFoundError("Folder not found")

        print(Fore.BLUE, folder_path.resolve().name)
        look_at_folder(folder_path)
        
    except Exception as err:
        print(err)



def look_at_folder(path: Path, indent=0):
  
    for item in path.iterdir():
        # if(item.name == ".git" or item.name == ".venv"):
        #     continue      

        if item.is_dir():
            print(Fore.BLUE, " " * indent, item.name)
            inner_path = path / item.name
            look_at_folder(inner_path, indent + 3)
        else:
            print(Fore.GREEN," " * indent, item.name)
        




if __name__ == "__main__":
    main()





