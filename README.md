
# Determining Election Results with Python

## Overview of Project

Use Python to analyze a .csv file containing election results to determine a winner.

### Purpose

Using `for` loops and conditional statements analyze the `election_results.csv` file and provide the results for total votes cast, number and percentage of votes for each candidate, number and percentage of votes in each county, and the name of the county with the largest voter turnout. The results should be printed to the terminal and saved to the `election_results.txt` file.

## Election-Audit Results

* The total number of votes cast: (369,711) 

* County Votes:
    - Jefferson: 10.5% (38,855)
    - Denver: 82.8% (306,055)
    - Arapahoe: 6.7% (24,801)

* Largest County Turnout: (Denver)

* Candidate Votes:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)

* Election Winner:
    - Diana DeGette
    - Vote Count: 272,892
    - Percentage: 73.8%

### Example of Code for Results

The full script is available in the provided `PyPoll_Challenge.py` file.

Adding to Total Votes
```
# For each row in the CSV file.
for row in reader:

    # Add to the total vote count
    total_votes += 1
```
Adding to County Votes
```
if county_name not in county_options:

    # 4b: Add the existing county to the list of counties.
    county_options.append(county_name)

    # 4c: Begin tracking the county's vote count.
    county_votes[county_name] = 0

# 5: Add a vote to that county's vote count.
county_votes[county_name] += 1
```
Adding to Candidate Votes
```
if candidate_name not in candidate_options:

    # Add the candidate name to the candidate list.
    candidate_options.append(candidate_name)

    # And begin tracking that candidate's voter count.
    candidate_votes[candidate_name] = 0

# Add a vote to that candidate's count
candidate_votes[candidate_name] += 1
```
Example of Determining Percentage
```
# 6c: Calculate the percentage of votes for the county.
    cvote_percentage = float(cvotes) / float(total_votes) * 100
    county_results = (
        f"{county_name}: {cvote_percentage:.1f}% ({cvotes:,})\n")
```

## Election-Audit Summary

This script can be reused to determine outcomes of other elections if using a `.csv` file that has the results in it. One step needed would be to change the path at `file_to_load = ` by providing the correct directory and file name for the new file. Another modification needed might be referencing the correct index if the data is in a different order in the new `.csv` file. 

The data in the `.csv` file used in this analysis is as follows (Ballot ID,County,Candidate) with the index being (0,1,2). The new file for example could be (Ballot ID,Candidate,County) then at the following location in the code, the index would need to be changed for candidate_name and county_name next to `row[]`.
```
# For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes += 1

        # Get the candidate name from each row.
        candidate_name = row[2]

        # 3: Extract the county name from each row.
        county_name = row[1]
```
