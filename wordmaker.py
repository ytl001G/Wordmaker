import random
from wordmaker_func import *

rules = '''
consonants p, b, t, d, k, g, m, n, s, z, f, v, l, r

start a
end s
'''
syllable_patterns = ['CVC', 'CV', 'VC', 'CCV', 'V']
seed = 42

length = "short"
num_words = 20

##############################

if seed:
    random.seed(seed)

interpret_rules(rules)

for i in range(num_words):
    syllable_length = pick_length(length)
    print(make_word(syllable_patterns, syllable_length))



