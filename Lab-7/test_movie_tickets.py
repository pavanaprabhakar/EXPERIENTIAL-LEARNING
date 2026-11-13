
from hypothesis import given, strategies as st
from movie_tickets import parse_seat, total_price, average_rating


@given(st.one_of(st.text(), st.none()))
def test_parse_seat_no_crash(s):
    try:
        parse_seat(s)
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none()))
def test_total_price_no_crash(s):
    try:
        total_price(s)
    except ValueError:
        pass


@given(st.one_of(st.text(), st.none()))
def test_average_rating_no_crash(s):
    try:
        average_rating(s)
    except ValueError:
        pass
