#!/usr/bin/env python3

import random

def add_film(films, new_film)
	films.append(new_film)
	print("New film added")

def choice_film(films)
	if not films:
		print("Not added films")
		return
	random_film = random.choice(films)
	print(random_film)

def main()
	films = []
	while True:
		print("Print 1 for add a film")
		print("Print 2 for choice a film")
		print("Print 3 for exit")

