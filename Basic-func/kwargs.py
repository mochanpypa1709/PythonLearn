def mean(**kwargs):
    return kwargs

#output will dict
print(mean(a=1, b=2, c=3))


#kwargs sum sample
def find_sum(**kwargs):
    return sum(kwargs.values())
    
print(find_sum(a=5, b=4))


#find winner
def find_winner(**kwargs):
    return max(kwargs, key = kwargs.get)
 
print(find_winner(Andy = 17, Marry = 19, Sim = 45, Kae = 34))