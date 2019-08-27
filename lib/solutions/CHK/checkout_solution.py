# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	result = [x.strip() for x in skus.split(',')]

	count = 0

	if 'A' in result:
		a_occurances = result.count("A")
		if a_occurances >= 3:
			if a_occurances%3==0:
				r = a_occurances//3
				for i in range(r):
					count+=130
			else:
				temp_a_occurances =a_occurances
				for i in range(1,a_occurances+1):
					if a_occurances%3==0:
						count+=130
						temp_a_occurances-=3


		else
			count += 50



	if 'B' in result:
		count += 30
	if 'C' in result:
		count +=20

    raise NotImplementedError()



