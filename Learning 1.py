# measure some strings
words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))




# Code that modifies a collection while iterating over that same collection
# can be tricky to get right.
# Instead, it is usually more straight-forward to loop over a copy
# of the collection or to create a new collection:


# Strategy:  Iterate over a copy

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(users)
for user, status in users.copy().items():
    if status == 'inactive':
        print('Removing', user)
        del users[user]
print('Collection is now', users, '\n')

# Strategy:  Create a new collection

# Create a sample collection
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print(users)
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        print('Found an active user', user, '; adding to active users collection')
print('New collection is:', active_users)


# Range function:
print(list(range(5, 10)))			# prints [5, 6, 7, 8, 9]
print(list(range(0, 10, 3)))		# prints [0, 3, 6, 9]		(step is 3)
print(list(range(-10, -100, -30)))	# prints [-10, -40, -70]	(step is -30)

# To iterate over the indices of a sequence, use range() and len()
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
# prints:
# 0 Mary
# 1 had
# 2 a
# 3 little
# 4 lamb

# Printing a range() gives an iterable.
print('range(10) is an iterable object:', range(10))
print('sum() takes an iterable object, such as sum(range(4):', sum(range(4)))


# Break and Else Statements:

# The break statement breaks out of the innermost enclosing for or while loop.
# In a for loop, the else clause is executed after the loop reaches its final iteration.
# In a while loop, it’s executed after the loop’s condition becomes false.

# In either kind of loop,
# the else clause is not executed if the loop was terminated by a break.

print('Searching for Primes:')
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:							# modulus whole division
            print(n, 'equals', x, '*', n//x)	# remainder
            break								# break out of inner X loop
    else:								        # loop failed in finding a factor
        print(n, 'is a prime number')

# Note: a try statement’s else clause runs when no exception occurs,
# 		and a loop’s else clause runs when no break occurs.


# Continue Statement:
# Continues with the next iteration of the loop.
for num in range(2, 10):
    if num % 2 == 0:
        print("Found an even number", num)
        continue
    print("Found an odd number", num)


# Match Statements:
# Only the first pattern that matches gets executed.

def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404 | 418:										# cases can be combined
            return "Not found / I'm a teapot"
        case _:												# case _ catches everything
            return "Something's wrong with the internet"

x = 0
print('x before match point (1,0) is currently:', x)
# Match cases can be used to bind variables:
# point is an (x, y) tuple
point = (1,0)
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):						# binds 1 to x
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")

print('x after match point (1,0) is currently:', x)
