import pandas as pd
from decimal import Decimal


# General
def total_number_of_values(column):
    return len(column)


def percentage_of_missing_values(column):
    not_null = pd.isnull(column)
    if len(not_null) == len(column):
        return Decimal(0)
    return Decimal(format(len(not_null)/len(column), '.5f'))


def cardinality(column):
    unique = column.unique()
    return unique.size


# Numerical data
def minimum(column):
    return column.min(axis=0,  skipna=True)


def maximum(column):
    return column.max(axis=0,  skipna=True)


def average_median(column):
    return column.median()


def first_quartile(column):
    return column.quantile(0.25)


def third_quartile(column):
    return column.quantile(0.75)


def standard_deviation(column):
    return column.std(axis=0, skipna=True)


# Categorical data
def mode(column, mode_num):
    return column.value_counts().index[mode_num]


def frequency_of_mode(column, mode_num):
    return column.value_counts()[mode_num]


def percentage_value_of_mode(column, mode_num):
    return Decimal(format(frequency_of_mode(column, mode_num)/len(column), '.5f'))