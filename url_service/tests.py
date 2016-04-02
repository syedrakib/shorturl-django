from nose.tools import eq_
from mock import patch
from .helpers import is_valid_URL, generate_random_string
import re

def test_is_valid_URL():
	eq_(is_valid_URL("facebook"), False)
	eq_(is_valid_URL("facebook.com"), False)
	eq_(is_valid_URL("www.facebook.com"), False)
	eq_(is_valid_URL("http://www.facebook.com"), True)

def test_generate_random_string():
	eq_(len(re.findall('[^a-zA-Z0-9]', generate_random_string())) == 0, True)
