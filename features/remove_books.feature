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
        When Add "any book" by "any one" with id 1
        Then Bookstore has "some book" by "another author"

    Scenario Outline: Remove two books 
        Given An empty bookstore
        When Add "example book 1" by "author 1" with id 1
        And Add "example book 2" by "author 2" with id 2
        And Add "example book 3" by "author 3" with id 3
        Then Total books count is 3
        But Remove book with id 1
        But Remove book with id 3
        Then Total books count is 1
        And Bookstore has "example book 2" by "author 2"


