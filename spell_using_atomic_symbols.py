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

from typing import Iterable

SYMBOLS = [
	 "H", "He", "Li", "Be",  "B",  "C",  "N",  "O",  "F", "Ne",
	"Na", "Mg", "Al", "Si",  "P",  "S", "Cl", "Ar",  "K", "Ca",
	"Sc", "Ti",  "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
	"Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr",  "Y", "Zr",
	"Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
	"Sb", "Te",  "I", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
	"Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
	"Lu", "Hf", "Ta",  "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
	"Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
	"Pa",  "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
	"Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
	"Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og",
]

def spell_using_atomic_symbols(remaining_str: str, potential_spelling: str = "") -> Iterable[str]:
	"""
	Generate ways to spell a word using atomic symbols.
	"""
	if remaining_str == "":
		yield potential_spelling
		return

	for symbol in SYMBOLS:
		if remaining_str.casefold().startswith(symbol.casefold()):
			yield from spell_using_atomic_symbols(remaining_str[len(symbol):], potential_spelling + symbol)

def main() -> None:
	while True:
		for spelling in spell_using_atomic_symbols(input("Type a word: ")):
			print(spelling)

if __name__ == "__main__":
	main()
