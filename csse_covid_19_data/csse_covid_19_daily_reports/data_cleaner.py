import csv

nyc_data = []
nyc_data_clean = [['Date', 'Confirmed', 'Deaths', 'Recovered']]

with open('03-09-2020.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    nyc_data.append(list(csv_reader)[0])

#print 'nyc data is currently', nyc_data

state = 'California'
#Processing only March data
for i in range(1,32):
    if i<10:
        date = '03-0'+str(i)+'-2020'
    else:
        date = '03-'+str(i)+'-2020'
    filename = date+'.csv'
    #print 'Processing date', date
    with open(filename) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        columns = csv_reader[0]
        #print 'columns', columns
        d = columns.index('Deaths')
        r = columns.index('Recovered')
        c = columns.index('Confirmed')
        #print 'rcd', r, c, d
        for row in csv_reader:
            if row[0]==state or row[1]==state or row[2]==state:
                #print 'Found NYC'
                nyc_data.append(row)
                nyc_data_clean.append([date, row[c], row[d], row[r]])
print 'March data processed'


#Processing only April data
for i in range(1,12):
    if i<10:
        date = '04-0'+str(i)+'-2020'
    else:
        date = '04-'+str(i)+'-2020'
    filename = date+'.csv'
    with open(filename) as csv_file:
        csv_reader = list(csv.reader(csv_file, delimiter=','))
        columns = csv_reader[0]
        #print 'columns', columns
        d = columns.index('Deaths')
        r = columns.index('Recovered')
        c = columns.index('Confirmed')
        #print 'rcd', r, c, d
        for row in csv_reader:
            if row[0]==state or row[1]==state or row[2]==state:
                #print 'Found NYC'
                nyc_data.append(row)
                nyc_data_clean.append([date, row[c], row[d], row[r]])
print 'April data processed'

#print 'nyc data over date range is', nyc_data_clean

#write this data to a text file
outfile = 'Cali_data_raw.txt'
with open(outfile, 'w') as f:
    for line in nyc_data:
        f.write('\t'.join(line))
        f.write('\n')
print 'Done writing to', outfile

outfile = 'Cali_data_clean.txt'
with open(outfile, 'w') as f:
    for line in nyc_data_clean:
        f.write('\t'.join(line))
        f.write('\n')
print 'Done writing to', outfile

