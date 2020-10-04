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
total_votes=0
# candidate options and candidate votes
candidate_options=[]
# 1. Declare the empty dictionary.
candidate_votes={}
# winning candidates and winning count tracter
winning_candidate=""
winning_count=0
winning_percentage=0
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    # Read and print the header row
    headers=next(file_reader)
    # Print each row in CSV file
    for row in file_reader:
        #2 Add to total vote count
        total_votes += 1
        # Print the candidate name from each row
        candidate_name=row[2]
        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add it to list of candidates
            candidate_options.append(candidate_name)
            #2. begin tracking that candidate's vote count
            candidate_votes[candidate_name]=0
            # Add a vote to that candidate's count
        candidate_votes[candidate_name] += 1
#Determine percentage of votes for each candidate by looping through the counts
 # 1. Iterate through the candidate list
for candidate_name in candidate_votes:
    #2. Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3. Calcalate percentage of votes
    vote_percentage= float(votes)/float(total_votes)*100
    # to do: print each candidates name, vote count and percentage of votes to termal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    #determine winning vote count and candidate
    # Determine if the votes is greater than the winning count
    if (votes>winning_count) and (vote_percentage>winning_percentage):
        winning_count=votes
        winning_percentage=vote_percentage
        winning_candidate=candidate_name
#To do: print out winning candidate, vote count and percentage
winning_candidate_summary=(
    f"----------------------\n"
    f"Winner:{winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"--------------------\n")
print(winning_candidate_summary)