# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

	result = [x.strip() for x in skus.split(',')]
	if all(x.isalpha() for x in result):
		pass
	else:
		return -1

	count = 0

	if 'A' in result:
		a_occurances = result.count("A")
		temp_a_occurances =a_occurances
		for i in range(1,a_occurances+1):
			if i%3==0:
				count+=130
				temp_a_occurances-=3

		for i in range(temp_a_occurances):
			count+=50

	if 'B' in result:
		b_occurances = result.count("B")
		temp_b_occurances =b_occurances
		for i in range(1,b_occurances+1):
			if i%2==0:
				count+=45
				temp_b_occurances-=2

		for i in range(temp_b_occurances):
			count+=30
		

	if 'C' in result:
		c_occurances = result.count("C")
		c_amt = 20*c_occurances
		count +=c_amt

	if 'D' in result:
		d_occurances = result.count("D")
		d_amt = 15*d_occurances
		count +=d_amt

	return count

	raise NotImplementedError()





