BIN = str(input('Введите последовательность "0" и "1" '))
print(set(BIN))
cur_seq = ''
s = {'0', '1'}
one = 0
zero = 0
al = 0
fac_one = 1
fac_zero = 1
fac_al = 1
def list_check(BIN):
    if set(BIN) == s:
        return 1
    elif set(BIN) == {'1'}:
        return 2
    elif set(BIN) == {'0'}:
        return 3

def test_list_check():
    assert list_check('01')
    assert list_check('10')
    assert list_check('0')
    assert list_check('1')
    assert not list_check('light_sun ')
    assert not list_check('5140')
    assert not list_check('?/><;:#№@$%&*_-=+')
