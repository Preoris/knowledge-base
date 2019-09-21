#!/bin/python

def add(matrix1, matrix2):
	newmatrix = [[0,0],[0,0]]
	newmatrix[0][0] = matrix1[0][0] + matrix2[0][0]
	newmatrix[0][1] = matrix1[0][1] + matrix2[0][1]
	newmatrix[1][0] = matrix1[1][0] + matrix2[1][0]
	newmatrix[1][1] = matrix1[1][1] + matrix2[1][1]
	return newmatrix
	
#mat1 = [[1, -2],[-3, 4]]
#mat2 = [[2, -1],[0, -1]]
