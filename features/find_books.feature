Feature: Find Books
 
    Scenario: Find Foo
        Given An empty bookstore
        When Add "foo" by "foo" with id 123
        Then Bookstore has "foo" by "foo"

    Scenario: Find Bar
        Given An empty bookstore
        When Add "foo" by "bar" with id 123
        Then Bookstore has "foo" by "bar"

    Scenario: Undefined Step 				
        Given This isn't implemented 
        