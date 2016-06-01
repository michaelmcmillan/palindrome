from log import Log
from sentence import Sentence

class Palindrome:

    cache = {}

    def __init__(self, text):
        self.sentence = Sentence(text)
        self.ordinary_index = 0
        self.opposite_index = self.sentence.length - 1
        self.half_way_index = round(self.sentence.length / 2)

    def _increment_and_decrement_indexes(self):
        self.ordinary_index += 1
        self.opposite_index -= 1

    def _is_sentence_symmetrical(self):
        while self.ordinary_index < self.half_way_index:
            if not self.sentence.characters_are_equal(self.ordinary_index, self.opposite_index):
                return False
            self._increment_and_decrement_indexes();
        return True

    def is_valid(self):
        Log.stdout('Checking if "%s" is a palindrome.' % self.sentence.text)
        if self.sentence in self.cache:
            Log.stdout('Hit the cache.')
            return self.cache[self.sentence]
        else:
            Log.stdout('Missed the cache.')
            valid = self.sentence.is_valid() and self._is_sentence_symmetrical()
            self.cache[self.sentence.text] = valid
            return valid
