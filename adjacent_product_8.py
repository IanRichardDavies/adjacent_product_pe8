def largest_adjacent_product(num,d):
    '''
	Finds the largest product of d adjacent numbers in number num
	Solves Project Euler #8
    '''
    maxprod = 1
    for i in range(len(str(num))-d):
        if "0" not in str(num)[i:i+d]:
            prod = 1
            for j in str(num)[i:i+d]:
                prod *= int(j)
            if prod > maxprod:
                maxprod = prod
    return maxprod