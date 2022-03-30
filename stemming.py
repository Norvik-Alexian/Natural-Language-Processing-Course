from nltk.stem.porter import PorterStemmer
from nltk.stem.snowball import SnowballStemmer

p_stemmer = PorterStemmer()

words = ['run', 'runner', 'ran', 'runs', 'easily', 'fairly', 'fairness', 'generous', 'generation', 'generously', 'generate']


for word in words:
    print(f'{word} --------> {p_stemmer.stem(word)}')

print('\n' * 2)
s_stemmer = SnowballStemmer(language='english')

for word in words:
    print(f'{word} -----> {s_stemmer.stem(word)}')
