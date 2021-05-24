# Election_Analysis
*Utilizing Python & VS Code Integration: Election Auditing Performance*

---
## Project Overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

  1. Calculate the total number of votes cast.
  2. Get a complete list of candidates who received votes.
  3. Calcuate the total number of votes each candidate received.
  4. Calculate the percentage of votes each candidate won.
  5. Determine the winner of the election based on popular vote.

In addition, the election committee has requested the following information to complete the aforementioned audit analysis:

  1.  The voter turnout for each county
  2. The percentage of votes from each county out of the total vote count
  3. The county with the highest turnout

To fulfill the brief, the following deliverables are created:
  - Deliverable 1: The Election Results Printed to the Command Line
  - Deliverable 2: The Election Results Saved to a Text File
  - Deliverable 3: A written Analysis of the Election Audit

---

---
## Election-Audit Results: 
The analysis of the election shows that:
- There were 369,711 votes cast in the congressional election.

- The participating counties and their respective votes were:
  - Jefferson: Received 10.5% of the vote and 38,855 number of votes.
  - Denver: Received 82.8% of the vote and 306,055 number of votes.
  - Arapahoe: Received 6.7% of the vote and 24,801 number of votes

_This makes Denver the county with the largest voter turnout._

- The congressional candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.

_This makes Diana DeGette, the winner of the election, who received 73.8% of the vote and 273,892 number of votes_

---
## Election-Audit Summmary
Based on the analysis and my experience in writing python scripts for election audits, I am providing the election commision with a business proposal: the external validity of this script is wide ranging, given appropriate modifications, making it a reliable resource that can be utilised for any election.

1. Scale the script to analyse election turnout data for future senatorial election audits or presidential elections.

To address this, I would suggest modifiying the portion of the script that utilzing list indexing to retrieve candidate/county names. Instead of hard-coding the row number of the data file, a future adapter of this script can instead search for column header names like "County", "State", or "Candidate". Data from larger elections may not be so user friendly in format. With more potential variables to delve into and larger date files, the more automated the script is in the extraction process, the less time it will take for modification down the line. 

2. Secondly, I would suggest adding a third KPI to analyse when auditing the election data: method of voting. The data provided did shed light on how votes were casted in each county for the congressional candidates. There were three voting methods used to support the collection of votes and aid in voter turnout:

  - Mail-in Ballot, hand counted
  - Punch Cards, machine counted
  - Direct Recoding Electiontric, computer counted

To ensure that future elections are accurately and effectively managed, one should consider adding a analysis on voter turnout by method: This can prove useful when candidates or campagin teams need further corroboration on the final election results, especially when mail-in ballot counting risks human error. Furthermore, election commisions can use this information down the line when allocating resources to election infrastructure after the analysis indicates the most popular methodologies by the voters. Campaign teams can utilize this information to optimize advertising resources closer to the election, creating localized campaign strategies to sway in-between voters. To accomplish this, one can adapt the current "county" or "candidate" for loop iterations to look for column headers with categorical "voter method" data rows.






