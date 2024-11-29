import os
import sys
import glob
import shutil
import mycommon

mymodule_path = mycommon.get_module_path()

def find_module_file():
    """
    Find the SIP generated module file.
    SIP builds the module in a directory like:
    'build/lib2_sip/build/lib.win-amd64-cpython-312/lib2_sip.*'
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    pattern = os.path.join(script_dir, "../bindings/lib2_sip/build/lib2_sip/build/lib.*/lib2_sip.*")
    files = glob.glob(pattern)
    return files[0] if files else None

my_lib2_sip = find_module_file()
shutil.copy2(my_lib2_sip, mymodule_path)

sys.path.insert(0, mymodule_path)
import lib2_sip

# Test the function
def test_lib2_add():
    result = lib2_sip.add(1, 1)
    print(f"lib2_sip.add(1,1) = {result}")
    assert result == 2

if __name__ == "__main__":
    test_lib2_add()
