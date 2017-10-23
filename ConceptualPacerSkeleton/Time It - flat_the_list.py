

def make_blank_charmap(y=50, x=80):

   none = [None];                   rows    =  none  * y
   for  j, row  in enumerate(rows): rows[j] = [None] * x
   for  j, row  in enumerate(rows):
    for i, none in enumerate(row ): row [i] = [None, None, None]
   return rows

two_dimensional_list = make_blank_charmap()



def flat_the_list_A(two_dim_list):
    flat_list=[]
    for y in two_dim_list:
        for x in y:
            flat_list.append(x)
    return flat_list



def flat_the_list_B(two_dim_list):
    return [y for x in two_dim_list for y in x]



import itertools
def flat_the_list_C(two_dim_list):
    return list(itertools.chain(*two_dim_list))


setup_A = '''from __main__ import flat_the_list_A, two_dimensional_list'''
code_A  = '''flat_the_list_A(two_dimensional_list)'''

setup_B = '''from __main__ import flat_the_list_B, two_dimensional_list'''
code_B  = '''flat_the_list_B(two_dimensional_list)'''

setup_C = '''import itertools
from __main__ import flat_the_list_C, two_dimensional_list'''
code_C  = '''flat_the_list_C(two_dimensional_list)'''


import timeit as t

print(min(t.repeat(code_A, setup_A, number=100)))
print(min(t.repeat(code_B, setup_B, number=100)))
print(min(t.repeat(code_C, setup_C, number=100)))

