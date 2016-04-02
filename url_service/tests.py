from nose.tools import eq_
from mock import patch
from .helpers import is_valid_URL

def test_is_valid_URL():
	eq_(is_valid_URL("facebook"), False)
	eq_(is_valid_URL("facebook.com"), False)
	eq_(is_valid_URL("www.facebook.com"), False)
	eq_(is_valid_URL("http://www.facebook.com"), True)
