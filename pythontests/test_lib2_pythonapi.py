import os
import sys
import mycommon

sys.path.insert(0, mycommon.get_module_path())
import lib2_pythonapi

# Test the function
def test_lib2_add():
    result = lib2_pythonapi.add(1, 1)
    print(f"lib2_pythonapi.add(1,1) = {result}")
    assert result == 2

if __name__ == "__main__":
    test_lib2_add()
