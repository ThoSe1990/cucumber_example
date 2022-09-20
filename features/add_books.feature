Feature: Add Books

    Scenario: Find added book 
        Given An empty bookstore
        When Add "a book" by "somebody" with id 123
        Then Bookstore has "a book" by "somebody"

    Scenario: Add books to an empty bookstore
        Given An empty bookstore
        When Add "a book" by "somebody" with id 123
        And Add "another book" by "another author" with id 456
        Then Total books count is 2

    Scenario: Initialize a bookstore with a json file
        Given A bookstore with following books
        """
            {
                "books": [
                    {
                        "id": "123456",
                        "author": "Buzz Michelangelo",
                        "title": "The Story Of Buzz Michelangelo"
                    },
                    {
                        "id": "456789",
                        "author": "Moxie Crimefighter",
                        "title": "How To Fight Crimes"
                    }
                ]
            }
        """
        Then Total books count is 2
        But Add "some other book" by "Jeff" with id 999
        Then Total books count is 3


    Scenario: This Scenario is tagged with foo 
        Given An empty bookstore
        When Add "foo" by "foo" with id 123
        Then Bookstore has "foo" by "foo"


    Scenario: This Scenario is tagged with foo and bar
        Given An empty bookstore
        When Add "foo" by "bar" with id 123
        Then Bookstore has "foo" by "bar"