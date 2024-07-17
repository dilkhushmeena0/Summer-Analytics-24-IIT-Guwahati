print('my_mod..')
test = 'Test String'

def find_ind(to_search, target):
    for i, val in enumerate(to_search):
        if val == target:
            return i
        
    return -1