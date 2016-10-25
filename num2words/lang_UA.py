# -*- encoding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA
u"""
>>> from textwrap import fill

>>> ' '.join([str(i) for i in splitby3('1')])
u'1'
>>> ' '.join([str(i) for i in splitby3('1123')])
u'1 123'
>>> ' '.join([str(i) for i in splitby3('1234567890')])
u'1 234 567 890'

>>> print(' '.join([n2w(i) for i in range(10)]))
нуль один два три чотири п'ять шість сім вісім дев'ять

>>> print(fill(' '.join([n2w(i+10) for i in range(10)])))
десять одинадцять дванадцять тринадцять чотирнадцять п'ятнадцять
шістнадцять сімнадцять вісімнадцять дев'ятнадцять

>>> print(fill(' '.join([n2w(i*10) for i in range(10)])))
нуль десять двадцять тридцять сорок п'ятдесят шістдесят сімдесят
вісімдесят дев'яносто

>>> print(n2w(100))
сто
>>> print(n2w(101))
сто один
>>> print(n2w(110))
сто десять
>>> print(n2w(115))
сто п'ятнадцять
>>> print(n2w(123))
сто двадцять три
>>> print(n2w(1000))
тисяча
>>> print(n2w(1001))
тисяча один
>>> print(n2w(2012))
дві тисячі дванадцять

>>> print(n2w(12519.85))
дванадцять тисяч п'ятсот дев'ятнадцять кома восімдес'ят

>>> print(fill(n2w(1234567890)))
мільярд двісті тридцять чотири мільйони п'ятсот шістдесят сім тисяч
вісімсот дев'яносто

>>> print(fill(n2w(215461407892039002157189883901676)))
двісті п'ятнадцять нонілліонов чотири сотні шістдесят один октілліон
чотири сотні сім септілліонов вісімсот дев'яносто два секстильйонів
тридцять дев'ять квінтильйонів два квадрильйона сто п'ятдесят сім
трильйонів сто вісімдесят дев'ять мільярдів вісімсот вісімдесят три
мільйони дев'ятсот одна тисяча шістсот сімдесят шість

>>> print(fill(n2w(719094234693663034822824384220291)))
сімсот дев'ятнадцять нонілліонов дев'яносто чотири октілліона двісті
тридцять чотири септілліона шістсот дев'яносто три секстильйонів
шістсот шістдесят три квінтильйони тридцять чотири квадрильйона
вісімсот двадцять два трильйона вісімсот двадцять чотири мільярда
триста вісімдесят чотири мільйони двісті двадцять тисяч двісті
дев'яносто один

>>> print(to_currency(1.0, 'EUR'))
один євро, нуль центів

>>> print(to_currency(1.0, 'UAH'))
одна гривня, нуль копійок

>>> print(to_currency(1234.56, 'EUR'))
тисяча двісті тридцять чотири євро, п'ятдесят шість центів

>>> print(to_currency(1234.56, 'UAH'))
тисяча двісті тридцять чотири гривні, п'ятдесят шість копійок

>>> print(to_currency(10111, 'EUR', seperator=u' і'))
сто один євро і двадцять центів

>>> print(to_currency(10121, 'UAH', seperator=u' і'))
сто один гривня і двадцять одна копійка

>>> print(to_currency(10122, 'UAH', seperator=u' і'))
сто одна гривня і двадцять дві копійки

>>> print(to_currency(10121, 'EUR', seperator=u' і'))
сто один євро і двадцять один цент

>>> print(to_currency(-1251985, cents = False))
мінус дванадцять тисяч п'ятсот дев'ятнадцять євро, 85 центів

"""
from __future__ import unicode_literals

ZERO = (u'нуль',)

ONES_FEMININE = {
    1: (u'одна',),
    2: (u'дві',),
    3: (u'три',),
    4: (u'чотири',),
    5: (u'п\'ять',),
    6: (u'шість',),
    7: (u'сім',),
    8: (u'вісім',),
    9: (u'дев\'ять',),
}

ONES = {
    1: (u'один',),
    2: (u'два',),
    3: (u'три',),
    4: (u'чотири',),
    5: (u'п\'ять',),
    6: (u'шість',),
    7: (u'сім',),
    8: (u'вісім',),
    9: (u'дев\'ять',),
}

TENS = {
    0: (u'десять',),
    1: (u'одинадцять',),
    2: (u'дванадцять',),
    3: (u'тринадцять',),
    4: (u'четирнадцять',),
    5: (u'п\'ятнадцять',),
    6: (u'шістнадцять',),
    7: (u'сімнадцять',),
    8: (u'вісімнадцять',),
    9: (u'дев\'ятнадцять',),
}

TWENTIES = {
    2: (u'двадцять',),
    3: (u'тридцять',),
    4: (u'сорок',),
    5: (u'п\'ятдесят',),
    6: (u'шістдесят',),
    7: (u'сімдесят',),
    8: (u'вісімдесят',),
    9: (u'дев\'яносто',),
}

HUNDREDS = {
    1: (u'сто',),
    2: (u'двісті',),
    3: (u'триста',),
    4: (u'чотириста',),
    5: (u'п\'ятсот',),
    6: (u'шістсот',),
    7: (u'сімсот',),
    8: (u'вісімсот',),
    9: (u'дев\'ятсот',),
}

THOUSANDS = {
    1: (u'тисяча', u'тисячі', u'тисяч'), # 10^3
    2: (u'мільйон', u'мільйона', u'мільйонів'), # 10^6
    3: (u'мільярд', u'мільярда', u'мільярдів'), # 10^9
    4: (u'трильйон', u'трильйона', u'трильйонів'), # 10^12
    5: (u'квадрильйон', u'квадрильйона', u'квадрильйонів'), # 10^15
    6: (u'квінтильйон', u'квінтильйони', u'квінтильйонів'), # 10^18
    7: (u'секстильйон', u'секстильйона', u'секстильйонів'), # 10^21
    8: (u'септілліон', u'септілліона', u'септілліонов'), # 10^24
    9: (u'октілліон', u'октілліона', u'октілліонов'), #10^27
    10: (u'нонілліон', u'нонілліона', u'нонілліонов'), # 10^30
}

CURRENCIES = {
    'UAH': (
        (u'гривня', u'гривні', u'гривень'), (u'копійка', u'копійки', u'копійок')
    ),
    'EUR': (
        (u'евро', u'евро', u'евро'), (u'цент', u'цента', u'центов')
    ),
    'RUB': (
        (u'рубль', u'рубля', u'рублей'), (u'копейка', u'копейки', u'копеек')
    ),
    'USD': (
        (u'долар', u'долара', u'доларів'), (u'цент', u'цента', u'центів')
    ),
}


def splitby3(n):
    length = len(n)
    if length > 3:
        start = length % 3
        if start > 0:
            yield int(n[:start])
        for i in range(start, length, 3):
            yield int(n[i:i+3])
    else:
        yield int(n)


def get_digits(n):
    return [int(x) for x in reversed(list(('%03d' % n)[-3:]))]


def pluralize(n, forms):
    if (n % 100 < 10 or n % 100 > 20):
        if n % 10 == 1:
            form = 0
        elif (n % 10 > 1 and n % 10 < 5):
            form = 1
        else:
            form = 2
    else:
        form = 2
    return forms[form]


def int2word(n, feminine=False):
    if n < 0:
        return ' '.join([u'мінус', int2word(abs(n))])

    if n == 0:
        return ZERO[0]

    words = []
    chunks = list(splitby3(str(n)))
    i = len(chunks)
    for x in chunks:
        i -= 1
        n1, n2, n3 = get_digits(x)

        if n3 > 0:
            words.append(HUNDREDS[n3][0])
            
        if n2 > 1:
            words.append(TWENTIES[n2][0])

        if n2 == 1:
            words.append(TENS[n1][0])
        elif n1 > 0 and not (i > 0 and x == 1):
            ones = ONES_FEMININE if i == 1 or feminine and i == 0 else ONES
            words.append(ones[n1][0])

        if i > 0:
            words.append(pluralize(x, THOUSANDS[i]))

    return ' '.join(words)


def n2w(n):
    n = str(n).replace(',', '.')
    if '.' in n:
        left, right = n.split('.')
        return u'%s кома %s' % (int2word(int(left)), int2word(int(right)))
    else:
        return int2word(int(n))


def to_currency(n, currency='USD', cents=True, seperator=','):
    if type(n) == int:
        if n < 0:
            minus = True
        else:
            minus = False

        n = abs(n)
        left = n / 100
        right = n % 100
    else:
        n = str(n).replace(',', '.')
        if '.' in n:
            left, right = n.split('.')
        else:
            left, right = n, 0
        left, right = int(left), int(right)
        minus = False
    cr1, cr2 = CURRENCIES[currency]

    if minus:
        minus_str = "мінус "
    else:
        minus_str = ""

    if cents:
        cents_feminine = currency == 'UAH'
        cents_str = int2word(right, cents_feminine)
    else:
        cents_str = "%02d" % right

    return u'%s%s %s%s %s %s' % (
        minus_str,
        int2word(left),
        pluralize(left, cr1),
        seperator,
        cents_str,
        pluralize(right, cr2)
    )


class Num2Word_UA(object):
    def to_cardinal(self, number):
        return n2w(number)

    def to_ordinal(self, number):
        raise NotImplementedError()

    def to_currency(self, number, longval=True, currency='USD', cents=True, seperator=','):
        return to_currency(number, currency=currency, cents=cents, seperator=seperator)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
