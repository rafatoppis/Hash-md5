# Author: Rafael Toppis
# Version: 1.0.0
# Date: 06.05.2024


import csv
import hashlib

# Specify the delimiter
delimiter = ','

# Open the file
with open('fileToHash.csv', mode='r', newline='') as csvfile:
    # Create a reader
    reader = csv.reader(csvfile, delimiter=delimiter)
    # Transform all in a list  ||  Working on the list to import to csv aagain.
    lines = list(reader)

    # Add 'hash-md5' column
    lines[0].append('hash-md5')


    # Iterate through each line and calculate hash
    for line in lines[1:]:  # Skip header line
        text = line[2] # Select the colum "M-Subject"
        # Calculate MD5 hash
        md5_hash = hashlib.md5(text.encode()).hexdigest()
        line.append(md5_hash)
    
    # Remove Duplicated Hashes to create a ID for each individual Hash number
    hashes = []
    for i in lines:
        hashes.append(i[4])
    nondup = list(set(hashes))


    # Add 'Group ID' Column
    lines[0].append('Group ID')
    for line in lines[1:]:
        value = line[4] # Select hash Column
        id = nondup.index(value) # get the nondup index where the hash was found.
        line.append(id) 


    

# Write the updated lines back to the CSV file
with open('hashed.csv', mode='w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=delimiter)
    writer.writerows(lines)

print("Hashes extracted and Grouped by ID Number.")





