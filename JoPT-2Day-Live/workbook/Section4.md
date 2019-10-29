### 4. Foundations of Selenium WebDriver

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

```
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

```
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

### Writing a Simple Python Class



### Python unittest - Test Class, Test Methods, Fixtures and Assertions

Selenium library is meant only for automating the UI of a web application. To write tests, you need a test engine. Python has a built-in unit test engine called `unittest`.

Steps:
1. Create a test class and inherit it from `unittest.TestCase`
2. Make a `super().__init__()` call to complete any necessary initization needed by the engine.
2. Implement any tests as test methods of this class. For this, the names of methods should be prefixed with `test`.
4. In the test methods, write validations by using `assertion` methods of the `TestCase` object.
5. Optionally, move set-up and clean-up instructions to `Test Fixture methods` at test-class-level (`setUpClass/tearDownClass`) or test-method-level (`setUp/tearDown`) (We'll explore test method level fixtures in this workshop).

### Hands-On: A Sample Unit Test Class

Let's write some unit tests for the Calculator class found in `calc.py`.

### Long Exercise: Use unittest to implement valid and invalid login scenario.

Implement the following test scenarios as test methods in a single test class:
1. Valid Login Test
2. Invalid Login Test

#### Tips and Inputs
1. User name is `user`, password is `bitnami`.
2. To click an element, you can call `click()` method of element.
3. To get the value of an attribute of an element, you can use `get_attribute` method call.
4. The link URL for a hyperlink in HTML is contained in its `href` attribute.

### Walk-through of a Sample Solution
Let's look at the details of a possible solution. Map to the way you approached the problem and take a note of any new learning or a different way of solving the same problem.
