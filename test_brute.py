import pytest
from brute import Brute
from unittest.mock import Mock
import string

todo = pytest.mark.skip(reason='todo: pending spec')

def describe_Brute():

    @pytest.fixture
    def cracker():
        return Brute("TDD")

    def describe_bruteOnce():

        def it_returns_true_when_attempt_matches_target(cracker):
            #bruteOnce returns True when the input matches
            assert cracker.bruteOnce("TDD") is True

        def it_returns_false_when_attempt_does_not_match_target(cracker):
            #bruteOnce returns False when the input does not match
            assert cracker.bruteOnce("wrong") is False

    def describe_bruteMany():

        @pytest.fixture
        def mock_cracker(mocker):
            #create a mocked Brute instance with patched randomGuess method
            mock_brute = Brute("TDD")
            mocker.patch.object(mock_brute, 'randomGuess', side_effect=["TDD", "wrong"])
            return mock_brute
        
        def it_returns_time_to_crack_when_successful(mock_cracker):
            #bruteMany returns the time taken
            time_taken = mock_cracker.bruteMany(limit=10)
            assert time_taken > 0
        
        def it_returns_negative_one_when_unsuccessful(mocker):
            #bruteMany returns -1 if the secret is not cracked in time 
            mock_brute = Brute("TDD")
            mocker.patch.object(mock_brute, 'randomGuess', return_value="wrong")
            result = mock_brute.bruteMany(limit=10)
            assert result == -1
    
        def it_verifies_bruteOnce_is_called(mock_cracker, mocker):
            mock_brute_once = mocker.patch.object(mock_cracker, 'bruteOnce', return_value=True)
            mock_cracker.bruteMany(limit=1)
            mock_brute_once.assert_called_with("TDD")

    #Had to add this due to the coverage report
    def describe_randomGuess():

        def it_generates_a_string_within_the_expected_length_range(cracker):
            #Ensures randomGuess generates a string of length between 1 and 8
            guess = cracker.randomGuess()
            assert 1 <= len(guess) <= 8

        def it_generates_strings_with_valid_characters(cracker):
            #Ensures randomGuess generates strings containing only valid characters
            guess = cracker.randomGuess()
            valid_characters = string.ascii_letters + string.digits
            assert all(char in valid_characters for char in guess)

