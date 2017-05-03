# -*- coding: utf-8 -*-
"""
(@)Author: glassCodeBender
(#)Title: TableFilter.py
(#)Version: 1.0

WARNING: Currently the program does not work from the commandline. However, the main aspects of the program work. I already
used them to filter out duplicate names from an excel document.

Program Purpose: Program allows users to remove duplicates from a column in a csv file (or excel converted to csv). The actual purpose
of the program was to remove duplicate rows from an excel file so that I could use the sample data in a database for a school project. 
Eventually I will design the program to accept commandline arguments. However, since the current program is a full program instead of 
a script, I need to use a program other than system.argv.

Inputs:

__file1 : Accepts String filename. Currently accepts only csv files.
__duplicate : Accepts a String. User determines the name of the column to remove duplicate rows based on 
    - I used 'Customer Name' in my program to remove duplicate customers.
__file_destination : Determines where the newly created csv file should save to. 
    - I need to rewrite the program so that it saves to the default working directory when I add commandline arguments.


NEED TO ADD __main__ == __name__ and help functionality. 

This program will be periodically updated to include much more functionality.

"""

import pandas as pd
import argparse
import os
import sys

class TableFilter(object):
    def __init__(self):
        self.__file = args.file
        self.__duplicate_column = args.duplicate_column
        self.__file_dest = args.file_dest
        # Adding extra functionality to program
        self.__compare = args.compare

    """
        Description: Method filters out the unique values in the column of a csv file.
        Return: DataFrame excluding the value
    """

    def populate_df(self):
        try:
            csv_file = self.__file
            df = pd.DataFrame()
            pop_df = df.from_csv(csv_file)
        except IOError as e:
            print("I/O error: The file did not import properly.")
        return pop_df

        """        
        Create a column of boolean values 
        Check to see if the previous value in the column is equal
        """

    def filter_uniq(self):
        dup = self.__duplicate
        pop_df = self.populate_df
        pop_df['Unique'] = (pop_df[dup] == pop_df[dup].shift())
        filtered_df = pop_df[pop_df['Unique'] == False]
        return filtered_df

    """ Export to filtered DataFrame to CSV file. """

    def export_to_CSV(self) -> object:
        fileDestination = self.__file_dest
        df = self.filter_uniq()
        df.to_csv(fileDestination)

    # Process command-line arguments.
    if __name__ == '__main__':

        """ Create commandline functionality and add a help command. """
        parser = argparse.ArgumentParser( add_help=True, description="Allows users to filter CSV file in a variety of ways." )
        parser.add_argument( '-f', action = 'store', dest = 'file', help='Store the name of the csv file you want converted' )
        parser.add_argument( '-c', action = 'store', dest = 'column', help='Store the name of the column you want filtered.' )
        parser.add_argument( '-d', action = 'store', dest = 'file_destination', default= str( os.getcwd() ) + "/filteredcsvfile.csv", help= "Store the name of the file you'd like the program to create" )
        parser.add_argument( '-a', action = 'store', dest = 'compare', help = 'Use "gt" for greater than, "lt" for less than, or "eq" for equals')

        if len(sys.argv) <= 2:
            parser.print_help()
            sys.exit(1)

        args = parser.parse_args()
        # file = cmd_args.file
        # duplicate_column = cmd_args.column
        # file_dest = cmd_args.file_destination

        filter_object = TableFilter()
        filter_object.export_to_CSV()

        """
        if file_destination is None:
            file_destination = os.getcwd() + "/filteredcsvfile.csv"
        """
