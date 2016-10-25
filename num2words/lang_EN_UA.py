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

from __future__ import unicode_literals
from .lang_EN import Num2Word_EN


class Num2Word_EN_UA(Num2Word_EN):

    def to_splitnum(self, val, hightxt="", lowtxt="", jointxt="",
                    divisor=100, longval=True, cents=True):
        out = []
        try:
            high, low = val
        except TypeError:
            high, low = divmod(val, divisor)
        if high:
            hightxt = self.title(self.inflect(high, hightxt))
            out.append(self.to_cardinal(high))
            if hightxt:
                out.append('United State')
                out.append(hightxt)
            if jointxt:
                out.append(self.title(jointxt))
        if cents:
            out.append(self.to_cardinal(low))
        else:
            out.append("%02d" % low)
        if lowtxt and longval:
            out.append(self.title(self.inflect(low, lowtxt)))
        return " ".join(out)

    def merge(self, (ltext, lnum), (rtext, rnum)):
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum :
            return ("%s-%s"%(ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            return ("%s %s"%(ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return ("%s %s"%(ltext, rtext), lnum * rnum)
        return ("%s, %s"%(ltext, rtext), lnum + rnum)

    def to_currency(self, val, longval=True, **kwargs):
        jointxt = kwargs.get('seperator', 'and')
        cents = kwargs.get('cents', True)
        return self.to_splitnum(val, hightxt="dollar/s", lowtxt="cent/s",
                                jointxt=jointxt, longval=longval, cents=cents)


n2w = Num2Word_EN_UA()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num
to_year = n2w.to_year


def main():
    for val in [1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
                180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
                8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
                -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)
    n2w.test(
        1325325436067876801768700107601001012212132143210473207540327057320957032975032975093275093275093270957329057320975093272950730)
    for val in [1, 120, 1000, 1120, 1800, 1976, 2000, 2010, 2099, 2171]:
        print val, "is", n2w.to_currency(val)
        print val, "is", n2w.to_year(val)


if __name__ == "__main__":
    main()
