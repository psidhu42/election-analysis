# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

import csv
import os

# Assign a variable for the file to load and the path.

# direct load method: file_to_load = 'resources/election_results.csv'
# indirect method:
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
# open() function: election_data = open(file_to_load, 'r')
# 'with' function:
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    print(election_data)
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

# # Print each row in the CSV file.
#     for row in file_reader:
#         print(row)

# Print the header row.
    headers = next(file_reader)
    print(headers)

# Close the file, if using open() funtion.
#election_data.close()

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")