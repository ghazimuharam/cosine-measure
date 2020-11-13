terms = ['approach', 'breakthrough', 'drug', 'hope',
         'new', 'patient', 'schizophrenia', 'treatment']

hashed = []
for term in terms:
    hashval = 0
    for idx, i in enumerate(term):
        hashval = hashval + (ord(i) * idx+1)
    hashed.append(hashval)

for idx, term in enumerate(terms):
    print(term, ': ', hashed[idx])
