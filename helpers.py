import pandas as pd
import os.path
import matplotlib.pyplot as plt
from sklearn import preprocessing
import pandas.plotting as pdplot


# Global settings for pandas table formatting
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)


# Read data from .csv file and return data []
def read_data(file):
    print('....................\nReading data from ' + file + '...')
    with open(file, encoding="utf-8", newline='') as dataset:
        airbnbs = pd.read_csv(dataset, delimiter=',', usecols=[1, 3, 4, 6, 7, 8, 9, 10, 11, 13, 14, 15])
        print('Done!\n....................')
    return airbnbs


# Write table data into a .csv file
def write_csv(df, filename):
    if os.path.isfile(filename) is False:
        print(df.to_csv(filename))
    print('New file (' + filename + ') created')


# Print table in formatted manner onto the console
def print_table(df):
    print(df.to_markdown())
    print('\n.........................................')


# Draw and display histogram
def single_histogram(col, col_name):
    if col.dtype != 'object':
        hist = col.hist(log=True, bins=100)
        plt.title(col_name)
        plt.show()


# Draw and display histogram
def histogram(df):
    hist = df.hist(log=True)
    plt.show()


# Plot scatter plot with numerical data
def scatter_plot(df, x, y, title):
    df.plot(kind='scatter', x=x, y=y, title=title)
    plt.show()


# Provide SPLOM diagram
def splom(df):
    pdplot.scatter_matrix(df)
    plt.show()


# Draw normal bar chart
def bar_chart(df, col):
    df[col].value_counts().plot(kind='bar')
    plt.show()


# Draw bar chart for categorical data
def bar_chart_categorical(df, x, y):
    # Category to state
    all_categories = df[x].unique()

    neighbourhoods = df[y].unique()
    neighbourhoods_count = {}
    for n in neighbourhoods:
        neighbourhoods_count[n] = []

    for category in all_categories:
        mask = df[x] == category
        category_df = df[mask]
        nbhd_count = category_df[y].value_counts()
        for n in neighbourhoods:
            neighbourhoods_count[n].append(nbhd_count.get(n, 0))

    categories_to_state_df = pd.DataFrame(neighbourhoods_count, index=all_categories)
    categories_to_state_df.plot(kind='bar')
    plt.show()


# Draw bar chart for categorical x numerical data relationships
def box_plot(df, col, by):
    df.boxplot(column=col, by=by)
    plt.show()


# Create table of correlation and covariance files
def write_corr_cov_tables(df):
    if os.path.isfile('correlations.csv') is False:
        write_csv(df.corr(method='pearson'), 'correlations.csv')
    print('New file (' + 'correlations.csv' + ') created')

    if os.path.isfile('covariance.csv') is False:
        write_csv(df.cov(), 'covariance.csv')
    print('New file (' + 'covariance.csv' + ') created')


# Change dtype from "object" to "category" for more appropriate metadata
def categorize(df):
    for col_name in df.columns:
        if col_name == 'name' or col_name == 'host_name':
            continue
        if df[col_name].dtype == 'object':
            df[col_name] = df[col_name].astype('category')
    return df


# Convert categorical data to numerical
def categorical_to_numerical(df):
    for col_name in df.columns:
        if str(df[col_name].dtype) == 'category':
            df.loc[:, [col_name]] = df[col_name].cat.codes


def normalize(df):
    x = df.values
    min_max_scalar = preprocessing.MinMaxScaler()
    x_scaled = min_max_scalar.fit_transform(x)
    normalized_df = pd.DataFrame(x_scaled)
    return normalized_df


def remove_outstanding_value(df, value):
    for row in df:
        if row[1] == value:
            row[1] = None
