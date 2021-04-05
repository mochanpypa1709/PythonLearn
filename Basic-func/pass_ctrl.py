def foo(password):
    if len(password) >= 8:
        return False
    else:
        return True

print(foo('mochan'))


#function temp
def feel(temp):
    if temp > 25:
        return 'Hot'
    elif 15 <= temp <= 25:
        return 'Warm'
    else:
        return 'Cold'

print(feel(15))