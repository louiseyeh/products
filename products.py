import os     #os:作業系統 operating system

products = []
# 讀取檔案
if os.path.isfile('products.csv'):     #檢查檔案是否存在
	print('有此檔案!')
	with open('products.csv', 'r',encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue #繼續 迴圈繼續 跳到下一回
			name, price = line.strip().split(',')  #split() 完變清單 ,等號前直接定義清單名稱
			products.append([name, price])
	print(products)
else:
	print('找不到檔案...')


#讓使用者輸入
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

#印出所有購買紀錄
#products[0][0] #存取二維清單
for p in products: #for loop 搞清楚清單內每一項目
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:  #'w' 寫入模式(write)
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n') # 用+來合併字串(str) 
		                                  #f.write() 才是真正寫入
		                                  #用','分隔存成csv才會分隔
