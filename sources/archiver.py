""" This module creates a backup archive of folder content + archive report
    text file.

This program generates a backup of an input path and places this backup
into an output path. Additional it is generating a text file as log file
with all elements stored into the archive. Only elements stored in the
archive shall be listed in the text file and will be moved to trash.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.
"""

__author__ = "Stephan Wink"
__contact__ = "stephan_wink@web.de"
__copyright__ = "Copyright $2022, $WShield"
__date__ = "2022/11/12"
__deprecated__ = False
__email__ =  "stephan_wink@web.de"
__license__ = "GPLv3"
__maintainer__ = "Stephan Wink"
__status__ = "Development"
__version__ = "0.0.1"

################################################################################
# Imports
import os
import datetime
import logging
from pathlib import Path
import zipfile
import send2trash


logging.basicConfig(level=logging.DEBUG,
    format="%(asctime)s - %(filename)s/%(funcName)s(%(lineno)d) - %(levelname)s - %(message)s")

################################################################################
# Variables

################################################################################
# Functions

def main(input_path_name:str, output_path_name:str):
    """
        This is the main processing function
    """
    if not isinstance(input_path_name, str) or not isinstance(output_path_name, str):
        raise TypeError("Arguments are not strings")

    input_path = Path(input_path_name)
    output_path = Path(output_path_name)
    logging.debug("Input path %s", os.path.abspath(input_path))
    logging.debug("Output path %s", os.path.abspath(input_path))

    if not input_path.exists() or not output_path.exists():
        raise TypeError("Pathes are not existing")

    if not input_path.is_dir() or not output_path.is_dir():
        raise TypeError("Arguments are not pathes")

    list_of_files = create_list_of_files(input_path)
    list_of_files = filter_list_of_files_by_date(list_of_files, 5)
    new_zip = archive_files(list_of_files, output_path)
    archive_list = create_archive_file_list(new_zip)
    create_archive_log_file(archive_list, output_path)
    move_archived_files_to_trash(archive_list, input_path.anchor)

    return 0

def archive_files(list_of_files:list, output_path:Path) -> zipfile.ZipFile:
    """ This function is zipping the folder and storing the archive
    """
    # use "w" for new and "a" to append to a zip archive
    archive_name = f"{create_archive_name()}.zip"
    with zipfile.ZipFile(output_path / archive_name, "w") \
        as archive:

        for elems in list_of_files:
            archive.write(elems, compress_type=zipfile.ZIP_DEFLATED)
            logging.debug("Zipping file: %s", elems)

    return archive

def create_archive_file_list(zip_file:Path) -> list:
    """ This function returns a list of files in the archive
    """
    return zip_file.namelist()

def create_archive_log_file(archive_list:list, output_path:Path):
    """ This function logs the list of archived files in output_path
    """
    log_name = f"{create_archive_name()}.log"
    with open(output_path / log_name, mode="w", encoding="utf-8") \
        as log_file:
        for elem in archive_list:
            log_file.write(elem + "\n")

def move_archived_files_to_trash(archive_list, anchor):
    """ This function moves the archived files from input to trash.
    """
    for elem in archive_list:
        #send2trash.send2trash(f"{input_path.anchor}{elem}")
        logging.debug("simulated move to trash: %s/%s", anchor, elem)

def create_archive_name():
    """
    This function generate a time / date based name
    """
    # datetime object containing current date and time
    now = datetime.datetime.now()
    # YYmmddHMS
    dt_string = now.strftime("%Y%m%d%H%M")
    return f"archive_{dt_string}"

def create_list_of_files(dir_name:Path) -> list:
    """create a list of file and sub directories
        names in the given directory
    """
    list_of_files = []
    for (dir_path, dir_names, files) in os.walk(dir_name):
        list_of_files += [os.path.join(dir_path, file) for file in files]

    return list_of_files

def filter_list_of_files_by_date(list_of_files:list, delta_days:int) -> list:
    """ This function filters the list of files according to date. 
    """
    now = datetime.datetime.now()
    date_past = now - datetime.timedelta(days=delta_days)

    for file in list_of_files:
        time_stamp = os.path.getmtime(file)
        file_time = datetime.datetime.fromtimestamp(time_stamp)
        if file_time > date_past:
            list_of_files.remove(file)

    return list_of_files

def test_func(delta_days:int):
    now = datetime.datetime.now()
    date_past = now - datetime.timedelta(days=delta_days)
    print(f"Past: {date_past}")

################################################################################
# Classes

################################################################################
# Scripts
if __name__ == "__main__":
    # execute only if run as a script
    print('--- foldarc script ---')
    main(os.path.join(os.getcwd(), 'from'), os.path.join(os.getcwd(), 'to'))

