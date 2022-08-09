touple=(23,"h3ll",23,[3,5,6])

a,b,c,d=touple
# print(a)
# print(b)
# print(c)
# print(d)


filename="protfolio.csv"
protfolio=[]

for line in open(filename):
    fields=line.split(',')
    name=fields[0]
    shares=fields[1]
    price=fields[2]
    block=(name,shares,price)
    protfolio.append(block)

print(protfolio)