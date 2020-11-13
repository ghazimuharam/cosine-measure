import os
import nltk
import math


class CosineMeasure():
    """
    Calculate cosine measure from given query
    """
    pass

    stopwords = ['a', 'but', 'for', 'is', 'on', 'not', 'the',
                 'are', 'while', 'were', 'will', 'with', 'when', 'toward', 'of']
    stemmer = nltk.stem.porter.PorterStemmer()

    def __init__(self, query, dir_path):
        self.query = query
        self.dir_path = dir_path
        self.files = []
        self.word = []
        self.word2doc = {}

    def word2documents(self):
        """
        mapping word in each documents to their index frequency
        """
        self.files = sorted(os.listdir(self.dir_path))
        for file_idx, file in enumerate(self.files):
            documents = open(self.dir_path+'/'+file, 'r')
            word_tokenizer = documents.read().split(' ')

            for word in word_tokenizer:
                if word not in self.stopwords:
                    stemmed = self.stemmer.stem(word)
                    if stemmed not in self.word:
                        self.word.append(stemmed)

                    if stemmed not in self.word2doc:
                        self.word2doc[stemmed] = {file_idx: 1}
                    else:
                        if file_idx in self.word2doc[stemmed].keys():
                            self.word2doc[stemmed][file_idx] += 1
                        else:
                            self.word2doc[stemmed][file_idx] = 1

        return self.word2doc

    def calculate_idf(self):
        """
        calculate inverse document frequency
        """
        idf = []
        for key in self.word2doc.keys():
            key_idf = math.log2(len(self.files)/len(self.word2doc[key]))
            idf.append(key_idf)

        return idf

    def total_term(self, file_idx):
        """
        total term of a query or document
        based on identified term in self.word
        """
        doc_total_term = 0
        for term in self.word:
            if file_idx in self.word2doc[term].keys():
                doc_total_term += self.word2doc[term][file_idx]

        return doc_total_term

    def count_tf(self):
        """
        calculate term frequency in a documents
        """
        term_frequency = {}
        for file_idx in range(len(self.files)):

            doc_total_term = self.total_term(file_idx)
            term_frequency[file_idx] = []
            for term in self.word:
                if file_idx in self.word2doc[term]:
                    term_count = self.word2doc[term][file_idx]
                    tf = term_count/doc_total_term

                    term_frequency[file_idx].append(tf)
                else:
                    term_frequency[file_idx].append(0)

        return term_frequency

    def vector_norm(self, vectors):
        """
        calculate norm of a vector
        """
        total_sum = sum([vector**2 for vector in vectors])

        return math.sqrt(total_sum)

    def document_vector(self):
        """
        calculate document vector (tf-idf)
        """
        tf = self.count_tf()
        idf = self.calculate_idf()

        weight = {}
        for doc_tf in tf.keys():
            tfidf = [(tf[doc_tf][i]*idf[i]) for i in range(len(idf))]
            weight[doc_tf] = tfidf

        return weight

    def query_vector(self):
        """
        calculate query_vector (tf-idf)
        """
        idf = self.calculate_idf()

        query = "do big dogs run on the carpet with cat"
        word_tokenizer = query.split(' ')

        query_freq = [0 for i in range(len(self.word))]
        for word in word_tokenizer:
            stemmed = self.stemmer.stem(word)
            if stemmed not in self.word:
                continue
            query_freq[self.word.index(stemmed)] += 1

        total_freq = sum(query_freq)

        tfidf = [((tf/total_freq)*idf) for tf, idf in zip(query_freq, idf)]

        return tfidf

    def cosine_measure(self):
        """
        docstring
        """
        query_vector = self.query_vector()
        norm_vector = self.vector_norm(query_vector)

        docs_vector = self.document_vector()

        all_docs = []
        for file_idx in docs_vector.keys():
            docxquery = [(docs_vector[file_idx][i]*query_vector[i])
                         for i in range(len(self.word))]

            # print(sum(docxquery), (self.vector_norm(
            #     docs_vector[file_idx]) * norm_vector))

            hasil = (sum(docxquery) /
                     (self.vector_norm(docs_vector[file_idx]) * norm_vector))
            all_docs.append(hasil)

        return all_docs

    def get_word(self):
        """
        docstring
        """
        return self.word
