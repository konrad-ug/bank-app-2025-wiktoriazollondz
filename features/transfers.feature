Feature: Money transfers

Scenario: User can transfer money between accounts
    Given Account registry is empty
    And I create an account using name: "Adam", last name: "Z", pesel: "11111111111"
    And I create an account using name: "Ewa", last name: "X", pesel: "22222222222"
    When I transfer "200" from account "000" to "11111111111"
    And I transfer "100" from account "11111111111" to "22222222222"
    Then Account with pesel "11111111111" has balance equal to "100"
    And Account with pesel "22222222222" has balance equal to "100"