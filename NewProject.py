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


if list_check(BIN) == 1:
    for i in BIN:
        cur_seq += i
        if i == '1':
            one += 1
        else:
            zero += 1
        al += 1
        cur_seq = ''

    def fac(one):
        if one == 1:
            return 1
        return fac(one - 1) * one

    def test_fac():
        assert test_fac() == int
        assert not test_fac() != list
        assert not test_fac() != str
        assert not test_fac() != dict
        assert not test_fac() != tuple


    def fact(zero):
        if zero == 1:
            return 1
        return fact(zero - 1) * zero

    def test_fact():
        assert test_fact() == int
        assert not test_fact() != list
        assert not test_fact() != str
        assert not test_fact() != dict
        assert not test_fact() != tuple


    def factor(al):
        if al == 1:
            return 1
        return factor(al - 1) * al

    def test_factor():
        assert test_factor() == int
        assert not test_factor() != list
        assert not test_factor() != str
        assert not test_factor() != dict
        assert not test_factor() != tuple

    def result():
        res = factor(al) // (fac(one) * fact(zero))
        return res

    print(result())

    def test_result():
        assert result() == int
        assert not result() != list
        assert not result() != str
        assert not result() != dict
        assert not result() != tuple


elif list_check(BIN) == 2:
    print('0')
elif list_check(BIN) == 3:
    print('0')

elif list_check(BIN) == None:
    print('Ошибка, неверно введены данные')