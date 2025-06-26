# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    compare.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tkeil <tkeil@student.42.fr>                +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/06/26 14:49:41 by tkeil             #+#    #+#              #
#    Updated: 2025/06/26 16:29:07 by tkeil            ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import re
import sys

def get_words_from_file(path):
	try:
		with open(path, 'r', encoding='utf-8') as file:
			text = file.read()
		words = re.split(r'[\n\r\v\t\f ]+', text)
		return set(filter(None, words))
		
	except FileNotFoundError:
		print(f"Error: File '{path}' not found.")
		sys.exit(1)

def print_diff(missing):
	for word in sorted(missing):
		print(word)

def main():
	if len(sys.argv) != 3:
		print("Usage: python compare.py <file1> <file2>")
		sys.exit(1)
	words1 = get_words_from_file(sys.argv[1])
	words2 = get_words_from_file(sys.argv[2])
	
	missing1 = words1 - words2
	missing2 = words2 - words1

	if missing1:
		print("\033[92mWords in file1 but not in file2:\033[0m")
		print_diff(missing1)
		
	if missing2:
		print("\n\033[92mWords in file2 but not in file1:\033[0m")
		print_diff(missing2)
	
	input = input("\nWrite the missing words to a file? (y/n): ").strip().lower()
	if input == 'y':
		output_file = input("Enter the output file name: ").strip()
		try:
			with open(output_file, 'w', encoding='utf-8') as file:
				if missing1:
					file.write("Words in file1 but not in file2:\n")
					for word in sorted(missing1):
						file.write(word + '\n')
				if missing2:
					file.write("Words in file2 but not in file1:\n")
					for word in sorted(missing1):
						file.write(word + '\n')
			print(f"Missing words written to {output_file}")

		except IOError as e:
			print(f"Error writing to file '{output_file}': {e}")
		

if __name__ == "__main__":
	main()
