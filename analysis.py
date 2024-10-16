# Modules
import serial
import matplotlib.pyplot as plt
import csv

# Variables
readings_count = 1
counter = 0
peaks_count = 0
maximum = 0
sample_no = 0

# Lists
readings = []
sample = []
data = []  # List to store ECG data
Ptime = []

# Setting up CSV file, CSV writer for output and ports for input
file = open('C:\\Users\\Admin\\PycharmProjects\\ECG_CODE\\dataECG.csv', 'r+')
variable = serial.Serial("COM7", 115200)
writer = csv.writer(file)

# Displaying ECG Code
while counter < 1000:
    line = variable.readline().decode().strip()  # Read a line from serial port
    writer.writerow([line])  # Write it to the CSV file
    value = int(line)  # Convert the string value to integer
    data.append(value)  # Append the value to the data list
    counter += 1
file.close()

# Adding the x and y values to the lists for plotting
file = open('C:\\Users\\Admin\\PycharmProjects\\ECG_CODE\\dataECG.csv', 'r')
for each in file:
    if each != '\n':
        readings.append(int(each[0:-1]))
        sample.append(int(readings_count))
        readings_count += 1
file.close()

# Finding the average time interval between peaks
file = open('C:\\Users\\Admin\\PycharmProjects\\ECG_CODE\\dataECG.csv', 'r')
Tcount = 0
peakTimes = []
for selection in file:
    if selection != '\n':
        readings.append(int(selection))
        if int(selection) >= 4000:
            peakTimes.append(Tcount)
    Tcount += 1
file.close()
print(peakTimes)

# Counting peaks
j = 0
while j < len(peakTimes) - 1:
    peaks_count += 1
    if peakTimes[j] + 5 >= peakTimes[j + 1]:
        j += 2
    else:
        j += 1
Tsum = 0
for i in range(0, len(peakTimes)-2, 2):
    Tsum += peakTimes[i+2] - peakTimes[i]

#Output
print("The number of peaks in 1000 samples :", peaks_count)
print("Average time between peaks: ", Tsum/(peaks_count//2))
plt.plot(readings)
plt.show()