import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
bestsellers = os.path.join(script_dir, 'bestsellers.csv')
bestseller_info = os.path.join(script_dir, 'bestseller_info.csv')

# Open the CSV file in 'write' mode
with open(bestsellers, 'r', encoding='utf8') as file:
  # Create a CSV writer object
  csv_reader = csv.reader(file)

  header = next(csv_reader)
  max_sales = 0
  best_selling_book = None

  for row in csv_reader:
     current_sales = float(row[4]) # assuming sales are in column 4 (index 4)
     
     if current_sales > max_sales:
         max_sales = current_sales
         best_selling_book = row
         print(best_selling_book)

with open(bestseller_info, 'w', newline='', encoding='utf8') as out_file:
    csv_writer = csv.writer(out_file)

    csv_writer.writerow(['Title', 'Author', 'Sales in Millions'])
    csv_writer.writerow([best_selling_book[0], best_selling_book[1], best_selling_book[4]])
