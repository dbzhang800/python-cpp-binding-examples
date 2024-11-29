import os
import sys

def get_lib_path(base_name):
    if sys.platform == "win32":
        lib_name = f"bin/{base_name}.dll"
    elif sys.platform == "darwin":
        lib_name = f"lib/lib{base_name}.dylib"
    else:
        lib_name = f"lib/lib{base_name}.so"
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../build", lib_name))
