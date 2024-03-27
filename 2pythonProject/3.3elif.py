operand_1=int(input('Enter operand1: '))
operand_2=int(input('Enter operand2: '))
operator=input('Enter the operator (+,-,*,/): ')

#if (test expr):
    #statement
#elif (test expr):
    #statement
#....
#else:
    #statement
#statement

if operator=='+':
    print(operand_1 + operand_2)
elif operator == '-':
    print(operand_1 - operand_2)
elif operator == '*':
    print(operand_1 * operand_2)
elif operator == '/':
    print(operand_1 / operand_2)
else:
    print('None')

print('Thank You')