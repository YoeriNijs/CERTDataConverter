#!/usr/bin/env python

# CERT Mean Program
# By Yoeri Nijs
# Master Thesis Human Aspects of Information Technology
# Tilburg University
#
# Read txt files provided by CERT (Computer Expression Recognition Toolbox)
# Process numbers of specific Action Units for the mean
# Store all means in a csv file

# Import libs
import csv, math, glob

# Function for calculating the mean
def calculateMean(data, column):
    
    # Read Action Unit column from CERT output file. Change this when you want to read other Action Units.
    
    # List for numbers
    AU = []
    
    # Count variable
    i = 0
    for row in data:
        
        # Do not store the header
        if i <= 3:
            pass
        
        # Store data in list AU
        else:
            AU.append(data[i][column])
            
        # Count for next row
        i = i + 1
    
    # Remove NaNs in AU list
    AU = [i for i in AU if str(i) != 'NaN']
    
    # Count items in AU list
    total = float(0)
    for i in AU:
        total = float(total) + float(i)
      
    # Calculate mean of AU
    averageAU = total/len(AU)
    
    # Return the mean of AU
    return averageAU

# Directory with all CERT output files in .txt
path = '.../*.txt'   
files = glob.glob(path)

# For every file in the directory, get the mean of the given Action Units
for file in files:
      
    try:
     
        # Open data file
        data = list(csv.reader(open(file, 'rb'), delimiter='\t'))
      
        # Process data file
        with open('.../output.csv', 'ab') as csvfile:
        
            # Field names in the output csv file
            fieldnames = ['filename','AU6','AU17','AU23','AU24','Anger','Contempt','Disgust','Fear','Joy','Sad','Surprise','Neutral']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

			# Write filename and Action Units in one row
            writer.writerow({'filename': str(file),'AU6': calculateMean(data, 36),'AU17': calculateMean(data, 34),'AU23': calculateMean(data, 39),'AU24': calculateMean(data, 40),'Anger': calculateMean(data, 47),'Contempt': calculateMean(data, 48),'Disgust': calculateMean(data, 49),'Fear': calculateMean(data, 50),'Joy': calculateMean(data, 51),'Sad': calculateMean(data, 52),'Surprise': calculateMean(data, 53),'Neutral': calculateMean(data, 54)})
    
    # When file is not found  
    except IOError:
        pass
    
    # When specific number is not found
    except IndexError:
        pass
    
    # When zero division goes wrong
    except ZeroDivisionError:
        pass
