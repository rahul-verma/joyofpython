'''
This file is a part of The Joy of Python Gihub Repository.
Copyright 2019 Rahul Verma
Website: www.RahulVerma.net
Email: rv [at] testmile.com
Creator: Rahul Verma
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''


import unittest

from jopt.calc import *


class CalcTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.calc = None

    def setUp(self):
        self.calc = self.calc and self.calc or Calculator()

    def tearDown(self):
        self.calc.reset()

    def __assert_state(self, expected_state):
        self.assertEqual(self.calc.calc_count, expected_state, "State not updated.")

    def test_addition(self):
        state = self.calc.calc_count
        self.assertEqual(self.calc.add(3,4), 7, "Addition is wrong.")
        self.__assert_state(state + 1)

    def test_subtraction(self):
        state = self.calc.calc_count
        self.assertEqual(self.calc.add(5,3), 2, "Subtraction is wrong.")
        self.__assert_state(state + 1)

    def test_state(self):
        state = self.calc.calc_count
        self.calc.add(1,2)
        self.calc.sub(1, 4)
        self.calc.add(1, 4)
        self.__assert_state(state + 3)
        self.calc.reset()
        self.__assert_state(0)


if __name__ == "__main__":
    unittest.main()