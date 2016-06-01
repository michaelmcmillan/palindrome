from log import Log
from sentence import Sentence

class Palindrome:
    
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
            if self.sentence.characters_are_equal(self.ordinary_index, self.opposite_index):
                self._increment_and_decrement_indexes()
            else:
                return False
        return True

    def is_valid(self):
        validness = self.sentence.is_valid() and self._is_sentence_symmetrical()
        Log.stdout('Checking if "%s" is a palindrome: %s' %
            (self.sentence.text, '✓' if validness else 'x'))
        return validness
