# https://opensource.org/license/mit/
#
# Copyright 2023 resurtm@gmail.com
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
# documentation files (the “Software”), to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all copies or substantial
# portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
# TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

from typing import Collection, Final


def solve(elems: Collection[int], k: int) -> bool:
    for i, a in enumerate(elems):
        for j, b in enumerate(elems):
            if i == j:
                continue
            if a + b == k:
                return True
    return False


def solve_one_pass(elems: Collection[int], k: int) -> bool:
    accum: Final[set[int]] = set()
    for a in elems:
        if a in accum:
            return True
        accum.add(k - a)
    return False


if __name__ == "__main__":
    items: Final = [10, 15, 3, 7]

    # multi pass
    assert not solve(items, 20)
    assert solve(items, 17)
    assert not solve(items, 16)

    # single pass
    assert not solve_one_pass(items, 20)
    assert solve_one_pass(items, 17)
    assert not solve_one_pass(items, 16)
