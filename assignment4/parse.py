import csv
import sys

def readCSV(filename):
    '''Reads the CSV file `filename` and returns a list
    with as many items as the CSV has rows. Each list item 
    is a tuple containing the columns in that row as stings.
    Note that if the CSV has a header, it will be the first
    item in the list.'''
    with open(filename,'r') as f:
        rdr = csv.reader(f)
        lines = list(rdr)
    return(lines)


### enter your code below
def get_avg_latlng(data):
    '''to compute the average latitude and longitude; also constructs permits in HP'''
    numrows = len(data)
    sumlatitude = 0
    sumlongitude = 0
    for row in data:
        sumlatitude = float(row[128]) + sumlatitude
        sumlongitude - float(row[129]) + sumlongitude
    1 = sumlatitude/numrows
    o = sumlongitude/numrows
    return(1,o)

hpp = readCSV("permits_hydepark.csv")
print(get_avg_latlng(hpp))

#clean HP dataset
cleaned_sip = []
for rown in readCSV('permits_hydepark.csv'):
    if row[28] == "":
        pass
    elif len(row[28]) == 6:
        cleaned_zip.append(int(row[28].split('-')[0]))
    else:
        cleaned_zip.append(int(row[28]))

#print(cleaned_zip)



#Make a Histogram!
import matplotlib.pyplot as plt
import numpy as np

#print(np.unique(cleaned_zip, return_counts = True)

def zip_code_barchart(data):
    fig = plt.figure()
    width = 0.1
    unique_zip_array = np.unique(data)
	unique_zip = unique_zip_array.tolist()
	zip_counts = np.unique(data, return_counts=True)
	plt.bar(unique_zip, zip_counts[1])
	plt.title("Hyde Park Zip Code Bar Chart")
	plt.xlabel("Zip Codes")
	plt.ylabel("Frequency")
	plt.tight_layout()
	#plt.show()
	plt.savefig("hpzip_bar.jpg")

zip_cade_barchart(cleaned_zip)



#combine into an executable program
def zip_code_barchart2(data):
	fig = plt.figure()
	width = .1
	unique_zip_array = np.unique(data)
	unique_zip = unique_zip_array.tolist()
	zip_counts = np.unique(data, return_counts=True)
	plt.bar(unique_zip, zip_counts[1])
	plt.title("Hyde Park Zip Code Bar Chart")
	plt.xlabel("Zip Codes")
	plt.ylabel("Frequency")
	plt.tight_layout()
	plt.show()
	#plt.savefig("hpzip_bar.jpg")

for arg in sys.argv:
	if arg == "latlong":
		print get_avg_latlng(hpp)
	elif arg == "hist":
	    print zip_code_barchart2(cleaned_zip)
