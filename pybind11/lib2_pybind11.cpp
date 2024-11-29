#include <pybind11/pybind11.h>
#include "../cpp/lib2/lib2.h"


PYBIND11_MODULE(lib2_pybind11, m) {
    m.doc() = "A simple example";
    m.def("add", &add, "A function that adds two numbers");
}

