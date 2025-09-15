import random
from wordmaker_func import *

##############################

rules = '''
'''
syllable_patterns = ['CVC', 'CV', 'VC', 'CCV', 'V']
seed = None

length = "short"
num_words = 10

##############################

if seed:
    random.seed(seed)

for i in range(num_words):
    syllable_length = pick_length(length)
    print(make_word(syllable_patterns, syllable_length))



