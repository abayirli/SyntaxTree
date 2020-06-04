from SyntaxTree import Expression, Plus, Times, Const, Var

def main():

	e1 = Times(Const(3), Plus(Var("y"), Var("x")))
	e2 = Plus(Times(Const(3), Var("y")), Var("x"))

	env = {"x": 2, "y": 3}

	print(f"e1: {e1} = {e1.eval(env)}")
	print(f"e2: {e2} = {e2.eval(env)}")

if __name__ == "__main__":
	main()