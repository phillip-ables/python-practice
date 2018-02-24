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