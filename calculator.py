number1=input('type a number: ')
action=input('multiplication, addition, substraction, or divsion: ')
number2=input('type a second number: ')

if action=='multiplication':
    print(float(number1)*float(number2))

if action=='addition':
    print(float(number1)+float(number2))

if action=='substraction':
    print(float(number1)-float(number2))

if action=='division':
    print(float(number1)/float(number2))