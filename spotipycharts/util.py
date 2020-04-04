import csv

def csv_to_list(text):
    lines = text.split('\n')
    if lines[0][0] == 'P':
        reader = csv.DictReader(lines)
    else:
        reader = csv.DictReader(lines[1:])
    return [row for row in reader]
