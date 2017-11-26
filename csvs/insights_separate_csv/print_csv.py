import csv
import argparse

def main():
	table = []
	with open('skt_table.csv') as file:
		reader = csv.reader(file)
		for row in reader:
			printer = ''
			for i, col in enumerate(row):
				if i != 3 and i != 4 and i != 7 and i != 8 and i != 9:
					col = col.replace('\n', '')
					printer += col + '\t'
			table.append(printer)

	with open('skt_table.txt', 'w') as file:
		for row in table:		
			file.write(row + '\n')

if __name__ == "__main__":
	main()
