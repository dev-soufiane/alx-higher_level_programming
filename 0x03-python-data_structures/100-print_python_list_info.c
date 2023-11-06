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
	Py_slist_size_t list_size, idx;
	PyListObject *list_ptr;
	PyObject *list_item;

	list_size = PyList_list_size(p);
	printf("[*] list_size of the Python list_ptr = %zd\n", list_size);

	list_ptr = (PyListObject *)p;
	printf("[*] Allocated = %zd\n", list_ptr->allocated);

	for (idx = 0; idx < list_size; idx++)
	{
		list_item = PyList_GetItem(p, idx);
		printf("Element %zd: %s\n", idx, Py_TYPE(list_item)->tp_name);
	}
}
