import os
import sys
from cffi import FFI

# Determine the shared library name
lib_base_name = "lib1"
if sys.platform == "win32":
    lib_path = f"bin/{lib_base_name}.dll"
elif sys.platform == "darwin":
    lib_path = f"lib/lib{lib_base_name}.dylib"
else:
    lib_path = f"lib/lib{lib_base_name}.so"
lib_full_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../build", lib_path))

# Create an FFI instance
ffi = FFI()

# Define the C function signature
ffi.cdef("""
         int add(int a, int b);
""")

lib1 = ffi.dlopen(lib_full_path)

# Test the function
def test_lib1_add():
    result = lib1.add(1, 1)
    print(f"lib1.add(1,1) = {result}")
    assert result == 2

if __name__ == "__main__":
    test_lib1_add()
