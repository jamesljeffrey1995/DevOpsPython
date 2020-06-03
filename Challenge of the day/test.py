from Factorial import factorialCalc
import pytest


def testAnswer():
	assert factorialCalc(8) == 40320
	assert factorialCalc(6) == 45