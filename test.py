from main import countvowels, is_palindrome, get_positives, get_negatives, get_average

# Test 1
def test_countvowels_simple():
    assert countvowels("hello") == 2

# Test 2
def test_countvowels_uppercase():
    assert countvowels("EduCaTiOn") == 5

# Test 3
def test_is_palindrome_true():
    assert is_palindrome("reconocer") == True

# Test 4
def test_is_palindrome_false():
    assert is_palindrome("python") == False

# Test 5
def test_get_positives_mixed():
    assert get_positives([-2, 0, 4, 6, -9]) == [4, 6]

# Test 6
def test_get_negatives_mixed():
    assert get_negatives([-2, 0, 4, -6]) == [-2, -6]

# Test 7
def test_get_average_normal():
    assert get_average([2, 4, 6]) == 4.0

# Test 8
def test_get_average_empty():
    assert get_average([]) == 0.0
