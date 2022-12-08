#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - prints byte info
 * @p: python object
 * return: none
 */
void print_python_bytes(PyObject *p)
{
	char *string;
	long int size, i , limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))

