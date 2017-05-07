# -*- coding: utf-8 -*-
"""
(@)Author: glassCodeBender
(#)Title: tablefilter.py
(#)Version: 1.0

Message me if you want me to add any functionality to the program, if you'd like me to write a subclass of the program,
or if you want to hire me for a job. I also know Scala and Java pretty well. 

WARNING: The program does not currently work from the commandline. However, the main aspects of the program work. I already
used them to filter out duplicate names from an excel document. Also, the --compare functionality has not been added yet.

Program Purpose: Program allows users to remove duplicate values from a column in a csv file (or from an Excel document 
that was converted to a csv). The actual purpose of the program was to remove duplicate rows from an excel table so that 
I could use the sample data in a database for a school project.

Inputs:
__file : Accepts String filename. Currently accepts only csv files.
__column : Accepts a String. User determines the name of the column to remove duplicate rows based on 
    - I used 'Customer Name' in my program to remove duplicate customers.
__file_dest : Determines where the newly created csv file should save to. 
    - I need to rewrite the program so that it saves to the default working directory when I add commandline arguments.
__compare : Allows the user to determine an operator (>, <, !=, =) that they want to use to filter a value. 
__comp_value : Accepts a String, Float, or Integer that the user wants to filter a column compared to.

This program will be periodically updated to include much more functionality.
"""

import pandas as pd
import argparse
import os
import sys

class TableFilter(object):

    def __init__(self, file18 = '', column_name = '', file_destination = '', comparison_op = '', comparison_value = '', rm_duplicates = False ):
        self.__file = file18
        self.__column = column_name
        self.__file_dest = file_destination
        self.__compare = comparison_op
        self.__comp_value = comparison_value
        self.__rmdup = rm_duplicates

    """ Description: Method filters out the unique values in the column of a csv file.
        Return: DataFrame excluding the duplicate values """

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
        assert rm_duplicates

        dup = self.__column
        pop_df = self.populate_df
        pop_df['Unique'] = (pop_df[dup] == pop_df[dup].shift())
        filtered_df = pop_df[pop_df['Unique'] == False]
        return filtered_df


    """ Allows users to filter a column based on a given value and an operator 
        Returns: DataFrame with filtered content. """

    def filter_by(self):
        comparison_op = self.__compare.upper()
        comparison_value = self.__comp_value
        column = self.__column
        pop_df = self.populate_df()
        
        # compare number values
        if isinstance(comparison_value, int) or isinstance(comparison_value, float):
            if comparison_op == 'EQ' or comparison_op == 'NEQ' or comparison_op == 'LTE' or comparison_op == 'GTE' or comparison_op == 'LT' or comparison_op == 'GT':
                if comparison_op == 'EQ':
                    df = pop_df[pop_df[column] == comparison_value]
                elif comparison_op == 'NEQ':
                    df = pop_df[pop_df[column] != comparison_value]
                elif comparison_op == 'LTE':
                    df = pop_df[pop_df[column] <= comparison_value]
                elif comparison_op == 'GTE':
                    df = pop_df[pop_df[column] >= comparison_value]
                elif comparison_op == 'LT':
                    df = pop_df[pop_df[column] < comparison_value]
                elif comparison_op == 'GT':
                    df = pop_df[pop_df[column] > comparison_value]
                else:
                    raise IOError("An exception was raised because you have deep psychological issues that affected your ability to use commandline tools.\n"
                                  "\n\tOnly 'EQ', 'NEQ', 'LTE', 'GTE', 'LT', or 'GT' can be used as operators.")
        # compare string values       
        if isinstance(comparison_value, str):
            if comparison_op == 'EQ':
                df = pop_df[pop_df[column].upper() == comparison_value.upper()]
            elif comparison_op == 'NEQ':
                df = pop_df[pop_df[column].upper() == comparison_value.upper()]
            else:
                raise IOError(
                    'An error occurred because you have deep psychological issues that affected your ability to use commandline tools.\n'
                    '\n\tONLY "EQ" and "NEQ" operations can performed when comparing values that include letters.')

        # NEED TO ADD DATETIME functionality!!!!!!!!
        return df

    """ Allows users to apply both filter unique columns out and filter by an operator
        Returns: DataFrame """

    def unique_and_filter(self):
        comparison_op, comparison_value, rm_dup, column = self.__compare, self.__comp_value, self.__rmdup, self.__column
        pop_df = self.filter_uniq()

        if isinstance(comparison_value, int) or isinstance(comparison_value, float):
            if comparison_op == 'EQ' or comparison_op == 'NEQ' or comparison_op == 'LTE' or comparison_op == 'GTE' or comparison_op == 'LT' or comparison_op == 'GT':
                if comparison_op == 'EQ':
                    df = pop_df[pop_df[column] == comparison_value]
                elif comparison_op == 'NEQ':
                    df = pop_df[pop_df[column] != comparison_value]
                elif comparison_op == 'LTE':
                    df = pop_df[pop_df[column] <= comparison_value]
                elif comparison_op == 'GTE':
                    df = pop_df[pop_df[column] >= comparison_value]
                elif comparison_op == 'LT':
                    df = pop_df[pop_df[column] < comparison_value]
                elif comparison_op == 'GT':
                    df = pop_df[pop_df[column] > comparison_value]
                else:
                    raise IOError(
                        "An exception was raised because you have deep psychological issues that affected your ability to use commandline tools.\n"
                        "\n\tOnly 'EQ', 'NEQ', 'LTE', 'GTE', 'LT', or 'GT' can be used as operators.")
        # compare string values       
        if isinstance(comparison_value, str):
            if comparison_op == 'EQ':
                df = pop_df[pop_df[column].upper() == comparison_value.upper()]
            elif comparison_op == 'NEQ':
                df = pop_df[pop_df[column].upper() == comparison_value.upper()]
            else:
                raise IOError(
                    'An error occurred because you have deep psychological issues that affected your ability to use commandline tools.\n'
                    '\n\tONLY "EQ" and "NEQ" operations can performed when comparing values that include letters.')
        return df
 
    """ Export to filtered DataFrame to CSV file. """

    def export_to_CSV(self):
        file_destination = self.__file_dest
        comp_op, comp_val, rm_dup = self.__compare, self.__comp_value, self.__rmdup
        response = ''

        if rm_dup and comp_op and comp_val:
            response = input('You indicated that you want to both exclude duplicate values from a column and filter the column by a value. Are you sure you want to do this? '
                  '\n\nEnter "y" to export two different CSV files, "b" to both remove duplicates and filter, "n" to close the program, "d" to remove duplicates, or "f" to filter by the value entered: ')
            
            if response.upper() == 'Y':
                df = self.filter_uniq()
                df1 = self.filter_by()
            elif response.upper() == 'B':
                df = self.unique_and_filter()
            elif response.upper() == 'N':
                sys.exit(1)
            elif response.upper() == 'D':
                df = self.filter_uniq()
            elif response.upper() == 'F':
                df = self.filter_by()
            else:
                raise IOError ("Something when wrong while attempting to export the formatted data to a CSV file.")

        if rm_dup and comp_op and comp_val and response == 'Y':

            df.to_csv(file_destination)
            df1.to_csv(file_destination + 'filtered')
            print( 'You indicated that you both want to exclude duplicate values from a column and filter a column by a value. \n'
                   'We output the filtered column to ' + file_destination + 'filtered' )
            sys.exit(0)
    
        elif comp_op and comp_val:
            df.to_csv(file_destination)
        elif rm_dup:
            df.to_csv(file_destination)
        else:
            print( 'You indicated that you both want to exclude duplicate values from a column and filter a column by a value. \n'
                   'As a result, we output the filtered column to ' + file_destination + 'filtered' )
            
    

    """ Process command-line arguments. """
    if __name__ == '__main__':

        """ Create commandline functionality to the program """
        parser = argparse.ArgumentParser( add_help = True, description = "Allows users to filter CSV file in a variety of ways." )

        # NEED TO ADD PARSER GROUP CALLED 'Positional Arguments'
        # parse.add_argument_group()
        parser.add_argument( '-f', '--file', dest = 'store', dest = 'file', help='Store the name of the csv file you want converted' )
        parser.add_argument( '-n', '--column', action = 'store', dest = 'column', help='Store the name of the column you want filtered.' )
        parser.add_argument( '-r', '--rmdup', action = 'store_true', dest = 'rmdup', help = 'If -r is added to your command, the program will remove all duplicates of the value passed to --column.')
        # NEED TO ADD PARSER GROUP CALLED 'Optional Arguments'
        # parser.add_argument_group()
        parser.add_argument( '-d', '--dest', action = 'store', dest = 'file_destination', default= str( os.getcwd() ) + "/filteredcsvfile.csv",
                                                                                          help = "Store the name of the file you'd like the program to create" )
        parser.add_argument( '-c', '--compare', action = 'store', dest = 'compare', help = 'Command allows user to filter a column based on an operator passed to -c and '
                                                                                           'a value (String or Float) passed to -z. \n'
                                                                                           'Accepted Values: \n\t"gt" for greater than, '
                                                                                           '\n"lt" for less than, '
                                                                                           '\n"ne" for not equal" '
                                                                                            '\n"lte" for less than or equal'
                                                                                           '\n"gte" for greater than or equal to'
                                                                                            '\n"eq" for equals' )
        parser.add_argument( '-z', '--value', action = 'store', dest = 'comp_value', help = 'Enter a value that you want to filter a column by. \n'
                                                                                            'For example: The following command will filter out all rows where "Gross Sales" was less than 30'
                                                                                            '\n~$ python tablefilter.py -f myfile.csv -n "Gross Sales" -c lt -z 30')
        parser.add_argument( '-v', '--verbose', action = 'store_true', help = 'Increase the verbosity of the program.' )

        if len(sys.argv) <= 2:
            parser.print_help()
            sys.exit(1)

        # moving parsed arguments to local variables just to be safe
        args = parser.parse_args()
        file = args.file
        file_dest = args.file_destination
        column = args.column
        compare = args.compare 
        rmdup = args.rmdup


        assert os.path.exists( str(os.getcwd()) + '/' + file )

        filter_object = TableFilter( file, column, file_dest, compare, rmdup)
        filter_object.export_to_CSV()

        if args.verbose:
            assert isinstance( file_dest )
            print( 'Your csv file has been filtered and saved to %s' % file_dest )

        """
        if file_destination is None:
            file_destination = os.getcwd() + "/filteredcsvfile.csv"
            """
