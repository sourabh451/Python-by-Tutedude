'''
#Celsius ====> Farenheit
c=input('Celsius: ')
c=float(c)
f=(c * 9/5) + 32
print('Farenheit: ',f)


#Farenheit ---> Celsius
f=input('Farenheit: ')
f=float(f)
c=(f - 32) * 5/9
print('Celsius: ',c)
'''

#Simple Interest Calculator:
#Eqn: Pnr/100
p=input('P: ')
n=input('n: ')
r=input('r: ')
p=int(p)
n=int(n)
r=int(r)
si=(p*n*r)/100
print("Simple Interest is: ",si)

