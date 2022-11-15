l = [1,2,3,4,5,6]
gen = (x*2 for x in l)
print(gen)

def power(n,exp):
    expo = exp
    res = 0
    if expo < 1:
        return res
        print(expo)
    else:
        res *= power(n,expo)
    expo -= 1


print(power(3,3))