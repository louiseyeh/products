import os     #os:作業系統 operating system
#refactor 重購
def read_file(filename):
	products = []
	with open(filename, 'r',encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續 迴圈繼續 跳到下一回
			name, price = line.strip().split(',')  #split() 完變清單 ,等號前直接定義清單名稱
			products.append([name, price])
	return products
	
#讓使用者輸入
def user_input(products):
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
	return products

#印出所有購買紀錄
#products[0][0] #存取二維清單
def print_products(products):
	for p in products: #for loop 搞清楚清單內每一項目
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:  #'w' 寫入模式(write)
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') # 用+來合併字串(str) 
			                                  #f.write() 才是真正寫入
			                                  #用','分隔存成csv才會分隔

#執行程式
def main():
	filename = 'products.csv'
	if os.path.isfile(filename):     #檢查檔案是否存在
		print('有此檔案!')
		products = read_file(filename)
	else:
		print('找不到檔案!')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()