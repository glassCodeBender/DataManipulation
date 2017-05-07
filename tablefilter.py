# -*- coding: utf-8 -*-
"""
(@)Author: glassCodeBender
(#)Title: TableFilter.py
(#)Version: 1.0

WARNING: Currently the program does not work from the commandline. However, the main aspects of the program work. I already
used them to filter out duplicate names from an excel document.

Program Purpose: Program allows users to remove duplicate values from a column in a csv file (or excel converted to csv). 
The actual purpose of the program was to remove duplicate rows from an excel file so that I could use the sample data in 
a database for a school project.

Inputs:
__file1 : Accepts String filename. Currently accepts only csv files.
__duplicate_column : Accepts a String. User determines the name of the column to remove duplicate rows based on 
    - I used 'Customer Name' in my program to remove duplicate customers.
__file_dest : Determines where the newly created csv file should save to. 
    - I need to rewrite the program so that it saves to the default working directory when I add commandline arguments.

This program will be periodically updated to include much more functionality.
"""

import pandas as pd
import argparse
import os
import sys

class TableFilter(object):

    def __init__(self, file = '', duplicate = '', file_destination = '', compare = '' ):
        self.__file = file
        self.__duplicate_column = duplicate
        self.__file_dest = file_destination
        # Adding extra functionality to program
        self.__compare = compare

    """ Description: Method filters out the unique values in the column of a csv file.
        Return: DataFrame excluding the value """

    def populate_df(self):
        try:
            csv_file = self.__file
            df = pd.DataFrame()
            pop_df = df.from_csv(csv_file)
        except IOError as e:
            print( "I/O error: The file did not import properly." )
        return pop_df

        """        
        Create a column of boolean values 
        Check to see if the previous value in the column is equal
        """

    def filter_uniq(self):
        dup = self.__duplicate_column
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

        """ Create commandline functionality to the program """
        parser = argparse.ArgumentParser( add_help = True, description = "Allows users to filter CSV file in a variety of ways." )

        # NEED TO ADD PARSER GROUP CALLED 'Positional Arguments'
        # parse.add_argument_group()
        parser.add_argument( '-f', '--file', dest = 'store', dest = 'file', help='Store the name of the csv file you want converted' )
        parser.add_argument( '-n', '--column', action = 'store', dest = 'column', help='Store the name of the column you want filtered.' )

        # NEED TO ADD PARSER GROUP CALLED 'Optional Arguments'
        # parser.add_argument_group()
        parser.add_argument( '-d', '--dest', action = 'store', dest = 'file_destination', default= str( os.getcwd() ) + "/filteredcsvfile.csv", help = "Store the name of the file you'd like the program to create" )
        parser.add_argument( '-c', '--compare', action = 'store', dest = 'compare', help = 'Use "gt" for greater than, "lt" for less than, or "eq" for equals')
        parser.add_argument( '-v', '--verbose', action = 'store_true', help = 'Increase the verbosity of the command.')

        if len(sys.argv) <= 2:
            parser.print_help()
            sys.exit(1)

        args = parser.parse_args()
        # file = cmd_args.file
        # duplicate_column = cmd_args.column
        # file_dest = cmd_args.file_destination

        assert os.path.exists( str(os.getcwd()) + '/' + args.file)

        filter_object = TableFilter(args.file, args.column, args.dest, args.compare)
        filter_object.export_to_CSV()

        if args.verbose:
            assert isinstance(args.dest)
            print('Your csv file has been filtered and saved to %s' % args.dest)

        """
        if file_destination is None:
            file_destination = os.getcwd() + "/filteredcsvfile.csv"
