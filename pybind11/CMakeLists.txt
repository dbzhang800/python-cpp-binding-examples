
set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 REQUIRED)

pybind11_add_module(lib2_pybind11 lib2_pybind11.cpp)
target_link_libraries(lib2_pybind11 PRIVATE lib2 pybind11::module)
