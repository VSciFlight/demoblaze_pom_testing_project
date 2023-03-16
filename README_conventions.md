# selenium_team_3
selenium_team_3: Alon, Eliav, Artium, Nir


File conventions:

* A docstring ("""text""") should be after every decleration of functions and classes
* A comment should appear besides loops and variables describing their
* NO IF NESTING ABOVE 2. Means you do not nest if statements more than two times.

utils.py includes the whole external imports for the projects

FUNCTIONS:
  - small letters
  - spaces replaces with underscores ("_")
  - test functions must start with "test_"
  
CLASS:
  - Camel Case. for example BaseHomePage
  - no spaces
  - test classes must start with the word "test_"
  

Packages:
  - Selenium
  - Requests
  - unittest



 TEST SUITE
 Test Suite is defined by a class in a file.
 Test Case is defined as a function within the Test Suite
 
 for example:
```
    class TestStocks:
      def test_stock_price():
        <code>
      
      def test_stock_value():
        <code>
```
* TestStocks - a test suite (class)
* test_stock_price - a test case (function)
* test_stock_value - a test case (function)
