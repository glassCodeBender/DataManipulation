# -*- coding: utf-8 -*-
"""
(@)Author: glassCodeBender
(#)Title: tablefilter.py
(#)Version: 1.0

Writer's Note: Message me if you want me to add any functionality to the program, if you'd like me to write a subclass 
of the program or if you want to hire me for a job. I also know Scala and Java pretty well. I wrote the tablefilter.py
in less than 2 days and I wrote the core components of the program (filter_unique() in less than 45 minutes.

WARNING: This program is a work in progress, but the main aspects of the program should work. I already used the 
program logic to filter out duplicate names from an excel document in iPython. 

Program Purpose: Program allows users to filter columns in a csv file. Users can either remove duplicate values from 
a column or filter the column based on the operators "eq" (equals), "neq" (not equal), "lt" (less than), "gt" (greater than)
"lte" (less than or equal to), "gte" (greater than or equal to). "get. The actual purpose of the program was to remove 
duplicate rows from an excel table so that I could use the sample data in a database for a school project.

Inputs:
__file : Accepts String filename. Currently accepts only csv files.
__column : Accepts a String. User determines the name of the column to remove duplicate rows based on 
    - I used 'Customer Name' in my program to remove duplicate customers.
__file_dest : Determines where the newly created csv file should save to. 
    - I need to rewrite the program so that it saves to the default working directory when I add commandline arguments.
__compare : Allows the user to determine an operator (>, <, !=, =) that they want to use to filter a value. 
__comp_value : Accepts a String, Float, or Integer that the user wants to filter a column compared to.
__rmdup : Accepts a Boolean that determines whether or not the user wants to remove duplicate values from a column.

"""

import pandas as pd
import argparse
import os
import sys

class TableFilter(object):

    def __init__(self, file18 = '', column_name = '', file_destination = '', comparison_op = '', comparison_value = '',
                 rm_duplicates = False):
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
            print("I/O error: The file did not import properly.")
        return pop_df

    """ Description: Filters rows in a 2D array to only include the first occurrence of a value in a given column
        Returns: DataFrame """

    def filter_uniq(self):
        rm_duplicates = self.__rmdup
        assert rm_duplicates

        dup = self.__column
        pop_df = self.populate_df
        pop_df['Unique'] = ( pop_df[dup] == pop_df[dup].shift() )
        filtered_df = pop_df[pop_df['Unique'] == False]
        filtered_df.drop( 'Unique', axis = 1, inplace = True )
        return filtered_df

    """ Description: Allows users to filter a column based on a given value and an operator 
        Returns: DataFrame with filtered content. """

    def filter_by(self):
        comparison_op = self.__compare.upper()
        comparison_value = self.__comp_value
        column = self.__column
        pop_df = self.populate_df()

        # compare number values
        if isinstance(comparison_value, int) or isinstance(comparison_value, float):
            if comparison_op == 'EQ' or comparison_op == 'NE' or comparison_op == 'LTE' or comparison_op == 'GTE' or comparison_op == 'LT' or comparison_op == 'GT':
                if comparison_op == 'EQ':
                    pop_df['Result'] = (pop_df[column] == comparison_value)
                elif comparison_op == 'NE':
                    pop_df['Result'] = (pop_df[column] != comparison_value)
                elif comparison_op == 'LTE':
                    pop_df['Result'] = (pop_df[column] <= comparison_value)
                elif comparison_op == 'GTE':
                    pop_df['Result'] = (pop_df[column] >= comparison_value)
                elif comparison_op == 'LT':
                    pop_df['Result'] = (pop_df[column] < comparison_value)
                elif comparison_op == 'GT':
                    pop_df['Result'] = (pop_df[column] > comparison_value)
                else:
                    raise IOError(
                        "An exception was raised because you have deep psychological issues that affected your ability to use commandline tools.\n"
                        "\n\tOnly 'EQ', 'NE', 'LTE', 'GTE', 'LT', or 'GT' can be used as operators.")

        # compare string values
        elif isinstance(comparison_value, str) and isinstance(pop_df[column], str):
            if comparison_op == 'EQ':
                pop_df['Result'] = (pop_df[column].upper() == comparison_value.upper())
            elif comparison_op == 'NE':
                pop_df['Result'] = (pop_df[column].upper() != comparison_value.upper())
            else:
                raise IOError(
                    'An error occurred because you have deep psychological issues that affected your ability to use commandline tools.\n'
                    '\n\tONLY "EQ" and "NE" operations can performed when comparing values that include letters.')
        else:
            raise ValueError("Something went wrong when attempting to compare the value you entered and the values in the column. "
                            "\nColumns made up of numbers can only be compared to numbers and columns made up of words can only be compared to words.")
        # NEED TO ADD DATETIME functionality!!!!!!!!
        df = pop_df[pop_df['Result'] == True]
        df.drop('Result', axis = 1, inplace = True)
        return df

    """ Description: Allows users to apply both filter unique columns out and filter by an operator
        Returns: DataFrame """

    def unique_and_filter(self):
        comparison_op, comparison_value, rm_dup, column = self.__compare, self.__comp_value, self.__rmdup, self.__column
        pop_df = self.filter_uniq()

        # compare number values
        if isinstance(comparison_value, int) or isinstance(comparison_value, float):
            if comparison_op == 'EQ' or comparison_op == 'NE' or comparison_op == 'LTE' or comparison_op == 'GTE' or comparison_op == 'LT' or comparison_op == 'GT':
                if comparison_op == 'EQ':
                    pop_df['Result'] = (pop_df[column] == comparison_value)
                elif comparison_op == 'NE':
                    pop_df['Result'] = (pop_df[column] != comparison_value)
                elif comparison_op == 'LTE':
                    pop_df['Result'] = (pop_df[column] <= comparison_value)
                elif comparison_op == 'GTE':
                    pop_df['Result'] = (pop_df[column] >= comparison_value)
                elif comparison_op == 'LT':
                    pop_df['Result'] = (pop_df[column] < comparison_value)
                elif comparison_op == 'GT':
                    pop_df['Result'] = (pop_df[column] > comparison_value)
                else:
                    raise IOError(
                        "An exception was raised because you have deep psychological issues that affected your ability to use commandline tools.\n"
                        "\n\tOnly 'EQ', 'NE', 'LTE', 'GTE', 'LT', or 'GT' can be used as operators.")

        # compare string values
        elif isinstance(comparison_value, str) and isinstance(pop_df[column], str):
            if comparison_op == 'EQ':
                pop_df['Result'] = (pop_df[column].upper() == comparison_value.upper())
            elif comparison_op == 'NE':
                pop_df['Result'] = (pop_df[column].upper() != comparison_value.upper())
            else:
                raise IOError(
                    'An error occurred because you have deep psychological issues that affected your ability to use commandline tools.\n'
                    '\n\tONLY "EQ" and "NE" operations can performed when comparing values that include letters.')
        else:
            raise ValueError("Something went wrong when attempting to compare the value you entered and the values in the column. "
                            "\nColumns made up of numbers can only be compared to numbers and columns made up of words can only be compared to words.")
        # NEED TO ADD DATETIME functionality!!!!!!!!
        df = pop_df[pop_df['Result'] == True]
        df.drop('Result', axis = 1, inplace = True)
        return df

    """ Description: Export to filtered DataFrame to CSV file. 
        Return: Void """

    def export_to_CSV(self):
        file_destination = self.__file_dest
        comp_op, comp_val, rm_dup = self.__compare, self.__comp_value, self.__rmdup
        response = ''

        if rm_dup and comp_op and comp_val:
            response = input(
                'You indicated that you want to both exclude duplicate values from a column and filter the column by a value. Are you sure you want to do this? '
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
                raise IOError("Something when wrong while attempting to export the formatted data to a CSV file.")

        if rm_dup and comp_op and comp_val and response == 'Y':
            df.to_csv(file_destination)
            df1.to_csv(file_destination + 'filtered')

            print(
                'You indicated that you both want to exclude duplicate values from a column and filter a column by a value. \n'
                'We output the filtered column to ' + file_destination + 'filtered')
            sys.exit(0)
        else:
            df.to_csv(file_destination)
            sys.exit(0)

    """ Process command-line arguments. """
    if __name__ == '__main__':

        """ Add commandline help functionality to the program """
        parser = argparse.ArgumentParser(add_help = True,
                                         description = 'Allows users to filter a CSV file in a variety of ways.\n'
                                                       'Sample usage: '
                                                       '\n\n\t~$ python tablefilter.py -f myfile.csv -n "Daily Sales" -d destination_file.csv -c gte -z 250')

        # NEED TO ADD PARSER GROUP CALLED 'Positional Arguments'
        # parse.add_argument_group()
        parser.add_argument('-f', '--file', action = 'store', dest = 'file',
                            help = 'Store the name of the csv file you want converted')
        parser.add_argument('-n', '--column', action = 'store', dest ='column',
                            help = 'Store the name of the column you want filtered.')
        parser.add_argument('-r', '--rm', action = 'store_true', dest = 'rm',
                            help = 'If -r is added to your command, the program will remove all duplicates of the value passed to --column.')
        # NEED TO ADD PARSER GROUP CALLED 'Optional Arguments'
        # parser.add_argument_group()
        parser.add_argument('-d', '--dest', action = 'store', dest = 'file_destination',
                            default = str(os.getcwd()) + "/filteredcsvfile.csv",
                            help = "Store the name of the file you'd like the program to create")
        parser.add_argument('-c', '--compare', action = 'store', dest = 'compare',
                            help = 'Command allows user to filter a column based on an operator passed to -c and '
                                 'a value (String or Float) passed to -z. \n'
                                 'Accepted Values: \n\t"gt" for greater than, '
                                 '\n"lt" for less than, '
                                 '\n"ne" for not equal" '
                                 '\n"lte" for less than or equal'
                                 '\n"gte" for greater than or equal to'
                                 '\n"eq" for equals')
        parser.add_argument('-z', '--value', action = 'store', dest = 'comp_value',
                            help = 'Enter a value that you want to filter a column by. \n'
                                 'For example: The following command will filter out all rows where "Gross Sales" was less than 30'
                                 '\n~$ python tablefilter.py -f myfile.csv -n "Gross Sales" -c lt -z 30')
        parser.add_argument('-v', '--verbose', action = 'store_true', help = 'Increase the verbosity of the program.')

        if len(sys.argv) <= 2:
            parser.print_help()
            sys.exit(1)

        # moving parsed arguments to local variables just to be safe
        args = parser.parse_args()
        file = args.file
        file_dest = args.file_destination
        column = args.column
        compare = args.compare
        rmduplicate = args.rm

        assert os.path.exists( str(os.getcwd()) + '/' + file )

        filter_object = TableFilter(file, column, file_dest, compare, rmduplicate)
        filter_object.export_to_CSV()

        if args.verbose:
            assert isinstance(file_dest)
            print('Your csv file has been filtered and saved to %s' % file_dest)

        """
        if file_destination is None:
            file_destination = os.getcwd() + "/filteredcsvfile.csv"
            """
