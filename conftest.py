""" This module defines configuration for pytest.

Longer description of this module.

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

__author__ = "One solo developer"
__authors__ = ["One developer", "And another one", "etc"]
__contact__ = "mail@example.com"
__copyright__ = "Copyright $YEAR, $COMPANY_NAME"
__credits__ = ["One developer", "And another one", "etc"]
__date__ = "YYYY/MM/DD"
__deprecated__ = False
__email__ =  "mail@example.com"
__license__ = "GPLv3"
__maintainer__ = "developer"
__status__ = "Production"
__version__ = "0.0.1"

################################################################################
# Imports
import pytest
import os

@pytest.fixture()
def my_data():
    """ my_data test fixture.
    """
    return [1, 2, 3, 4]

@pytest.fixture
def get_path_of_a_file1_txt(tmpdir):
    """ This ficture returns a string representation of a file
    """
    file_path = tmpdir.join("file1.txt")
 
    return os.path.abspath(file_path)

@pytest.fixture
def get_path_archiver_test1(tmpdir):
    """ This ficture returns a string representation of a path
    """
    path_path = tmpdir.mkdir("archiver_test1")
 
    return os.path.abspath(path_path)

@pytest.fixture
def get_path_to_correct_input_folder(tmpdir):
    """ This ficture returns a string representation of a path
    """
    path_path = tmpdir.mkdir("archiver_input")
    for i in range(0, 10):
        file = path_path.join(f"file{i}.txt")
        file.write("This is just test data.")

    return os.path.abspath(path_path)

@pytest.fixture
def get_list_of_files_from_input(tmpdir):
    """ This ficture returns a list of strings for input folder
    """
    path_path = tmpdir.join("archiver_input")
    return os.listdir(path_path)

@pytest.fixture
def get_path_to_correct_output_folder(tmpdir):
    """ This ficture returns string for output folder
    """
    path_path = tmpdir.mkdir("archiver_output")
    return os.path.abspath(path_path)