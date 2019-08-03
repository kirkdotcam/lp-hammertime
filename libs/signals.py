import csv

# defines up function
def up(ohlc):
    """Returns true/false of whether a row increases in value over the day
        
    """

    # test whether the stock rose on the day.
    if ohlc["close"] > ohlc["open"]:
        return True
    else:
        return False

# defines hammer function.
def hammer(ohlc):
    """Returns true/false of whether row is a "hammer" signal

    Args:
        row(ohlc dictionary)
    """

    # test whether the stock a) has a flat top b) rises and c) has a low shadow below the opening price
    if (ohlc["close"]==ohlc["high"]) and up(ohlc) and (ohlc["low"]<ohlc["open"]):
        return True
    else:
        return False


with open("../ohlc.csv") as file:

    # begin reading csv file
    reader = csv.reader(file)

    # pops the header row off the dataset
    header = next(reader)
    print(header)

    # processing rows
    for row in reader:

        #abstract ohlc data from the row into dictionary for easier handling
        #Bonus: could you make this a separate function?
        ohlc_data = {
            "open":row[3],
            "high":row[4],
            "low":row[5],
            "close":row[1]
        }

        if hammer(ohlc_data):
            print(row[0],ohlc_data)
        

