
import pytest
from movie_tickets import ticket_price, group_discount, snack_combo


# ---------------- TICKET PRICE TESTS ----------------

def test_invalid_seat():
    with pytest.raises(ValueError):
        ticket_price("luxury", 25, 15, False)


def test_invalid_show_time_negative():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, -1, False)


def test_invalid_show_time_above_23():
    with pytest.raises(ValueError):
        ticket_price("regular", 25, 24, False)


def test_morning_show():
    assert ticket_price("regular", 25, 10, False) == 100


def test_afternoon_show():
    assert ticket_price("regular", 25, 15, False) == 150


def test_evening_weekend_show():
    assert ticket_price("premium", 25, 18, True) == 320


def test_child_below_three():
    assert ticket_price("regular", 2, 15, False) == 0


def test_child_discount():
    assert ticket_price("regular", 12, 15, True) == 95


def test_normal_adult():
    assert ticket_price("regular", 25, 15, False) == 150


def test_senior_citizen_discount():
    assert ticket_price("regular", 60, 15, False) == 75


# ---------------- GROUP DISCOUNT TESTS ----------------

def test_no_tickets():
    with pytest.raises(ValueError):
        group_discount(0, False)


def test_small_group():
    assert group_discount(2, False) == 0


def test_student_small_group():
    assert group_discount(2, True) == 0


def test_medium_group():
    assert group_discount(5, False) == 10


def test_student_medium_group():
    assert group_discount(5, True) == 15


def test_large_group():
    assert group_discount(10, False) == 15


def test_student_large_group():
    assert group_discount(10, True) == 20


# ---------------- SNACK COMBO TESTS ----------------

def test_small_snack():
    assert snack_combo("small", False) == 120


def test_medium_snack():
    assert snack_combo("medium", False) == 180


def test_large_snack():
    assert snack_combo("large", False) == 250


def test_small_snack_coupon():
    assert snack_combo("small", True) == 70


def test_medium_snack_coupon():
    assert snack_combo("medium", True) == 130


def test_large_snack_coupon():
    assert snack_combo("large", True) == 200
