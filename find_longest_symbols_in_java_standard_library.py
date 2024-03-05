#!/usr/bin/env python3

# SPDX-License-Identifier: MIT
#
# Copyright © 2024 Victor Chernyakin
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import re
import requests
from bs4 import BeautifulSoup
from itertools import islice

def java_standard_library_symbols() -> set[str]:
	"""
	Get every symbol in the the Java standard library.
	"""

	symbols = set()

	for i in range(1, 28): # A-Z and _
		raw_page = requests.get(f"https://docs.oracle.com/javase/8/docs/api/index-files/index-{i}.html").text
		parsed_page = BeautifulSoup(raw_page, "html.parser")
		for l in parsed_page.find_all("span", "memberNameLink"):
			symbols.add(re.match(r"\w+", l.a.get_text()).group(0))

	return symbols

def main() -> None:
	for symbol in islice(sorted(java_standard_library_symbols(), key=len, reverse=True), 10):
		print(f"{len(symbol):>2}: {symbol}")

if __name__ == "__main__":
	main()
