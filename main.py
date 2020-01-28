from math import sqrt
print("Hello World!")
print("This is the prime number checker!")

start_number = input("What number would you like to start at? (It has to be greater than 0)  ")
end_number = input("What number would you like to end at? ")
counter = float(start_number)

def is_divisible(dividend, divisor):
    #print "dividend % divisor" + str(dividend % divisor)
    if (dividend % divisor == 0):
      divisible = True
    else:
      divisible = False
    return divisible

primes = []

while counter <= end_number:
  top = sqrt(float(counter))
  #print top

  i = 2

  

  div = False

  while (i <= top and div == False):
    div = is_divisible(counter, i)
    i += 1
    #print div
    #print i
    #print 

  #print div
  if div == False:
    print( str(counter) + " is prime yoooooo!")
    primes.append(counter)
  else:
    print( str(counter) + " is not prime. Let's get an F in the chat bro")
  counter += 1

for prime in primes:
  print(prime)

input("Press enter to continue." )
sleep(300)
