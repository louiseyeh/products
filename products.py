products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格:')
#	p = []
#	p.append(name)
#	p.append(price)
#	p = [name, price]
	products.append([name, price])
print(products)

#products[0][0] #存取二維清單

for p in products: #for loop 搞清楚清單內每一項目
	print(p[0], '的價格是', p[1])