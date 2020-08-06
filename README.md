# Python Assignment - Klika

This repository contains Python script and CSV file which are part of the job application assignment.

The script exports temperature-resistance pairs from thermistor datasheet and exports them to JSON file.

Python version used: **3.8.5**

Run script by using 
`python interview_solution.py -c fileName.csv`
or 
`python3 interview_solution.py -c fileName.csv`

where **fileName.csv** is name of your CSV file.

There is an optional "skip lines" parameter (`-s`) which you can use to specify how many header lines of the CSV file should be skipped from the top. I know that sometimes this can be hard for programmers, but counter starts from 1, not 0 :)

In case you want to skip first 100 lines of CSV file, command should be
`python interview_solution.py -c fileName.csv -s 100`



**Important note**

There is a pilcrow (¶) symbol in the header of CSV file. Python can't process it (even if you skip header lines). Because of this, Python script will terminate with the following error:

`UnicodeDecodeError: 'charmap' codec can't decode byte 0x83 in position 34: character maps to <undefined>`

Please remove pilcrow symbol and blank space before it in order for script to run without problems.

I have uploaded corrected version of CSV file just in case (**NTCG163JF103FT1-corrected.csv**).


