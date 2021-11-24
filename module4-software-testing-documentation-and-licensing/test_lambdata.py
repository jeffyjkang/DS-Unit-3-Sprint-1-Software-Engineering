'''
Basic Unit Tests for Lambdata package
'''

# def inc(x):
#     return x + 2

# def test_inc():
#     ans = inc(3)
#     assert ans == 5

from random import randint
import pytest
import test as ld
from test.oop_example import SocialMediaUser

# testing __init__
def test_increment():
    # Make sure increment works for int
    x0 = 0
    y0 = ld.increment(x0) # 1
    assert y0 == 1

    x1 = 100
    y1 = ld.increment(x1) # 101
    assert y1 == 101

def test_increment_float():
    # Make sure increment works for floats
    x0 = 10.5
    y0 = ld.increment(x0) # 11.5
    assert y0 == 11.5

def test_increment_neg_int():
    # Make sure increment works for neg int
    x0 = -1
    y0 = ld.increment(x0) # 0
    assert y0 == 0

def test_increment_neg_float():
    # Make sure increment works for neg floats
    x0 = -1.5
    y0 = ld.increment(x0) # -0.5
    assert y0 == -0.5

def test_colors():
    # Testing that colors contains correct items
    assert 'Cyan' in ld.COLORS
    assert 'Mauve' in ld.COLORS
    assert 'Blue' in ld.COLORS
    assert 'Brown' not in ld.COLORS

def test_number_colors():
    # Testing the number of elements in colors
    assert len(ld.COLORS) == 4

# testing oop

user1 = ld.oop_example.SocialMediaUser(name='John', location='AZ')
user2 = ld.oop_example.SocialMediaUser(name='Mike', location='KC', upvotes=250)

def test_SMU_constructor():
    # testing that name works properly
    assert user1.name == 'John'
    assert user2.name == 'Mike'
    # testing location
    assert user1.location == 'AZ'
    assert user2.location == 'KC'
    # testing upvotes
    assert user1.upvotes == 0 # default
    assert user2.upvotes == 250

def test_popularity():
    # test > 100 popular
    assert isinstance(user1.is_popular(), bool)
    assert not user1.is_popular()
    assert isinstance(user2.is_popular(), bool)
    assert user2.is_popular()

def test_SMU_constructor_types():
    # testing types
    assert isinstance(user1.name, str)
    assert isinstance(user2.location, str)
    assert isinstance(user1.upvotes, int)