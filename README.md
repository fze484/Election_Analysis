# Election_Analysis

# Overview of Election Audit: Explain the purpose of this election audit analysis.
In this assignment I assisted a Colorado board of elections employee in an election audit of the tabulated results for a U.S. congressional precinct in Colorado. I was tasked with reporting the total number of votes cast, the total number of votes for each candidate and county, the percentage of votes for each candidate and county, and the winner of the election based on the popular vote.

# Election-Audit Results: 

## How many votes were cast in this congressional election?
In this election, there were 369,711 votes cast.

## Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
* Jefferson received 10.5% of the votes (38,855) votes 
* Denver received 82.8% of the votes (306,055) while 
* Araphoe received 6.7% of the votes (24,801)

## Which county had the largest number of votes?
The winning county was Denver, with nearly 83% of the popular vote.

## Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
* Charles Casper Stockham received 23.0% of the votes (85,213) 
* Diana DeGette received 73.8% of the votes (272,892) and 
* Raymon Anthony Doane received 3.1% of the votes (11,606).

## Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
The winner of the election is Diana DeGette, who received 73.8% of the votes (272,892).

# Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election. Give at least two examples of how this script can be modified to be used for other elections.
This script could be further enhanced to estimate the votes that were cast by gender. This could be useful in seeing which gender voted most for which candidate and in which county. To get the gender count, a gender column would need to be first added to the dataset. Then, inside the for loop, we can count the votes by gender by iterating through the rows.   

This script could also be modified to account for historical election data. We may have a dataset with votes for different years, where we could prompt the user for input: input = "Please enter the year for which you would like to see the election results, enter 2018, 2019, or 2020" 


