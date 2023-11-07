#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 * @p: PyObject
 *
 * Return: Void
 */

void print_python_list_info(PyObject *p)
{
	long int list_size, idx;
	PyListObject *list_ptr;
	PyObject *list_item;

	list_size = Py_SIZE(p);

	printf("[*] Size of the Python List = %ld\n", list_size);

	list_ptr = (PyListObject *)p;

	printf("[*] Allocated = %ld\n", list_ptr->allocated);

	for (idx = 0; idx < list_size; idx++)
	{
		list_item = PyList_GetItem(p, idx);
		printf("Element %ld: %s\n", idx, Py_TYPE(list_item)->tp_name);
	}
}
