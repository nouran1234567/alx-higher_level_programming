#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>
#include <stdio.h>

/**
 * print_python_bytes - Prints info of  bytes
 *
 * @p: Object
 *
 * Return: none
 */

void print_python_bytes(PyObject *p)
{
	char *str;
	long int sz; 
	long int lmt;
	long int x

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	sz = ((PyVarObject *)(p))->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", sz);
	printf("  trying string: %s\n", str);

	if (sz >= 10)
		lmt = 10;
	else
		lmt = sz + 1;

	printf("  first %ld bytes:", lmt);

	for (x = 0; x < lmt; x++)
		if (str[x] >= 0)
			printf(" %02x", str[x]);
		else
			printf(" %02x", 256 + str[x]);

	printf("\n");
}

/**
 * print_python_list - Prints info of  list
 *
 * @p: Object
 *
 * Return: none
 */

void print_python_list(PyObject *p)
{
	long int sz, x;
	PyListObject *list;
	PyObject *obj;

	sz = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", sz);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (x = 0; x < sz; x++)
	{
		obj = ((PyListObject *)p)->ob_item[x];
		printf("Element %ld: %s\n", x, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
