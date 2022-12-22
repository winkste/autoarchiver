# Name of the project 
This is the project script used to document the program development.

# Program Idea
Idea: A program that checks the "temporary folder" and stores
all files and folders into an archive. Additional generate a text
file that include a list of all archived elements:
input folder: Downloads

Downloads
|->a.txt
|->b.txt
|->c
   |->c.txt

destination folder: archive
archive
|-> archive_downloads_20221112.zip
|-> archive_downloads_20221112.txt

# Program User Interface
This program uses the commandline interface.
- Emulation mode, using test folders:
python3 foldarc -e
- Standard mode:
python3 foldarc -input "/input/path" -output "output/path"
python3 foldarc -i "/input/path" -o "output/path"

# Program structure - Functions
main - main entry, calls the commandline parsing
cmdline_parse: parses the command line and checks valid input, calls process
create_archive(input, output)
   create_archive(input, output) - creates the archive
   create_archive_report(input, output) - creates text file with archive log
   empty_folder()


# Used Python Libraries
pylint, pytest, zipper, argparse, send2trash, os, datetime, logging

# Research
## Commandline parsing using argparse
```
import argparse
parser = argparse.ArgumentParser(description = "Program to archive temporary files")
parser.add_argument("-e", "--emul", help="emulation mode active", action="store_true")
parser.add_argument("-i", "--input", type=str, help="input file")
parser.add_argument("-o", "--output", type=str, help="output file")
args = parser.parse_args()

if args.emul:
    print("emulation mode on")

if args.input:
    print(args.input)

if args.output:
    print(args.output)

if args.target:
    print(args.target)
```
## Path check
from pathlib import Path
p = inputPath
p.is_dir() # true if exists and is folder

## Deleting files by moving to trash
import send2trash
send2trash.send2trash(subfolder/file)

## walking a folder and its subfolders with os.walk function
import os
from pathlib import Path

src = Path.cwd()

for folderName, subfolders, filenames in os.walk(src):
    print(f"The current folder is: {folderName}")

    for subfolder in subfolders:
        print(f"SUBFOLDER OF {folderName}: {subfolder}")
    for filename in filenames:
        print(f"FILE INSIDE {folderName}: {filename}")
    print("")

## Generate datetime for timestamp file name
from datetime import datetime

      # datetime object containing current date and time
      now = datetime.now()
      # YYmmddHMS
      dt_string = now.strftime("%Y%m%d%H%M%S")
      return "backup_" + dt_string + ".zip"