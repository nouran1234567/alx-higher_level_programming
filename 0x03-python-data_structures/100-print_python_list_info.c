#include <Python.h>

/**
 * print_python_list_info - Prints python lists basic info
 *
 * @p: PyObject *p list.
 */

void print_python_list_info(PyObject *p)
{
	int sz, loc, x;
	PyObject *item;
	sz = Py_SIZE(p);
	loc = ((PyListObject *)p)->allocated;
	printf("[*] Size of the Python List = %d\n", sz);
	printf("[*] Allocated = %d\n", loc);
	for (x = 0; x < sz; x++)
	{
		printf("Element %d: ", x);
		item = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(item)->tp_name);
	}
}
