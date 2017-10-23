

def make_blank_charmap_A(y=49, x=80):

   rows = []; 
   for  j in range(y):
    row = []
    for i in range(x): 
     row.append([None, None, None])
    rows.append(row)
   return rows



def make_blank_charmap_B(y=49, x=80):

   none = [None];                   rows    =  none  * 49
   for  y, row  in enumerate(rows): rows[y] = [None] * 80
   for  y, row  in enumerate(rows):
    for x, none in enumerate(row ): row [x] = [None, None, None]
   return rows


# DANGEROUSLY RESOURCE-HUNGRY METHOD
def make_blank_charmap_C(y=49, x=80):
   return eval(repr([[[None, None, None]]*x]*y))



setup_A = '''from __main__ import make_blank_charmap_A'''
code_A  = '''charmap = make_blank_charmap_A(50, 80)'''

setup_B = '''from __main__ import make_blank_charmap_B'''
code_B  = '''charmap = make_blank_charmap_B(50, 80)'''

# DANGEROUSLY RESOURCE-HUNGRY METHOD - 500x800 PC FROZED TO COMPLETE UNRESPONSIVENESS
setup_C = '''from __main__ import make_blank_charmap_C'''
code_C  = '''charmap = make_blank_charmap_C(50, 80)'''


import timeit as t

print(min(t.repeat(code_A, setup_A, number=10)))
print(min(t.repeat(code_B, setup_B, number=10)))

# DANGEROUSLY RESOURCE-HUNGRY METHOD
print(min(t.repeat(code_C, setup_C, number=10)))

