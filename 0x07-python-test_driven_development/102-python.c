#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - prints Python strings
 * @p: Python Object
 *
 * Return: no return
 */

void print_python_string(PyObject *p)
{
	PyObject *repr;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	repr = PyObject_Repr(p);

	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));

	if (PyUnicode_IS_COMPACT_ASCII(p))
	{
		printf("  value: %s\n", PyUnicode_AsUTF8(p));
	}
	else
	{
		PyObject *wide_str = PyUnicode_AsWideCharString(p, NULL);

		wprintf(L"  value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
		PyMem_Free(wide_str);
	}
}
