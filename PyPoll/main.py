#importing csv file
import os
import csv

#extracting the file path
polls_csv = os.path.join("Resources", "election_data.csv")

#read file, print header, skip header
with open ("Resources/election_data.csv", newline='') as file:
    csv_reader=csv.reader(file, delimiter=",")
    csv_header=next(csv_reader)
    print(f"csvheader:{csv_header}")

    #vote count
    initial_votes = 0
    #total_votes = []
    
    #dictionary of candidates
    candidates_with_votes_dict= {}


    #voter analysis 
    #total number of votes
    for row in csv_reader:
        Voter_ID = int(row[0]) 
        initial_votes += 1 
        Voter_ID = float(Voter_ID)
        
        total_votes = Voter_ID + initial_votes
        total_votes += 1
        print(f'TOTAL number of votes: {(total_votes)}')
        
        #vote percentage 
        
        #County
        County = str(row[1])
        
        #Candiate analysis
        for candidates in csv_reader:
            
            Candidate = str(row[2])
        #if vote_percentage > 50: