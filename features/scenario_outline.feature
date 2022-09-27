Feature: scenario outline here 
    
    Scenario Outline: Adding multiple books with scenario outline
        Given An empty bookstore
        When Add "<book>" by "<author>" with id <id>
        Then Total books count is 1
        And Bookstore has "<book>" by "<author>"

        Examples:
        | book           | author   | id |
        | example book 1 | author 1 | 1  |
        | example book 2 | author 2 | 2  |
        | example book 3 | author 3 | 3  |
        | example book 4 | author 4 | 4  |
