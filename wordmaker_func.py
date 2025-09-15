import random
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

@dataclass
class Consonant(Phoneme):
    voiced: bool
    type = "consonant"

class Vowel(Phoneme):
    type = "vowel"

class Glide(Phoneme):
    type = "glide"

consonants = [
    Consonant("p", False),
    Consonant("b", True),
    Consonant("t", False),
    Consonant("d", True),
    Consonant("k", False),
    Consonant("g", True),
    Consonant("m", True),
    Consonant("n", True),
    Consonant("s", False),
    Consonant("z", True),
    Consonant("f", False),
    Consonant("v", True),
    Consonant("l", True),
    Consonant("r", True)
]

vowels = [
    Vowel("a"),
    Vowel("e"),
    Vowel("i"),
    Vowel("o"),
    Vowel("u"),
    # Vowel("æ"),
    # Vowel("ø"),
    # Vowel("y")
]

glides = [
    Glide("j"),
    Glide("w")
]

lengths = ["short", "medium", "long"]
length_distributions = {
    "short": {1: 0.3, 2: 0.6, 3: 0.1},
    "medium": {4: 0.4, 5: 0.4, 6: 0.2},
    "long": {7: 0.5, 8: 0.3, 9: 0.2}
}

def pick_length(category: str) -> int:
    """범주 이름을 받아서 해당 길이 분포에서 길이를 하나 선택"""
    distrib = length_distributions[category]
    items = list(distrib.keys())
    weights = list(distrib.values())
    return random.choices(items, weights=weights, k=1)[0]

def pick_syllable(syllable: str):
    return_syllable = ""
    for char in syllable:
        if char == 'C':
            return_syllable += random.choice(consonants)
        if char == "V":
            return_syllable += random.choice(vowels)
        if char == "G":
            return_syllable += random.choice(glides)
    
    return return_syllable

def make_word(syllables: list, length: int):
    return_word = ""
    for _ in range(length):
        syllable_type = random.choice(syllables)
        return_word += pick_syllable(syllable_type)

    return return_word