#!/usr/bin/env python

# Copyright 2018-2020 John T. Foster
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import unittest
import nbconvert

with open("assignment2.ipynb") as f:
    exporter = nbconvert.PythonExporter()
    python_file, _ = exporter.from_file(f)


with open("assignment2.py", "w") as f:
    f.write(python_file)


from assignment2 import square, finite_diff, well


class TestSolution(unittest.TestCase):

    def test_square(self):
        assert square(10) == 100
        assert square(0) == 0

    def test_finite_diff(self):
        assert abs(finite_diff(4, 0.1) - 5.0) < 1e-6

    def test_well(self):
        assert abs(well(1.2, 5000, 3000) - 427.44) <= 0.1 

if __name__ == '__main__':
    unittest.main()
