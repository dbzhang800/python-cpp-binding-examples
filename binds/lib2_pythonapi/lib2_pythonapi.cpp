#define PY_SSIZE_T_CLEAN
#include <Python.h>
#include "../../cpp/lib2/lib2.h"

static PyObject* py_add(PyObject* self, PyObject* args) {
    int a, b;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)) {
        return NULL;
    }

    int result = add(a, b);  // call functions from lib2
    return PyLong_FromLong(result);
}

static PyMethodDef ModuleMethods[] = {
    {"add", py_add, METH_VARARGS, "Add two numbers"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "lib2_pythonapi",
    "A Python module that links to lib2.dll/liblib2.so",
    -1,
    ModuleMethods
};

PyMODINIT_FUNC PyInit_lib2_pythonapi(void) {
    return PyModule_Create(&moduledef);
}
