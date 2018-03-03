import random

  # http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html
a = [int(x) for x in input("Please enter a list of numbers: ").split()]
b = [int(x) for x in input("Please enter another list of numbers: ").split()]
for i in range(random.randint(0,20)):
    a.append(random.randint(0,100))
print(a)
for i in range(random.randint(0,20)):
    b.append(random.randint(0,100))
print(b)
fin = []
if (len(a) >= len(b)):
    for element in a:
        if element in b:
            if element not in fin:
                fin.append(element)
else:
    for element in b:
        if element in a:
            if element not in fin:
                fin.append(element)
print(fin)

'''
  # http://www.practicepython.org/exercise/2014/02/26/04-divisors.html
uNum = int(input("What would you like to devise?  "))
divisor = [];
x = range(2,uNum)

for element in x:
    if ((uNum % element) == 0):
        divisor.append(element)

print("the divisors to your number are: "+str(divisor))
'''

'''
  # http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html
uIn = [int(x) for x in input("Please enter a list of numbers: ").split()]
mOut = [];
for element in uIn:
    if(element < 5):
        mOut.append(element)
print("Numbers below five:")
print(mOut)
singleDigit = int(input("Please enter a single digit: "))
for element in uIn:
    if(element > singleDigit):
        uIn.remove(element)
print("This are inputs smaller than the number you gave: ")
print(uIn)
'''