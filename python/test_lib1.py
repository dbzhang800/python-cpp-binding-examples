import ctypes
import os
import sys

# Determine the shared library name
lib_base_name = "lib1"
if sys.platform == "win32":
    lib_path = f"bin/{lib_base_name}.dll"
elif sys.platform == "darwin":
    lib_path = f"lib/lib{lib_base_name}.dylib"
else:
    lib_path = f"lib/lib{lib_base_name}.so"
lib_full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build", lib_path))

# Load the shared library
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
