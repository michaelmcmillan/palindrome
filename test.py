from palindrome import Palindrome

assert Palindrome('amor roma').is_valid()
assert Palindrome('agnes i senga').is_valid()
assert Palindrome('A man, a plan, a canal, Panama!').is_valid()
assert Palindrome('No ‘x’ in Nixon').is_valid()
assert Palindrome('agnes i senga?').is_valid()
assert Palindrome('regninger').is_valid()
assert Palindrome('اااا').is_valid()
assert Palindrome('توت').is_valid() # toot in arabic

assert not Palindrome('agnes i sofa').is_valid()
assert not Palindrome('لheل').is_valid()
assert not Palindrome('h101hb').is_valid()
assert not Palindrome('False').is_valid()
