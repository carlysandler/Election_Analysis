# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# The total numer of votes each candidate won
# The winnner of the election based on popular vote.

# Import the datetime class from this datetime moodule.
import datetime as dt
# Use the now() atttribute on the datetime class to get the present time.
now = dt.datetime.now()
# Print the present time.
print("The time right now is ", now)
import csv
print(dir(csv))

print(dir(int))
print(dir(float))
print(dir(bool))
print(dir(list))
print(dir(tuple))
print(dir(dict))
print(dir(dt))
import random
print(dir(random))

# file_variable = open(filename, mode)
## file_variable = name of variable that will reference the file object 
## filename = string specifying the name of the file
## mode = string specifying the mode for reading/writing the file object
### "r": open a file to read
### "w": open to write; if file exists, will overwrite
### "x": open for exclusive creation; only if file exists
### "a": open to append data to existing file or create new
### "+": open for reading and writing 


	
# Open election_results.csv file
import csv
import os

# Assign a variable for the file to load and the path
## Chaining for variable declaration; program style for making (+) method calls on same object; code is clear & concise
file_to_load = os.path.join("RESOURCES", "election_results.csv")
# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data: 
	file_reader = csv.reader(election_data)

	# Read and print the header row.
	headers = next(file_reader)
	print(headers)


	



# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
	
	# Write three counties to the file. 
	txt_file.write("Arapahoe\nDenver\nJefferson")


