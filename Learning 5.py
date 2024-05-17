

# How to immplement the following?:
#
# 4.6: Mapping patterns: {"bandwidth": b, "latency": l}capturesthe "bandwidth"and"latency"
# values from a dictionary. Unlike sequence patterns, extra keys are ignored. An unpacking like **rest is also
# supported. (But **_ would be redundant, so it is not allowed.)


    
class HTTPProperties:
    def __init__(self, 

http_properties1 = {}
http_properties2 = {("bandwidth", 250)}
http_properties3 = {("ping", 34), ("bandwidth", 250), ("latency", 10)}
print(f"{http_properties1}\n{http_properties2}\n{http_properties3}")

def identify_properties(http_properties):
    match http_properties:
        case {}:
            print('status is empty')
        case _:
            pass
    #        for property, value in http_property.items()
    #            if property == "bandwidth
            print('unknown http status')

identify_properties(http_properties1)
identify_properties(http_properties2)

