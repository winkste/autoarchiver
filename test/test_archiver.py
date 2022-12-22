""" pytest module for archiver

This module defines the tests for the main.py module. Further explains of
pytest and unit tests can be found here in this video (german):
https://youtu.be/db2Iq2JHwiQ
https://docs.pytest.org/en/7.2.x/
https://docs.pytest.org/en/7.2.x/getting-started.html#get-started
https://docs.python.org/3/library/unittest.html


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
import sys
import pytest
from sources.archiver import main
#from conftest import get_path_of_file

def test_given_not_str_archiver_will_raise_exception():
    """
        This function tests for valid input pathes
    """
    with pytest.raises(TypeError):
        main("blabla", "blublu")

def test_given_not_pathes_archiver_will_raise_exception(get_path_of_a_file1_txt, 
                                                        get_path_archiver_test1):
    """
        This function tests if archiver handles path checks
        correct.
    """
    file_of_path = get_path_of_a_file1_txt
    path_of_path = get_path_archiver_test1
    with pytest.raises(TypeError):
        main(file_of_path, path_of_path)
    with pytest.raises(TypeError):
        main(path_of_path, file_of_path)

def test_given_in_out_archiver_will_return_list(get_path_to_correct_input_folder,
                                                    get_list_of_files_from_input,
                                                    get_path_to_correct_output_folder):
    """
        This function tests if archiver returns a correct list
        of files.
    """
    in_path = get_path_to_correct_input_folder
    result_list = get_list_of_files_from_input
    out_path = get_path_to_correct_output_folder
    file_list = main(in_path, out_path)
    assert file_list == result_list