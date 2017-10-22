#enter the number
num = 3

factorial = 1
if num < 0:
    print ("factors dont exist for negative numbers and stuff")
elif num == 0:
    print ("the factor is 1")
else:
  for i in range( 1, num + 1) :
      factorial = factorial*i
print ("the factorial of", num,"is", factorial )

