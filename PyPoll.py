# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who recieved votes.
# 3. The total number of votes each candidate won.
# 4. The percentage of votes each candidate won.
# 5. The winner of the election based on popular vote.

import csv
import os
from telnetlib import theNULL

# Assign a variable for the file to load and the path.

# direct load method: file_to_load = 'resources/election_results.csv'
# indirect method:
file_to_load = os.path.join("resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1a. Initialize a total vote counter.
total_votes = 0

# 2a. Declare new list for candidates.
candidate_options = []

# 3a. Declare an empty dictionary. 
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
# open() function: election_data = open(file_to_load, 'r')
# 'with' function:
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    print(election_data)
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 1b. Add to the toatl vote count.
        total_votes += 1

        # 2b. Print the candidate name from each row, append list to add names.
        candidate_name = row[2]
        
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)

            # 3b. Begin tracking that candidates vote count.
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1


    # 4. Determine the percentage of votes for each candidate by looping through the counts.
    # Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # Print the candidate name and percentage of votes.
        #print(f"{candidate_name}: received {vote_percentage:.1f}% of the vote.")

        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"        
        f"-------------------------\n")
    print(winning_candidate_summary)

# 1c. Print the total votes.
print(total_votes)

# 2c. Print the list of Candidates.
print(candidate_options)

# 3c. Print the candidate vote in dictionary.
print(candidate_votes)

# Close the file, if using open() funtion.
#election_data.close()

# Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")