one = {'0': '', '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX'}
ten = {'0': '', '1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC'}
hundreds = {'0': '', '1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM'}
thousands = {'0': '', '1': 'M', '2': 'MM', '3': 'MMM'}

Romannum = {}


for i in range(1, 40):
    textnum = str(i) 
    if len(textnum) == 1:
      Romannum[i] = one[textnum[0]]
    else:
        Rten= textnum[0]    
        Rone = textnum[1] 
        Romannum[i] = ten[Rten] + one[Rone]

while True:
    n = int(input("Enter a number for roman number conversion:"))
    if n in Romannum:
        print(f'The roman number of {n} is " {Romannum[n]} "')
    else:
        break