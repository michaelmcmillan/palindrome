import timeit
from palindrome import Palindrome
from unittest import TestCase, main

class TestPalindrome(TestCase):

    def test_is_valid_if_symmetric(self):
        assert Palindrome('amor roma').is_valid()

    def test_is_invalid_if_not_symmetric(self):
        assert not Palindrome('ramor romaa').is_valid()

    def test_is_valid_regardless_of_casing(self):
        assert Palindrome('Amor Roma').is_valid()

    def test_is_valid_as_it_ignores_non_alphabetical_characters(self):
        assert Palindrome('No ‘x’ in Nixon').is_valid()

    def test_is_valid_even_if_arabic(self):
        assert Palindrome('توت').is_valid() # toot in arabic

    def test_is_invalid_if_empty_string(self):
        assert not Palindrome('').is_valid()

    def test_remembers_valid_palindromes_in_cache(self):
        Palindrome('this goes in the cache ehcac eht ni seog siht').is_valid()
        assert Palindrome.cache['thisgoesinthecacheehcacehtniseogsiht'] == True

    def test_remembers_invalid_palindromes_in_cache(self):
        Palindrome('this also goes in the cache').is_valid()
        assert Palindrome.cache['thisalsogoesinthecache'] == False

    def test_raises_type_error_if_non_string_is_supplied(self):
        with self.assertRaises(TypeError):
            Palindrome(['a', 'm', 'm', 'a']).is_valid()

    def test_it_is_fast(self):
        timing_test = 'Palindrome("Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era.").is_valid()'
        timeit.timeit(timing_test, 'from palindrome import Palindrome', number=1000)

if __name__ == '__main__':
    main(buffer=True)
