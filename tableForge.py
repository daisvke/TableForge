padding = 8

def generate_table(labels):
	max_length = max(len(label) for label in labels) + padding
	table_width = max_length

	centered_labels = [label.center(table_width) for label in labels]

	print('+' + '-' * table_width + '+')
	for label in centered_labels:
		print(f"|{label}|")
		print('+' + '-' * table_width + '+')

user_input = input('Enter table labels (comma-separated): ')
labels = [label.strip() for label in user_input.split(',')]
generate_table(labels)
