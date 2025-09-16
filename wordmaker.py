import random
from wordmaker_func import *

rules = '''
C = p b t d k g m n s z f v l r
V = a e i o u

start pu
end m

length 2..4

syllable CV VC V
'''
seed = 42

num_words = 20

##############################

if seed:
    random.seed(seed)

interpret_rules(rules)

for i in range(num_words):
    print(make_word())



