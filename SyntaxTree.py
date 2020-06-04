class Expression:
	"""General Expression class where all expressions inherif from"""
	pass

class Times(Expression):
	"""Multiplication object where there is left and right hand sides"""
	def __init__(self,left, right):
		self.left  = left
		self.right = right

	def __str__(self):
		return "(" + str(self.left) + " * " + str(self.right) + ")"

	def eval(self, env):
		return self.left.eval(env) * self.right.eval(env)

class Plus(Expression):
	"""Addition object where there is left and right hand sides"""
	def __init__(self,left, right):
		self.left  = left
		self.right = right
	
	def __str__(self):
		return "(" + str(self.left) + " + " + str(self.right) + ")"

	def eval(self, env):
		return self.left.eval(env) + self.right.eval(env)

class Const(Expression):
	"""Constant object with an associated numerical value"""
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return str(self.value)

	def eval(self, env):
		return self.value

class Var(Expression):
	"""Variable object with associated name"""
	def __init__(self, name):
		self.name = name

	def __str__(self):
		return self.name

	def eval(self, env):
		return env[self.name]

