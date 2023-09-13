#include <Python.h>
#include <stdio.h>

void print_python_bytes(PyObject *p) {
Py_ssize_t size, i;
unsigned char *bytes_str;

printf("[.] bytes object info\n");

if (PyBytes_Check(p)) {
size = ((PyVarObject *)p)->ob_size;
bytes_str = (unsigned char *)((PyBytesObject *)p)->ob_sval;

printf("  size: %ld\n", size);
printf("  trying string: %s\n", (char *)bytes_str);

printf("  first %ld bytes: ", (size < 10) ? size : 10);
for (i = 0; i < size && i < 10; i++) {
printf("%02x", bytes_str[i]);
if (i < 9)
printf(" ");
}
printf("\n");
} else {
printf("  [ERROR] Invalid Bytes Object\n");
}
}

void print_python_list(PyObject *p) {
Py_ssize_t size, i;
PyObject *item;

printf("[*] Python list info\n");

if (PyList_Check(p)) {
size = ((PyVarObject *)p)->ob_size;

printf("[*] Size of the Python List = %ld\n", size);
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++) {
item = ((PyListObject *)p)->ob_item[i];
printf("Element %ld: %s\n", i, ((PyObject *)item)->ob_type->tp_name);

if (PyBytes_Check(item)) {
print_python_bytes(item);
}
}
} else {
printf("  [ERROR] Invalid List Object\n");
}
}
