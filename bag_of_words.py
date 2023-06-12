import sys
p1 = str(sys.argv[1])

corpus = open(p1, "r")
corpus2 = corpus.readlines()

# schopi - list to string
my_string = ''
my_list = corpus2
for i in range(len(my_list)):
 my_string += my_list[i]
 if i != len(my_list) - 1:
   my_string += ', '

# print(my_string)
corpus_string = my_string


corpus_prenorm = corpus_string.replace(".","")
corpus_prenorm2 = corpus_prenorm.replace("§","")
corpus_prenorm3 = corpus_prenorm2.replace(":","")
corpus_prenorm4 = corpus_prenorm3.replace(",","")
corpus_prenorm5 = corpus_prenorm4.replace("\n","" )
corpus_norm = corpus_prenorm5.lower()
corpus_pretokens = corpus_norm.strip()
corpus_tokens = corpus_pretokens.split(" ")

# stopwords remove

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
 
#example_sent = """This is a sample sentence,
#                  showing off the stop words filtration."""
 
stop_words = set(stopwords.words('english'))
 
#word_tokens = word_tokenize(corpus_tokens)
word_tokens = corpus_tokens
#filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]
# with no lower case conversion
filtered_sentence = []
 
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)
 
# print(word_tokens)
# print(filtered_sentence)

corpus_without = filtered_sentence


# lemmatization
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
corpus_lemmatized = []
for w in corpus_without:
 w2 = lemmatizer.lemmatize(w)
 corpus_lemmatized.append(w2)


# count frequency stats

from collections import Counter, defaultdict

# wordlist = ['red', 'yellow', 'blue', 'red', 'green', 'blue', 'blue', 'yellow']
wordlist = corpus_lemmatized 
# invert a temporary Counter(wordlist) dictionary so keys are
# frequency of occurrence and values are lists the words encountered
freqword = defaultdict(list)
for word, freq in Counter(wordlist).items():
    freqword[freq].append(word)

# print in order of occurrence (with sorted list of words)
for freq in sorted(freqword):
    print('count {}: {}'.format(freq, sorted(freqword[freq])))

p1b = str(p1)
p1c = p1b.replace("txt","")
p2= p1c + "_bag_of_words_stats.txt"
corpus_stats = open( p2,"w")

for freq in sorted(freqword):
    corpus_stats.write('count {}: {}'.format(freq, sorted(freqword[freq]))+'\n')
