from django.test import TestCase

_test_case = TestCase()

assert_contains = _test_case.assertContains  # método não está seguindo a PEP8. Deveria ser snakecase.
