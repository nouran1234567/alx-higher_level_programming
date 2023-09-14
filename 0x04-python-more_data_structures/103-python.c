#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

/**
 * print_python_bytes - Prints info of  bytes
 *
 * @p: Object
 *
 * Return: none
 */

void print_python_bytes(PyObject *p)
{
	long int sz;
	int x 
	char *try_str = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	PyBytes_AsStringAndSize(p, &try_str, &sz);

	printf("  size: %li\n", sz);
	printf("  trying string: %s\n", try_str);
	if (sz < 10)
		printf("  first %li bytes:", sz + 1);
	else
		printf("  first 10 bytes:");
	for (x = 0; x <= sz && x < 10; x++)
		printf(" %02hhx", try_str[x]);
	printf("\n");
}

void print_python_list(PyObject *p)
{
        long int sz = PyList_Size(p);
        int x;
        PyListObject *list = (PyListObject *)p;
        const char *ty;

        printf("[*] Python list info\n");
        printf("[*] Size of the Python List = %li\n", sz);
        printf("[*] Allocated = %li\n", list->allocated);
        for (x = 0; x < sz; x++)
        {
                type = (list->ob_item[x])->ob_type->tp_name;
		printf("Element %i: %s\n", x, ty);
                if (!strcmp(ty, "bytes"))
                        print_python_bytes(list->ob_item[x]);
        }
}

