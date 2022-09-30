import math

def egyptian_frac(numerator, denominator):
    # Creating our list of denominators for our Egyptian Fractions
    egypt_list = []
    while numerator != denominator:

        x = math.ceil(denominator/numerator)
        egypt_list.append(x)

        numerator = x * numerator - denominator
        denominator *= x

        str = ""

        for ones in egypt_list:
            str += "1/{0} + ".format(ones)

        fina_string = str[:-3]

        return fina_string

print(egyptian_frac(7,12)) 