import os

DOC_DIR = '../Documents'
docs = os.listdir(DOC_DIR)

docs_index = {}
inv_index = {}
stopword = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as",
            "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

for idx, doc in enumerate(docs):
    f = open(DOC_DIR+'/'+doc, 'r')
    docs_index[idx] = doc
    tokens = f.read().lower().strip().split(' ')
    for token in tokens:
        if token in stopword:
            continue
        if token in inv_index:
            check = inv_index[token]
            if(docs.index(doc) in check):
                continue
            inv_index[token].insert(0, [tokens.index(token), docs.index(doc)])
        else:
            inv_index[token] = [[tokens.index(token), docs.index(doc)]]

print(inv_index)
print(docs_index)
