import csv
import time
from tqdm import tqdm

def search_csv(input_file, output_file, keyword):
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        header = next(reader)  # Read the header

        # Find the indices of columns containing the keyword
        keyword_indices = []
        for index, column in enumerate(header):
            if keyword.lower() in column.lower():
                keyword_indices.append(index)

        with open(output_file, 'w', newline='') as output:
            writer = csv.writer(output)
            writer.writerow(header)  # Write the header to output.csv

            total_rows = sum(1 for _ in reader)  # Get the total number of rows (excluding header)
            file.seek(0)  # Reset the file pointer
            next(reader)  # Skip the header while iterating

            with tqdm(total=total_rows, unit='rows', unit_scale=True) as pbar:
                for row in reader:
                    # Check if any keyword indices contain the keyword
                    if any(keyword.lower() in str(row[index]).lower() for index in keyword_indices):
                        writer.writerow(row)  # Write the row to output.csv

                    pbar.update(1)  # Update progress bar

                    # Delay to update the progress bar at least once per second
                    time.sleep(0.01)

    print("Output file generated successfully.")


# User input
input_csv = input("Enter the name of the input CSV file: ")
output_csv = input("Enter the name of the output CSV file: ")
search_keyword = input("Enter the keyword to search: ")

# Run the script
search_csv(input_csv, output_csv, search_keyword)
