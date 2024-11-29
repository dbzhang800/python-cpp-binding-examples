import os
import sys

def get_module_path():
    if sys.platform == "win32":
        lib_dir = "bin"
    else:
        lib_dir = "lib"
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../build", lib_dir))

def get_lib_path(base_name):
    if sys.platform == "win32":
        lib_name = f"{base_name}.dll"
    elif sys.platform == "darwin":
        lib_name = f"lib{base_name}.dylib"
    else:
        lib_name = f"lib{base_name}.so"
    return os.path.join(get_module_path(), lib_name)

