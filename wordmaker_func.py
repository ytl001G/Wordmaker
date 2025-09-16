import random
import re
from dataclasses import dataclass

@dataclass
class Phoneme:
    value: str

    def __add__(self, other):
        """두 Phoneme을 더하면 문자열 결합"""
        if isinstance(other, Phoneme):
            return Phoneme(self.value + other.value)
        elif isinstance(other, str):
            return Phoneme(self.value + other)
        else:
            raise TypeError("Phoneme + Phoneme 또는 Phoneme + str만 가능합니다.")
        
    def __radd__(self, other):
        """str + Phoneme"""
        if isinstance(other, str):
            return Phoneme(other + self.value)
        else:
            raise TypeError("str + Phoneme만 가능합니다.")

    def __str__(self):
        """print() 호출 시 value 출력"""
        return self.value

    def __repr__(self):
        return f"Phoneme('{self.value}')"

# {C:[], V:[] ...}
characters = {}

prefix: list[str] = []
suffix: list[str] = []

syllables: list[str] = []

length: list[int] = []

def interpret_rules(rules: str):
    for line in rules.splitlines():
        if not line.strip():
            continue

        if line.startswith("start"):
            prefix.append(line.split()[1])
            continue

        if line.startswith("end"):
            suffix.append(line.split()[1])
            continue

        if line.startswith("syllable"):
            syllables.extend(line.split()[1:])
            continue

        if line.startswith("length"):
            global length
            length = list(map(int, re.findall(r'\d+', line)))

        if re.match(r'^[A-Za-z]+\s=', line):
            lable = re.match(r'^[A-Za-z]+', line).group()
            right = line.split("=", 1)[1].strip()
            labled_characters = right.split()
            characters[lable] = labled_characters
            continue

def pick_syllable(syllable):
    return_syllable = ""
    for char in syllable:
        return_syllable += random.choice(characters[char])
    
    return return_syllable

def make_word():
    return_word = ""
    word_length = random.randint(length[0], length[1])
    for _ in range(word_length):
        syllable_type = random.choice(syllables)
        return_word += pick_syllable(syllable_type)

    if prefix:
        return_word = random.choice(prefix) + return_word

    if suffix:
        return_word = return_word + random.choice(suffix) 
    return return_word