# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
	skus_clean=""
	for elem in skus:
		if elem.isalpha():
			if elem.islower():
				return -1
			skus_clean= skus_clean+ elem+','
		else:
			return -1
	skus_clean = skus_clean.rstrip(',')

	result = [x.strip() for x in skus_clean.split(',')]

	count = 0


	if 'A' in result:
		a_occurances = result.count("A")
		temp_a_occurances =a_occurances
		for i in range(1,a_occurances+1):
			if i%5==0:
				count+=200
				temp_a_occurances-=5

		temp_a_occurances2 =temp_a_occurances
		for i in range(1,temp_a_occurances+1):
			if i%3==0:
				count+=130
				temp_a_occurances2-=3

		for i in range(temp_a_occurances2):
			count+=50

	if 'C' in result:
		c_occurances = result.count("C")
		c_amt = 20*c_occurances
		count +=c_amt

	if 'D' in result:
		d_occurances = result.count("D")
		d_amt = 15*d_occurances
		count +=d_amt

	b_amount_free = 0
	if 'E' in result:
		e_price = 40
		b_amount_free = 0
		e_occurances = result.count("E")
		temp_e_occurances =e_occurances
		for i in range(1,e_occurances+1):
			if i%2==0:
				count+=(e_price*2)
				b_amount_free+=1
				temp_e_occurances-=2

		for i in range(temp_e_occurances):
			count+=e_price

	check_b_for_discount = result.count("B")
	if check_b_for_discount:
		b_discount =0
		temp_b_amount_free =b_amount_free
		for i in range(1,b_amount_free+1):
			b_discount+=30

	for i in range(1,b_amount_free+1):
		if 'B' in result:
			result.remove('B')
		


	if 'B' in result:
		b_occurances = result.count("B")
		temp_b_occurances =b_occurances
		for i in range(1,b_occurances+1):
			if i%2==0:
				count+=45
				temp_b_occurances-=2

		for i in range(temp_b_occurances):
			count+=30

	f_amount_free = 0
	if 'F' in result:
		f_occurances = result.count("F")
		print(f_occurances)
		temp_f_occurances = f_occurances

		for i in range(1,f_occurances+1):
			if temp_f_occurances <2:
				break

			if i%2==0:
				f_amount_free+=1
			temp_f_occurances-=1


	print(f"f_amount_free {f_amount_free}")

	f_occurances = result.count("F")
	if f_occurances >=3:
		for i in range(1,f_amount_free+1):
			if 'F' in result:
				result.remove('F')

	print(result)


	if 'F' in result:
		f_occurances = result.count("F")
		f_amt = 10*f_occurances
		count +=f_amt

	return count

	raise NotImplementedError()



