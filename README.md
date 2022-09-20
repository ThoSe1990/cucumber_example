[![Build Status](https://dev.azure.com/thomassedlmair/cucumber_example/_apis/build/status/ThoSe1990.cucumber_example?branchName=main)](https://dev.azure.com/thomassedlmair/cucumber_example/_build/latest?definitionId=12&branchName=main)

# Coding With Thomas: Cucumber Example

Find the corresponding Blog post here: https://www.codingwiththomas.com/blog/start-using-cucumber

To build and run this example please install all needed dependencies.  

This installation guide refers to an Ubuntu systems. In general I use a docker container to build and run my cucumber tests. The cucumber development libs need boost and if you don't have already boost in your project then it's quite an effort to install boost under windows. However, you can download Ruby from here: https://rubyinstaller.org/downloads/ and then use `gem install cucumber` from the terminal (Find for instance this installation guide for Windows: https://www.guru99.com/cucumber-installation.html)

## Cucumber And It's Dependencies

Moved to conan build. Since there is no cucumber recipe on conancenter or bincrafters, I provide this conanfile which worked for me in combination with gtest. I only tried it with msvc on windows and gcc on ubuntu. To create the conan package on your local machine run: 

```
conan create .\conanfile\cucumber-cpp\conanfile.py cucumber-cpp/0.5@cwt/stable --build missing
```

After the package was created the project can be built with: 

```
conan install . -if build --build missing
cmake -S . -B ./build 
cmake --build ./build (--config Debug/Release # for msvc builds...)
```


### Run 

Start our test executable in the background using `&` (or I start usually the executable in debug on my machine).
```
./build/bin/cucumer_example  &
```

Navigate into `./src/cucumber` and run cucumber with your feature files (placeholders with `*` are allowed here).   
I don't know why, but I don't get cucumber to run from the project root directory.
```
cd ./src/cucumber
cucumber ./features/example.feature
```

Which brings then the folloing output:
```
Feature: Example tests for a bookstore api

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

  @foo
  Scenario: This Scenario is tagged with foo
    Given An empty bookstore
    When Add "foo" by "foo" with id 123
    Then Bookstore has "foo" by "foo"

  @foo @bar
  Scenario: This Scenario is tagged with foo and bar
    Given An empty bookstore
    When Add "foo" by "bar" with id 123
    Then Bookstore has "foo" by "bar"

9 scenarios (9 passed)
33 steps (33 passed)
```