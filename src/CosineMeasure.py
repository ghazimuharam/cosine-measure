import os
import nltk
import math


class CosineMeasure():
    """
    Calculate documents similarity between
    documents and query provided
    """

    # Stopwords provided by assigment, feel free to change with your
    stopwords = ['a', 'but', 'for', 'is', 'on', 'not', 'the',
                 'are', 'while', 'were', 'will', 'with', 'when', 'toward', 'of']

    # PorterStemmer to stem english term
    stemmer = nltk.stem.porter.PorterStemmer()

    # constructor for CosineMeasure
    def __init__(self, query, dir_path):
        self.query = query  # Query to find
        self.dir_path = dir_path  # Directory path of corpus
        self.files = []  # File name in corpus directory
        self.word = []  # All term found in corpus
        self.word2doc = {}  # Dictionary of word and doc

    def word2documents(self):
        """
        Mapping each word in documents to their frequency
        base on the index of self.word
        """

        # Find all file name in corpus directory
        self.files = sorted(os.listdir(self.dir_path))

        # Read all file
        for file_idx, file in enumerate(self.files):
            documents = open(self.dir_path+'/'+file, 'r')

            # Tokenizer provided by assigment files,
            # feel free to change tokenizer with other method of split
            word_tokenizer = documents.read().split(' ')

            # Looping for the entire word in a documents
            for word in word_tokenizer:
                # Removing stopwords from list of stopwords
                if word not in self.stopwords:
                    # Stem every term with PorterStemmer
                    stemmed = self.stemmer.stem(word)
                    if stemmed not in self.word:
                        # Append only unique word
                        self.word.append(stemmed)

                    # Checking for the appearance in word2doc dictionary
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
        Calculate inverse document frequency
        """
        idf = []

        # using log with base 2 to calculate idf
        # idf = log2(total_file/total_specificterm_appear)
        for key in self.word2doc.keys():
            key_idf = math.log2(len(self.files)/len(self.word2doc[key]))
            idf.append(key_idf)

        return idf

    def total_term(self, file_idx):
        """
        Return total term of a query or document
        based on identified term in self.word
        takes in file index based on self.files
        """

        doc_total_term = 0
        for term in self.word:
            if file_idx in self.word2doc[term].keys():
                doc_total_term += self.word2doc[term][file_idx]

        return doc_total_term

    def count_tf(self):
        """
        Calculate term frequency in a documents
        """
        term_frequency = {}

        # Looping for the entire files
        for file_idx in range(len(self.files)):

            # Tf = total_specific_term/total_term_in_file
            doc_total_term = self.total_term(file_idx)
            term_frequency[file_idx] = []
            for term in self.word:

                # Check file_idx appearance in word2doc specific term
                if file_idx in self.word2doc[term]:
                    term_count = self.word2doc[term][file_idx]
                    tf = term_count/doc_total_term

                    term_frequency[file_idx].append(tf)
                else:
                    # Line below keep the entire line align
                    term_frequency[file_idx].append(0)

        return term_frequency

    def vector_norm(self, vectors):
        """
        Calculate norm of a vector
        """
        # ||d|| = math.sqrt(sum(each_vector**2))
        total_sum = sum([vector**2 for vector in vectors])

        return math.sqrt(total_sum)

    def document_vector(self):
        """
        Calculate document vector (tf-idf)
        """

        tf = self.count_tf()
        idf = self.calculate_idf()

        weight = {}

        # Calculate tf idf for each documents
        for doc_tf in tf.keys():
            # Elementwise multiplication
            tfidf = [(tf[doc_tf][i]*idf[i]) for i in range(len(idf))]
            weight[doc_tf] = tfidf

        return weight

    def query_vector(self):
        """
        Calculate query_vector (tf-idf)
        """
        idf = self.calculate_idf()

        query = self.query
        word_tokenizer = query.split(' ')

        # Finding term frequency of each term in query
        query_freq = [0 for i in range(len(self.word))]
        for word in word_tokenizer:
            stemmed = self.stemmer.stem(word)
            if stemmed not in self.word:
                continue
            query_freq[self.word.index(stemmed)] += 1

        total_freq = sum(query_freq)

        # Calculate tfidf of a qeury
        tfidf = [((tf/total_freq)*idf) for tf, idf in zip(query_freq, idf)]

        return tfidf

    def cosine_measure(self):
        """
        Measure similarity between documents
        and query using cosine measure
        """

        # Pre-processing and calculation before
        # Measuring Cosine
        self.word2documents()
        self.calculate_idf()
        self.count_tf()
        self.document_vector()
        self.query_vector()

        query_vector = self.query_vector()
        norm_vector = self.vector_norm(query_vector)  # Query norm vector
        docs_vector = self.document_vector()

        all_docs = []

        # Calculate Cosine using Cosine Measure formula
        # CosineM(d1, q) = sum(elementwise_mul(d1, q))/(docs_norm*query*norm)
        for file_idx in docs_vector.keys():
            docxquery = [(docs_vector[file_idx][i]*query_vector[i])
                         for i in range(len(self.word))]
            hasil = (sum(docxquery) /
                     (self.vector_norm(docs_vector[file_idx]) * norm_vector))
            all_docs.append(hasil)

        return all_docs

    def document_ranking(self):
        """
        Print document ranking based on Cosine Measure
        """
        all_docs = self.cosine_measure()

        print(
            f'\t\tCosine Measure\nQuery: {self.query.capitalize()}')

        for file_idx, docs_rank in enumerate(all_docs):
            print(f'{self.files[file_idx]}: {docs_rank}')
