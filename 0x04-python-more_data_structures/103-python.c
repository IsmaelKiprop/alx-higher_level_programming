#include <Python.h>
#include <stdio.h>

/**
 * print_python_bytes - Print information about Python bytes objects
 * @p: PyObject pointer
 */
void print_python_bytes(PyObject *p) {
    PyBytesObject *bytes_obj;
    Py_ssize_t size, i;
    unsigned char *bytes_str;

    printf("[.] bytes object info\n");

    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    bytes_obj = (PyBytesObject *)p;
    size = PyBytes_Size(p);
    bytes_str = PyBytes_AsString(p);

    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", bytes_str);

    printf("  first %ld bytes: ", (size < 10) ? size : 10);
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", bytes_str[i]);
        if (i < 9)
            printf(" ");
    }
    printf("\n");
}

/**
 * print_python_list - Print information about Python lists
 * @p: PyObject pointer
 */
void print_python_list(PyObject *p) {
    PyListObject *list_obj;
    Py_ssize_t size, i;
    PyObject *item;

    printf("[*] Python list info\n");

    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    list_obj = (PyListObject *)p;
    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", list_obj->allocated);

    for (i = 0; i < size; i++) {
        item = PyList_GetItem(p, i);
        printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
        if (PyBytes_Check(item)) {
            print_python_bytes(item);
        }
    }
}
