#include <listobject.h>
#include <object.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: PyObject
 *
 * Return: Void
 */

void print_python_list_info(PyObject *p)
{
	int i;
	long int list_size = PyList_Size(p);
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", list_size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < list_size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
