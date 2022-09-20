Feature: Remove Books

    Scenario: Remove one book 
        Given An empty bookstore
        When Add "a book" by "somebody" with id 123
        And Add "another book" by "another author" with id 456
        Then Total books count is 2
        But Remove book with id 123
        Then Total books count is 1

    Scenario: Remove all books 
        Given An empty bookstore
        When Add "a book" by "somebody" with id 123
        And Add "another book" by "another author" with id 456
        Then Total books count is 2
        But Remove all books
        Then Total books count is 0

    Scenario Outline: This will fail
        Given An empty bookstore
        When Add "any book" by "any one" with id <id>
        Then Bookstore has "some book" by "another author"

    Scenario Outline: Adding multiple books with scenario outline
        Given An empty bookstore
        When Add "example book 1" by "author 1" with id <id>
        And Add "example book 2" by "author 2" with id <id>
        And Add "example book 3" by "author 3" with id <id>
        Then Total books count is 3
        And Bookstore has "example book 1" by "author 1"
        And Bookstore has "example book 2" by "author 2"
        And Bookstore has "example book 3" by "author 3"


