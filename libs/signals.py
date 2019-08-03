import csv

def up(ohlc):
    """Returns true/false of whether a row is 
        
    """
    if ohlc["close"] > ohlc["open"]:
        return True




with open("../ohlc.csv") as file:
    reader = csv.reader(file)

    header = next(reader)
    print(header)

    for row in reader:

        ohlc_row = {
            "open":row[3],
            "high":row[4],
            "low":row[5],
            "close":row[1]
        }

        if up(ohlc_row):
            print(ohlc_row)
        

