from lib.album_parameters_validator import AlbumParametersValidator

"""
With a valid title and a year
It is valid
"""

def test_is_valid():
    validator = AlbumParametersValidator("My Title", "1990")
    assert validator.is_valid() == True

"""
With a blank or None title
It is not valid
"""

def test_is_not_valid_title():
    validator_1 = AlbumParametersValidator("", "1990")
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator(None, "1990")
    assert validator_2.is_valid() == False

"""
With an blank or None release year
It is not valid
"""

def test_is_not_valid_title():
    validator_1 = AlbumParametersValidator("My Title", None)
    assert validator_1.is_valid() == False
    validator_2 = AlbumParametersValidator("My Title", "")
    assert validator_2.is_valid() == False

"""
With invalid parameters
Produces errors
"""

def test_generate_errors():
    validator_1 = AlbumParametersValidator("", "")
    assert validator_1.generate_errors() == "Title can't be blank, Release year can't be blank"