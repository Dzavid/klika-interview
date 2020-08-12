import csv
import json
import argparse


def importandexportdata(filename, numofheaderlines=6):
    with open(filename, mode='r', encoding="Latin-1") as csv_file:

        valuesdict = dict()
        fieldnames = ['Temp', 'Min', 'Nom', 'Max', 'B25/T', '-dT', 'dT']
        csv_reader = csv.DictReader(csv_file, fieldnames=fieldnames, delimiter=',')

        # Skip given number of header lines
        for i in range(numofheaderlines):
            next(csv_reader, None)

        for row in csv_reader:

            if (0 <= int(row["Temp"]) <= 100) and (int(row["Temp"]) % 5 == 0):
                valuesdict[float(row["Temp"])] = float(row["Nom"])

    # Dump data to json file
    j = json.dumps(valuesdict, indent=4)
    f = open(filename.split('.')[0] + '.json', 'w')
    print(j, file=f)
    f.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', dest="csvName", required=True, help='(Required) Name of csv file to read from')
    parser.add_argument('-s', dest="numofheaderlines",
                        help='(Optional) Number of header lines in csv file (How many lines from the top should be '
                             'skipped)')
    args = parser.parse_args()

    numofheaderlines = None
    numofheaderlines = args.numofheaderlines  # Assign value if provided by user as an argument

    filename = args.csvName

    if (filename.split('.')[-1] != 'csv'):
        print('Given file does not contain csv extension.')
        exit()

    if numofheaderlines:
        importandexportdata(filename, int(numofheaderlines))
    else:
        importandexportdata(filename)
