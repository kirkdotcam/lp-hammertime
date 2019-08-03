import csv



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

        print(ohlc_row)
        

