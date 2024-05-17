# 4.8.5
# 4.8.6 Lambda Expressions
# What is happening in this example?
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

print('\n')
# 4.8.8 Function Annotations

def f(ham: str, eggs: str = 'eggs')-> str:
    print("Annotations:", f.__annotations__) # annotations attribute are stored in the function dictionary
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs

print(f('spam'))


