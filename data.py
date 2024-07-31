a= 13.42
print(int(a))
ai= int(a)
ai2=a-ai
ai2r=round(ai2,2)
print(ai2r)
b= 42.13
print(int(b))
bi= int(b)
bi2=b-bi
bi2r=round(bi2,2)
print(bi2r)
a3=ai2r*100
print(a3)
b3=bi2r*100
print(b3)
print(ai==b3 or bi==a3)