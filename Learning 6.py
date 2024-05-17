from enum import Enum

class Color(Enum):
    RED = 'red'
    GREEN = 'green'
    BLUE = 'blue'
    EMPTY = ''

color = Color(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case Color.RED:
        print("I see red!")
    case Color.GREEN:
        print("Grass is green")
    case Color.BLUE:
        print("I'm feeling the blues :(")
    case _:
        pass

def fib(n):
    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
#        print(a, end=' ')
        a, b = b, a+b
    #print()
    return result

#Enter an int:
while True:
    try:
        x = int(input("Enter and int: "))
        break
    except ValueError:
        print("Ooops!")
print('You entered:', x)
fibsequence = fib(x)
print(fibsequence)
# pickup at pg 27