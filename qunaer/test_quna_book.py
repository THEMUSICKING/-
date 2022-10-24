import pytest

from qunaer.book_quna import *

def test_book_ticker():
    start = '北京'
    end = '上海'
    n = 2
    name = '金欢'
    id = '################'
    mobile = '#######'
    book_ticket(start, end, n, name, id, mobile)

if __name__ == '__main__':
    pytest.main(['-sv','test_quna_book.py'])
