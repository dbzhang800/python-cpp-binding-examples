import ctypes
import os
import sys
import mycommon

# Load the shared library
lib_full_path = mycommon.get_lib_path('lib1')
try:
    lib1 = ctypes.CDLL(lib_full_path)
    print(f"Successfully loaded library from {lib_full_path}")
except OSError as e:
    print(f"Failed to load library: {e}")
    sys.exit(1)

# Specify the function signature
lib1.add.argtypes = [ctypes.c_int, ctypes.c_int]
lib1.add.restype = ctypes.c_int

# Test the function
def test_lib1_add():
    result = lib1.add(1, 1)
    print(f"lib1.add(1,1) = {result}")
    assert result == 2

if __name__ == "__main__":
    test_lib1_add()
