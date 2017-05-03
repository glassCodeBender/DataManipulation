lf# -*- coding: utf-8 -*-
"""
(@)Author: glassCodeBender
(#)Title: TableFilter.py
(#)Version: 1.0

Program Purpose: Experiment with filtering csv files.

NEED TO ADD __main__ == __name__ and help functionality. 

This program will be periodically updated to include much more functionality.

"""

import pandas as pd

class TableFilter(object):
    def __init__(self, file='', duplicate_column_name='', file_destination = ''):
        self.__file1 = file
        self.__duplicate = duplicate_column_name
        self.__file_dest = file_destination

    """
        Description: Method filters out the unique values in the column of a csv file.
        Return: DataFrame excluding the value
    """
    def populate_df(self):
        try:
            csv_file = self.__file1
            df = pd.DataFrame()
            pop_df = df.from_csv(csv_file)
        except IOError as e:
            print( "I/O error: The file did not import properly." )
        return pop_df

        """        
        Create a column of boolean values 
        Check to see if the previous value in the column is equal
        """
    def filter_df(self):
        dup = self.__duplicate
        pop_df = self.populate_df
        pop_df['Unique'] = ( pop_df[dup] == pop_df[dup].shift() )
        filtered_df = pop_df[ pop_df['Unique'] == False ]
        return filtered_df

    """ Export to filtered DataFrame to CSV file. """
    def export_to_CSV(self):
        fileDestination = self.__file_dest
        df = self.filterDataFrame()
        df.to_csv(fileDestination)
        """
        if __main__ == __name__:
        """


