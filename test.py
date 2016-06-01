import timeit
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

try:
    Palindrome(['a', 'm', 'm', 'a']).is_valid()
except TypeError as error:
    assert True
else:
    assert False

timing_test = 'Palindrome("Are we not pure? “No sir!” Panama’s moody Noriega brags. “It is garbage!” Irony dooms a man; a prisoner up to new era.").is_valid()'
timeit.timeit(timing_test, 'from palindrome import Palindrome', number=1000)
