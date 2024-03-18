# import os
#
# file = os.listdir()
#
#
# with os.scandir(os.getcwd()) as file_scan:
#     for entry in file_scan:
#         info = entry.stat()
#         print(f"fayl nomi --> {file} |||||||--->>> atributlar --> {info.st_mtime}")

####################################################################

# from pathlib import Path
#
# file = Path("NewFolder")  # create new folder
#
# file.mkdir()

####################################################################

# import os

# print(os.getcwd())
# file = os.getcwd() + "/matn.txt"
# os.remove(file)
