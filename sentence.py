class Sentence:

    def __init__(self, text):
        if not isinstance(text, str):
            raise TypeError
        self.text = self._remove_unimportant_characters(text)
        self.length = len(self.text)

    def is_valid(self):
        return self.text != ''

    def _remove_unimportant_characters(self, text):
        text_without_unimportant_characters = ''
        for character in text:
            if character.isalpha():
                text_without_unimportant_characters += character
        return text_without_unimportant_characters

    def characters_are_equal(self, first_index, second_index):
        return self.text[first_index].lower() == self.text[second_index].lower()
