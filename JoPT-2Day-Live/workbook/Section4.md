### 4. Foundations of Selenium WebDriver

- [Hands-On: Basic Browser Handling Using Python Selenium Client Bindings](#hands-on-basic-browser-handling-using-python-selenium-client-bindings)
- [Hands-On: Finding Elements using `driver.find_element` method](#hands-on-finding-elements-using-driverfind_element-method)
- [Hands-On: Dynamic Waiting and State Checking](#hands-on-dynamic-waiting-and-state-checking)
- [Hands-On: Entering Text](#hands-on-entering-text)
- [Defining a Class](#defining-a-class)
- [Hands-On: Create a Calculator Class](#hands-on-create-a-calculator-class)
- [Python `unittest`: TestCase Class, Test Methods, Fixtures and Assertions](#python-unittest-testcase-class-test-methods-fixtures-and-assertions)
- [Hands-On: A Sample Unit Test Class](#hands-on-a-sample-unit-test-class)
- [Long Exercise: Use unittest to implement valid and invalid login scenario.](#long-exercise-use-unittest-to-implement-valid-and-invalid-login-scenario)
  * [Tips and Inputs](#tips-and-inputs)
- [Walk-through of a Sample Solution](#walk-through-of-a-sample-solution)

### Hands-On: Basic Browser Handling Using Python Selenium Client Bindings

In continuation to the demo using ChromeDriver, we'll now automate the following steps using Selenium library:

ChromeDriver executable can be used to automate Chrome. As a part of this demonstrate to you the following steps:

1. Launch Chrome.
2. Go to https://www.google.com.
3. Find all HTML nodes with the tag input and print the source.
4. Quit Chrome.

Let's install selenium:

```
pip install selenium
```

To launch chrome:

```python
from selenium import webdriver
driver = webdriver.Chrome(executable_path=<path>)
```

We'll implement and use the function `get_driver_path` in `project_utils.py`.

To go to a url:

```python
driver.get('<url>')
```

For finding and printing source of all input nodes:

```python
matches = re.findall(r'(<input.*?>)', driver.page_source)
for match in matches:
    print(match)
```

For quitting Chrome:

```python
driver.quit()
```

Let's implement these steps in `ex17.py` file.

### Hands-On: Finding Elements using `driver.find_element` method

This step onwards, we'll use the WordPress application. You should use the ip address as per the lab machine allocated to you.

URL for admin interface is: `http://<ip address/wp-admin`.

For finding an element, you need to express it as a 'By' strategy. Following are some commonly used strategies:

```python
from selenium.webdriver.common.by import By
By.ID
By.NAME
By.XPATH
By.CSS_SELECTOR
```

Let's identify the user name field using all these strategies and implement in `ex18.py` file.

### Hands-On: Dynamic Waiting and State Checking

Many a times, the element is not ready to be interacted with and this leads to flaky tests.

A highly suggested approach is to use fluent/dynamic waiting for the desired state.

```python
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
wait = WebDriverWait(<driver_object>, <time>)
element = wait.until(EC.element_to_be_clickable((<by_type>, <by_value>))
```

Other usual conditions of interest are `presence_of_element_located` and `visibility_of_element_located`.

Notice that you have to pass, the `By` strategy and value as a `tuple` unlike `find_element` call where you passed them as individual arguments.

Let's implement this new style in `ex19.py` file.

### Hands-On: Entering Text

To enter some text in the text box, we can use `send_keys` method of `WebElement`. Optionally, you can also clear the text before entering anything.

```python
element.clear()
element.send_keys('<text>')
```

Let's enter `user` text in the user name text box in `ex19.py` file.

### Defining a Class

You can create a class in Python using the `class` keyword. It can contain any number of functions, which are mostly bound to a specific object/instance of a class and hence are called `bound methods` or simply `methods`.

The class names in Python are the only exception to naming and use the CamelCase style.

```python
class ClassName:

    def __init__(self):
        pass
        
    def method1(self, some_arg):
        pass
        
    def method2(self, some_arg2):
        pass
 ```
 
 A class acts as a template/blue-print to create any number of objects.

Note that in the definition of a function, you always pass `self` as the first argument (unless you are dealing with advanced method variants, not in scope of this workshop). This is a reference to the current object/instance and unlike most other languages is defined explicitly in Python.

Creating an object of this class is similar to a function call syntax:
 
 ```python
 cn = ClassName()
 ```
 
 Now, you can call the methods, as you called methods of pre-defined objects so far:
 
 ```python
 cn.method1(val1)
```

Note that while calling, the first argument `self` is automatically handled by Python's method call mechanism.

### Hands-On: Create a Calculator Class

Let's create a simple class `Calculator` with 3 methods `add` and `sub` and `reset`. For each calculation that it does, it increments a state attribute `calc_count`. Calling the `reset` methods, resets the value of `calc_count` to 0.

Write usage code in `ex20.py`.

### Python `unittest`: TestCase Class, Test Methods, Fixtures and Assertions

Selenium library is meant only for automating the UI of a web application. To write tests, you need a test engine. Python has a built-in unit test engine called `unittest`.

Steps:
1. Create a test class and inherit it from `unittest.TestCase`
2. Make a `super().__init__()` call to complete any necessary initization needed by the engine.
2. Implement any tests as test methods of this class. For this, the names of methods should be prefixed with `test`.
4. In the test methods, write validations by using `assertion` methods of the `TestCase` object.
5. Optionally, move set-up and clean-up instructions to `Test Fixture methods` at test-class-level (`setUpClass/tearDownClass`) or test-method-level (`setUp/tearDown`) (We'll explore test method level fixtures in this workshop).

### Hands-On: A Sample Unit Test Class

Let's write some unit tests for the Calculator class created in `calc.py` in `ex21.py`.

1. Write a test method for `add` method. 
2. Write a test method for `sub` method. 
3. Write a test method with multiple calls to `add` and `sub`.

Create the calculator instance in `setUp` if it does not exist. Reset the caluclator in `tearDown` method.

For each test, assert the output of a method call as well expected `calc_count` value.

There are multiple ways to run unit tests. One easy way of doing so is running the following command from terminal:

```
python -m unittest <test_script_path>
```

### Long Exercise: Use unittest to implement valid and invalid login scenario.

Implement the following test scenarios as test methods in a single test class in `ex22_login_tests.py` file.
1. Valid Login Test
2. Invalid Login Test

#### Tips and Inputs
1. User name is `user`, password is `bitnami`.
2. To click an element, you can call `click()` method of element.
3. To get the value of an attribute of an element, you can use `get_attribute` method call.
4. The link URL for a hyperlink in HTML is contained in its `href` attribute.

### Walk-through of a Sample Solution
Let's look at the details of a possible solution. Map to the way you approached the problem and take a note of any new learning or a different way of solving the same problem.
