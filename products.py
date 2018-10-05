
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

with open('products.csv', 'w', encoding='utf-8') as f:  #'w' 寫入模式(write)
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 用+來合併字串(str) 
		                                  #f.write() 才是真正寫入
		                                  #用','分隔存成csv才會分隔
