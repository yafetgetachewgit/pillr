import scipy as sp


def error(f, x, y):
	return sp.sum((f(x)-y)**2)