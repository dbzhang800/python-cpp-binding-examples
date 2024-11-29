import ctypes
import os
import sys
import mycommon

# Load the shared library
sys.path.insert(0, mycommon.get_module_path())
import lib2_pybind11

# Test the function
def test_lib2_add():
    result = lib2_pybind11.add(1, 1)
    print(f"lib2_pybind11.add(1,1) = {result}")
    assert result == 2

if __name__ == "__main__":
    test_lib2_add()
