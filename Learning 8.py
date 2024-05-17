#  (*name must occur before **name.)
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
    print('Parameters:\nKind:', kind, '\n*arguments:', arguments, '\n**keywords:', keywords)
        
cheeseshop("Limburger", "It's very runny, sir.",
            "It's really very, VERY runny, sir.",
            shopkeeper="Michael Palin",
            client="John Cleese",
            sketch="Cheese Shop Sketch")

# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#		^Positional Only
#					   ^Positional or Keyword
#									  ^Keyword Only
#  / and * are optional. If used, these symbols indicate
# the kind of parameter by how the arguments may be passed
# to the function.  If / and * are not present in the function definition,
# arguments may be passed to a function by position or by keyword.

# Consider that 'name' is both a positional and keyword argument.
#
# Running this command:
#	foo(1, **{'name': 2})
#
# This is Invalid for a function:
#
# def foo(name, **kwds):
#	return 'name' in kwds
#
# This is Valid for a function:
# def foo(name, /, **kwds):
#	return 'name' in kwds
#
# The '/' is required to process the 'name' variable in the library because
# the argument is a position_or_keyword definition.

# Guidance:

# Use positional-only if you want the name of the parameters
# to not be available to the user.
# This is useful when:
# 1) Parameter names have no real meaning
# 2) If you want to enforce the order of the arguments when the function is called
# 3) If you need to take some positional parameters and arbitrary keywords.

# Use keyword-only when names have meaning
# and the function definition is more understandable by being explicit with names
# or you want to prevent users relying on the position of the argument being passed.

# For an API, use positional-only
# to prevent breaking API changes if the parameter’s name is modified in the future.