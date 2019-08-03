import csv

# defines up function
def up(ohlc):
    """Returns true/false of whether a row is 
        
    """

    # test whether the stock 
    if ohlc["close"] > ohlc["open"]:
        return True
    else:
        return False

# defines hammer function
def hammer(ohlc):
    """Returns true/false of whether row is a "hammer" signal

    Args:
        row(ohlc dictionary)
    """

    if (ohlc["close"]==ohlc["high"]) and up(ohlc) and (ohlc["low"]<ohlc["open"]):
        return True
    else:
        return False

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

        if hammer(ohlc_row):
            print(row[0],ohlc_row)
        

