d = 0.85
structure = {'A':['B','C'] , 'B':['C'] , 'C':['A'] , 'D':['C']}
values = {'A': 1 , 'B': 1 , 'C': 1 , 'D': 1}

for i in structure:
  for j in structure[i]:
    values[i] = (values[i] * d) / len(structure[i])


