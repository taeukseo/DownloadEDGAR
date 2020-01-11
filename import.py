import pandas as pd

filename = 'master'
year = 2004
qtr = 4

def idx2csv(filename,year,qtr):

    lookup1 = 'CIK|Company Name|Form Type|Date Filed|Filename'

    exportfilename = "csv/" + "Y" + str(year) + "Q" + str(qtr) + ".csv"
    readfilename = "www.sec.gov/Archives/edgar/full-index/" + str(year) + "/QTR" + str(qtr) + "/master.idx" 
    enc = 'latin-1'

    with open(readfilename, encoding = enc) as myFile:
        for temp, line in enumerate(myFile, 1):
            if lookup1 in line:
                num1temp = temp
    num1start = num1temp

    df1 = pd.read_csv(readfilename, sep = '|', skiprows= range(0,num1start-1), encoding=enc)
    df2 = df1.drop(df1.index[0])
    df2.to_csv(exportfilename, index=False)
    print("Imported Y%dQ%d" % (year,qtr))


for Y in range(1993,2020):
    for Q in range(1,5):
        idx2csv('master',Y,Q)
    