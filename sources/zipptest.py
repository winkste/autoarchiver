import os
import zipfile
from pathlib import Path

# archiving data to a new zip archive
myPath = os.path.join(os.getcwd(), 'from')
print(myPath)

# use "w" for new and "a" to append to a zip archive
newZip = zipfile.ZipFile(Path("/Users/stephan_wink/Downloads") / "zip_example.zip", "w")

for folder_name, subfolders, file_names in os.walk(myPath):
    print(f"The current folder is: {folder_name}")

    for file_name in file_names:
        print(f"Zipping file: {file_name}")
        newZip.write(Path(folder_name) / file_name, compress_type=zipfile.ZIP_DEFLATED)

newZip.close()
