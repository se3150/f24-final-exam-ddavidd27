Feature: encode or decode a secret message
As a secret spy
I should be able to encode and decode messages
So that I can chat with my spy friends like a pro.

Scenario: I can successfully encode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    # write your steps here
    When I input the text "David is going to get an A" in the input field
    And I set the shift to "2"
    And I click the "Encode" button
    Then I should see the encoded message "Fcxkf ku iqkpi vq igv cp C"

Scenario: I can successfully decode a secret message
    Given I open the url "https://www.hanginghyena.com/solvers_a/caesar-cipher-decoder"
    # write your steps here
    When I input the text "Fcxkf ku iqkpi vq igv cp C" in the input field
    And I set the shift to "2"
    And I set the mode to "Decode"
    And I click the "Translate Message!" button
    Then I should see the message "David is going to get an A"
