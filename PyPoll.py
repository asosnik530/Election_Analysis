# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote\
# Assign a variable for the file to load and the path.
File_to_load='Resources/election_results.csv'
# Open the election results and read the file
with open(File_to_load) as election_data:
# To do: Perform analysis
    print(election_data)
# Close the file. 
election_data.close()
import csv
import os
# Assign a variable for the file to load and the path
file_to_load=os.path.join("Resources", "election_results.csv")
# open the election resutls and read the file
with open(file_to_load) as election_data:
# print the file object
    print(election_data)
# create a file name variable to direct or indirect path to the file.
file_to_save= os.path.join("analysis","election_analysis.txt")
# using the open function with the"w" mode we will write data to the file
with open(file_to_save,"w") as txt_file:
# Write some data to the file
   txt_file.write("Counties in the Election\n-----------\nArapahoe\nDenver\nJefferson")
# Add our dependencies
import csv
import os
file_to_load=os.path.join("Resources","election_results.csv")
file_to_save=os.path.join("analysis","election_analysis.txt")
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    # Read and print the header row
    headers=next(file_reader)
    print(headers)