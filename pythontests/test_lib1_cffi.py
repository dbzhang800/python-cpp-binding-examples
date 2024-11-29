import os
import sys
from cffi import FFI
import mycommon

lib_full_path = mycommon.get_lib_path('lib1')

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
