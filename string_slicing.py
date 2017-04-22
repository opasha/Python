data = 'XBOX 360 | 150 | New'

data.index('|')

product = data[:data.index('|')] # data.index('|') = 9, so it's data[0:9] = XBOX 360

price = data[data.index('|')+2:data.index('N')-2]

condition = data[data.index('N'):]

print(product)

print(price)

print(condition)