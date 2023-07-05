

def generate_table(labels):
	max_length = max(len(label) for label in labels) + 4
	table_width = max_length + 4

	centered_labels = [label.center(max_length + 2) for label in labels]

	print('+' + '-' * (table_width - 2) + '+')
	for label in centered_labels:
		print(f'|{label}|')
		print('+' + '-' * (table_width - 2) + '+')

user_input = input('Enter table labels (comma-separated): ')
labels = [label.strip() for label in user_input.split(',')]
generate_table(labels)
