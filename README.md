# Election_Analysis

# Overview of Election Audit: 
In this assignment I assisted a Colorado board of elections employee in an election audit of the tabulated results for a U.S. congressional precinct in Colorado. I was tasked with reporting the total number of votes cast, the total number of votes for each candidate and county, the percentage of votes for each candidate and county, and the winner of the election based on the popular vote.

# Election-Audit Results: 

## Total votes.
In this election, there were 369,711 votes cast.

## Breakdown of the number of votes and the percentage of total votes for each county in the precinct.
* Jefferson received 10.5% of the votes (38,855) votes 
* Denver received 82.8% of the votes (306,055) while 
* Araphoe received 6.7% of the votes (24,801)

## County with the largest number of votes.
The winning county was Denver, with nearly 83% of the popular vote.

## Breakdown of the number of votes and the percentage of the total votes each candidate received.
* Charles Casper Stockham received 23.0% of the votes (85,213) 
* Diana DeGette received 73.8% of the votes (272,892) and 
* Raymon Anthony Doane received 3.1% of the votes (11,606).

## Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
The winner of the election is Diana DeGette, who received 73.8% of the votes (272,892).

### Terminal screenshot 
<img width="614" alt="Screen Shot 2022-09-13 at 21 14 43" src="https://user-images.githubusercontent.com/80678332/190037369-4fef61aa-04ae-4c79-b362-a3d89b56c2f2.png">


### Text file screenshot 

<img width="491" alt="Screen Shot 2022-09-13 at 21 15 33" src="https://user-images.githubusercontent.com/80678332/190037380-3009224a-001d-4e12-9dbd-71c60a1b117e.png">

# Election-Audit Summary: 
This script could be further enhanced to estimate the votes that were cast by gender. This could be useful in seeing which gender voted most for which candidate and in which county. To get the gender count, a gender column would need to be first added to the dataset. Then, inside the for loop, we can count the votes by gender by iterating through the rows.   

Another idea would be to check for duplicate ballot IDs in the first column of the CSV file. Instead of the csv reader function, we could convert this file into a dataframe and use the following code: df.drop_duplicates(subset=['ID'], inplace=True)

This script could also be modified to account for historical election data. We may have a dataset with votes for different years, where we could prompt the user for input: input = "Please enter the year for which you would like to see the election results, enter 2018, 2019, or 2020" 


