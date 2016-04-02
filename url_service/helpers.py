from django.core.validators import URLValidator
from django.core.exceptions import ValidationError
from django.http import HttpResponse

import random, string

def is_valid_URL(a_url):
	validate = URLValidator()
	try:
		validate(a_url)
	except ValidationError:
		return False
	else:
		return True

def generate_random_string():
	LENGTH_OF_FINAL_STRING = 6
	randomizer = random.SystemRandom()
	character_set = string.ascii_uppercase + string.ascii_lowercase + string.digits
	return ''.join(randomizer.choice(character_set) for x in range(LENGTH_OF_FINAL_STRING))


