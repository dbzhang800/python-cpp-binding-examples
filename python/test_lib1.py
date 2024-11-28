import ctypes
import os
import sys

# Determine the shared library name
if sys.platform == "win32":
    lib_name = "lib1.dll"
    lib_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build/bin"))
elif sys.platform == "darwin":
    lib_name = "lib1.dylib"
    lib_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build/lib"))
else:
    lib_name = "lib1.so"
    lib_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build/lib"))

# Load the shared library
try:
    lib1 = ctypes.CDLL(os.path.join(lib_dir, lib_name))
    print(f"Successfully loaded library from {os.path.join(lib_dir, lib_name)}")
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
