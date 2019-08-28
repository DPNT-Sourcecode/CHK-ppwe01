# noinspection PyUnusedLocal
# skus = unicode string

def discount_A(just_price=False, result=None):
	if just_price:
		return 50

	count=0
	a_occurances=0
	a_occurances = result.count("A")
	price = getFullPrice(discount_A(just_price=True),a_occurances)
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

	#print(f"price {price}")
	#print(f"count {count}")
	discount = price - count
	return discount


def discount_B(just_price=False, result=None, waiting=True):
	if just_price:
		return 30
	if waiting:
		return True

	count=0
	b_occurances=0
	b_occurances = result.count("B")
	price = getFullPrice(discount_B(just_price=True),b_occurances)
	temp_b_occurances =b_occurances
	for i in range(1,b_occurances+1):
		if i%2==0:
			count+=45
			temp_b_occurances-=2

	for i in range(temp_b_occurances):
		count+=30

	#print(f"price {price}")
	#print(f"count {count}")
	discount = price - count
	return discount



def discount_E(just_price=False, result=None):
	#print("E")
	if just_price:
		return 40

	e_price = 40
	b_amount_free = 0
	count=0
	e_occurances=0
	b_discount =0

	e_occurances = result.count("E")
	temp_e_occurances =e_occurances
	for i in range(1,e_occurances+1):
		if i%2==0:
			count+=(e_price*2)
			b_amount_free+=1
			temp_e_occurances-=2
	for i in range(temp_e_occurances):
		count+=e_price

	#print(f"b_amount_free {b_amount_free}")
	check_b_for_discount = result.count("B")
	if check_b_for_discount:
		b_discount =0
		for i in range(1,b_amount_free+1):
			b_discount+=30

	for i in range(1,b_amount_free+1):
		if 'B' in result:
			result.remove('B')

	#print(f"b_discount {b_discount}")
	return b_discount



def discount_F(just_price=False,result=None):
	
	if just_price:
		return 10

	#print(f'discount_F - result: {result}')
	f_amount_free = 0
	count=0
	f_occurances = result.count("F")
	#print(f"f_occurances {f_occurances}")
	price = getFullPrice(discount_F(just_price=True),f_occurances)
	temp_f_occurances = f_occurances

	for i in range(1,f_occurances+1):
		if temp_f_occurances <2:
			break
		if i%2==0:
			f_amount_free+=1
		temp_f_occurances-=1

	#print(f"f_amount_free {f_amount_free}")

	if f_occurances >=3:
		for i in range(1,f_amount_free+1):
			if 'F' in result:
				result.remove('F')

	if 'F' in result:
		f_occurances = result.count("F")
		f_amt = 10*f_occurances
		count +=f_amt

	return price - count





def discount_H(just_price=False, result=None):
	if just_price:
		return 10

	count=0
	h_occurances=0
	h_occurances = result.count("H")
	#print(f"h_occurances {h_occurances}")
	price = getFullPrice(discount_H(just_price=True),h_occurances)
	temp_h_occurances =h_occurances

	#print("\nfor i in range(1,h_occurances+1):")
	for i in range(1,h_occurances+1):
		if i%10==0:
			print(f"i%10==0 {i%10==0}")
			count+=80
			temp_h_occurances-=10
	#print(f"\ntemp_h_occurances {temp_h_occurances}")

	temp_h_occurances2 =temp_h_occurances

	#print("\nfor i in range(1,temp_h_occurances+1):")
	for i in range(1,temp_h_occurances+1):
		if i%5==0:
			#print(f"i%5==0 {i%5==0}")
			count+=45
			temp_h_occurances2-=5
	#print(f"\ntemp_h_occurances {temp_h_occurances2}")

	#print("\nfor i in range(temp_h_occurances2):")
	for i in range(temp_h_occurances2):
		print(f"i: {i}")
		count+=10

	#print(f"price {price}")
	#print(f"count {count}")
	discount = price - count
	return discount




def discount_K(just_price=False, result=None):
	#print("K")
	if just_price:
		return 80

	count=0
	k_occurances=0
	k_occurances = result.count("K")
	price = getFullPrice(discount_K(just_price=True),k_occurances)
	temp_k_occurances =k_occurances
	for i in range(1,k_occurances+1):
		if i%2==0:
			count+=150
			temp_k_occurances-=2

	for i in range(temp_k_occurances):
		count+=80

	#print(f"price {price}")
	#print(f"count {count}")
	discount = price - count
	return discount



def discount_N(just_price=False, result=None):
	if just_price:
		return 40

	n_price = 40
	m_amount_free = 0
	count=0
	n_occurances=0
	m_discount =0

	n_occurances = result.count("N")
	#print( f"n_occurances {n_occurances}")

	temp_n_occurances =n_occurances
	#print("\n for i in range(1,n_occurances+1):")
	for i in range(1,n_occurances+1):
		if i%3==0:
			print(f"i%3==0: {i%3==0}")
			count+=(n_price*3)
			m_amount_free+=1
			temp_n_occurances-=3
	#print(f"temp_n_occurances {temp_n_occurances}")
	#print(f"m_amount_free {m_amount_free}")

	#print("\n for i in range(1,temp_n_occurances+1):")
	for i in range(temp_n_occurances):
		count+=n_price
		#print(f"count {count}")

	check_m_for_discount = result.count("M")
	#print(f"check_m_for_discount {check_m_for_discount}")
	if check_m_for_discount:
		m_discount =0
		for i in range(1,m_amount_free+1):
			m_discount+=15

	for i in range(1,m_amount_free+1):
		if 'M' in result:
			result.remove('M')

	return m_discount




def discount_P(just_price=False, result=None):
	if just_price:
		return 50

	count=0
	p_occurances=0
	p_occurances = result.count("P")
	price = getFullPrice(discount_P(just_price=True),p_occurances)
	temp_p_occurances =p_occurances
	for i in range(1,p_occurances+1):
		if i%5==0:
			count+=200
			temp_p_occurances-=5

	for i in range(temp_p_occurances):
		count+=50

	#print(f"price {price}")
	#print(f"count {count}")
	discount = price - count
	return discount




def discount_Q(just_price=False, result=None, waiting=True):
	if just_price:
		return 30

	if waiting:
		return True
	count=0
	q_occurances=0
	q_occurances = result.count("Q")
	price = getFullPrice(discount_Q(just_price=True),q_occurances)
	temp_q_occurances =q_occurances
	for i in range(1,q_occurances+1):
		if i%3==0:
			count+=80
			temp_q_occurances-=3

	for i in range(temp_q_occurances):
		count+=30

	#print(f"price {price}")
	#print(f"count {count}")
	discount = price - count
	#print(f"q__discount {discount}")
	return discount






def discount_R(just_price=False, result=None):
	if just_price:
		return 50


	r_price = 50
	q_amount_free = 0
	count=0
	r_occurances=0
	q_discount =0

	r_occurances = result.count("R")
	#print( f"n_occurances {r_occurances}")

	temp_r_occurances =r_occurances
	#print("\n for i in range(1,r_occurances+1):")
	for i in range(1,r_occurances+1):
		if i%3==0:
			print(f"i%3==0: {i%3==0}")
			count+=(r_price*3)
			q_amount_free+=1
			temp_r_occurances-=3
	#print(f"temp_r_occurances {temp_r_occurances}")
	#print(f"q_amount_free {q_amount_free}")

	#print("\n for i in range(1,temp_r_occurances+1):")
	for i in range(temp_r_occurances):
		count+=r_price
		#print(f"count {count}")

	check_q_for_discount = result.count("Q")
	#print(f"check_q_for_discount {check_q_for_discount}")
	if check_q_for_discount:
		q_discount =0
		for i in range(1,q_amount_free+1):
			q_discount+=30

	for i in range(1,q_amount_free+1):
		if 'Q' in result:
			result.remove('Q')
	#print(f"q_discount {q_discount}")
	return q_discount



def discount_U(just_price=False, result=None):
	if just_price:
		return 40

	#print(f'discount_U - result: {result}')
	u_amount_free = 0
	count=0
	u_occurances = result.count("U")
	#print(f"u_occurances {u_occurances}")
	price = getFullPrice(discount_U(just_price=True),u_occurances)
	temp_u_occurances = u_occurances

	for i in range(1,u_occurances+1):
		if temp_u_occurances <2:
			break
		if i%3==0:
			u_amount_free+=1
		temp_u_occurances-=1

	#print(f"u_amount_free {u_amount_free}")

	if u_occurances >=4:
		for i in range(1,u_amount_free+1):
			if 'U' in result:
				result.remove('U')

	if 'U' in result:
		u_occurances = result.count("U")
		u_amt = 40*u_occurances
		count +=u_amt

	return price - count






def discount_V(just_price=False, result=None):
	if just_price:
		return 50

	count=0
	v_occurances=0
	v_occurances = result.count("V")
	price = getFullPrice(discount_V(just_price=True),v_occurances)
	temp_v_occurances =v_occurances
	for i in range(1,v_occurances+1):
		if i%3==0:
			count+=130
			temp_v_occurances-=3

	temp_v_occurances2 =temp_v_occurances
	for i in range(1,temp_v_occurances+1):
		if i%2==0:
			count+=90
			temp_v_occurances2-=3

	for i in range(temp_v_occurances2):
		count+=50

	#print(f"price {price}")
	#print(f"count {count}")
	discount = price - count
	return discount


def getTotalBeforeDiscount(result):
	total_price_without_discount =0
	for elem in result:
		if elem in discount_skus:
			price =available_skus[elem](just_price=True)
		else:
			price = available_skus[elem]
		total_price_without_discount +=price
	return total_price_without_discount

def getFullPrice(price, occurances):
	return price*occurances



available_skus = {
				  'A':discount_A,'B':discount_B,'C':20,'D':15,'E':discount_E,'F':discount_F,'G':20,'H':discount_H,'I':35,'J':60,
				  'K':discount_K,'L':90,'M':15,'N':discount_N,'O':10,'P':discount_P,'Q':discount_Q,'R':discount_R,'S':30,'T':20,
				  'U':discount_U,'V':discount_V,'W':20,'X':90,'Y':10,'Z':50}
discount_skus = ['A','B','E','F','H','K','N','P','Q','R','U','V']



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


	if 'M' in result and 'N' in result:
		#result_copy = result.copy()
		result_copy = []
		n_occurances = result.count("N")
		m_occurances = result.count("N")
		for elem in result:
			if elem == 'M':
				result_copy.append('N')
			elif elem == 'N':
				result_copy.append('M')
			else:
				result_copy.append(elem)

		result = result_copy.copy()

		#print(f"result if m and n present {result_copy}")

	total_price_without_discount = getTotalBeforeDiscount(result)
	discount =0
	discount_skus_copy = discount_skus.copy()
	for elem in result:
		#print(f"discount_skus_copy {discount_skus_copy}")
		if elem in discount_skus_copy:
			waiting = available_skus[elem](result=result)
			if waiting == True:
				#print("waiting  "+elem)
				continue
			discount +=available_skus[elem](result=result)
			discount_skus_copy.remove(elem)

	for elem in result:
		if elem in discount_skus_copy:
			#print(f"elem....{elem}")
			discount +=available_skus[elem](result=result, waiting=False)
			discount_skus_copy.remove(elem)


	#print(f"price after discount {total_price_without_discount-discount}")
	count = total_price_without_discount-discount
	#print(result)
	return count

	raise NotImplementedError()

