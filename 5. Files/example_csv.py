import csv


with open('examp_csv_text.txt', 'w') as f:
    o = csv.writer(f)
    o.writerow(range(5))
    o.writerow(['a', 'b', 'c', 'd', 'e'])