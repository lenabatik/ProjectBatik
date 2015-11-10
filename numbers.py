import math

class Numbers:
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		if c > 0:
			self.c = c
		else:
			self.c = 0
		print(self.a, self.b, self.c)
			
	def sum(self):
		return self.a + self.b + self.c
	
	def multiplication(self):
		return self.a * self.b * self.c
	
	def abs_multiplication(self):
		return math.fabs(self.a * self.b * self.c)
	
"""proba1=Numbers(2,3,4)
proba1.sum()
print(proba1.sum())
print(proba1.multiplication())
print(proba1.abs_multiplication())"""
