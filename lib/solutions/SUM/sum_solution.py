# noinspection PyShadowingBuiltins,PyUnusedLocal
def compute(x:int, y:int) -> int:
	if x<0 or x>100 or y<0 or y>100:
		raise ValueError('Numbers must be positive, (between 0-100)')
	return x+y
	raise NotImplementedError()




