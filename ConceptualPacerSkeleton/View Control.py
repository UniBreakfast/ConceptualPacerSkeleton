from cui3toolbox import *
from itertools import chain

def make_cliche_charmap(y=49, x=80):
    return (((B_BLACK, F_DIM_WHITE, '.'),)*x,)*y

GR=GROUND = make_cliche_charmap()


def make_blank_charmap(y=49, x=80):

   none = [None];                   rows    =  none  * y
   for  j, row  in enumerate(rows): rows[j] = [None] * x
   for  j, row  in enumerate(rows):
    for i, none in enumerate(row ): row [i] = (None, None, None)
   return rows


level = make_blank_charmap()


#for i, char in enumerate([[B_BLACK, F_DIM_WHITE, 'S'],
#                          [B_BLACK, F_DIM_WHITE, 'e'],
#                          [B_BLACK, F_DIM_WHITE, 'e'],
#                          [B_BLACK, F_DIM_WHITE, ' '],
#                          [B_BLACK, F_DIM_WHITE, 't'],
#                          [B_BLACK, F_DIM_WHITE, 'h'],
#                          [B_BLACK, F_DIM_WHITE, 'e'],
#                          [B_BLACK, F_DIM_WHITE, ' '],
#                          [B_BLACK, F_DIM_WHITE, 'r'],
#                          [B_BLACK, F_DIM_WHITE, 'e'],
#                          [B_BLACK, F_DIM_WHITE, 'a'],
#                          [B_BLACK, F_DIM_WHITE, 's'],
#                          [B_BLACK, F_DIM_WHITE, 'o'],
#                          [B_BLACK, F_DIM_WHITE, 'n']]):
#    #level[0][i]=char
#    level[20+i][25+i]=char

# Создаёт снимок сверху: смысловая часть, вокруг которой видна подложка.
overview = make_blank_charmap()
for j, y in enumerate(level):
    for i, x in enumerate(y):
        if x[0]:
            overview[j][i] = x
        else:
            overview[j][i] = GR[j][i]


#Пишет нужный текст нужным цветом в символьную карту.
def write_to_charmap(charmap, text, colors, pos_y, pos_x):
    for i, char in enumerate(text):
        charmap[pos_y][pos_x+i] = (colors[0], colors[1], char)

write_to_charmap(overview, "Ok, now we're talking!", (B_DIM_RED, F_BLUE), 0, 0)


# Делает из двухмерного массива одномерный.
overview_linear=list(chain(*overview))


# Очищает цвето-коды из всех ячеек, где они не меняются.
first_match=True
for i, char in enumerate(overview_linear[1:]):
    if first_match:
        if char[0] == overview_linear[i][0] and char[1] == overview_linear[i][1]:
            overview_linear[i+1] = [overview_linear[i+1][2]]
            first_match=False
            j = i
    else:
        if char[0] == overview_linear[j][0] and char[1] == overview_linear[j][1]:
            overview_linear[i+1] = [overview_linear[i+1][2]]
        else:
            first_match=True

        
# Превращает одномерный массив значений в длииииинную строку.
overview_string=[]
for y in overview_linear:
        overview_string.append(''.join(y))

#del overview_string[-1]
print(end=''.join(overview_string))

print(overview_string[:25])

string=overview_string

#chars = [*string][:20]



#char = [chars[0]]
#char = chars[0].encode('unicode-escape')

#char = b'\\u0421'.decode('unicode-escape')


#print(chars)


