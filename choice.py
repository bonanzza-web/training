#!/usr/bin/env python3

import random

def add_film(films, new_film):
	films.append(new_film)
	print("New film added")

def choice_film(films):
	if not films:
		print("Not added films")
		return
	random_film = random.choice(films)
	print("You choiced: ", random_film)

def main():
	films = []
	while True:
		print("Print 1 for add a film")
		print("Print 2 for choice a film")
		print("Print 3 for exit")

		choice = input("Choice option: ")

		if choice == "1":
			new_film = input("Enter film: ")
			add_film(films, new_film)
		elif choice == "2":
			choice_film(films)
			input("Push enter for exit: ")
			break
		elif choice == "3":
			print("Exit")
			break
		else:
			print(choice)

if __name__ == "__main__":
	main()
