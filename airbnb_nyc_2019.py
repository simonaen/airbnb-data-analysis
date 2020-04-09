import pandas as pd
import quality_analysis as qa
import helpers
import correctors


# Perform dataset quality analysis for numeric attributes
def numeric_qa(attributes):
    print('Performing dataset quality analysis for numeric attributes...\n')

    columns = ['total_number_of_values', 'percentage_of_missing_values', 'cardinality',
               'min', 'max', '1st_quartile', '3rd_quartile', 'average_median', 'standard_deviation']
    df = pd.DataFrame(columns=columns, index=attributes.columns)

    for col in attributes.columns:
        row = df.loc[col]
        row['total_number_of_values'] = qa.total_number_of_values(attributes[col])
        row['percentage_of_missing_values'] = qa.percentage_of_missing_values(attributes[col])
        row['cardinality'] = qa.cardinality(attributes[col])
        row['min'] = qa.minimum(attributes[col])
        row['max'] = qa.maximum(attributes[col])
        row['average_median'] = qa.average_median(attributes[col])
        row['1st_quartile'] = qa.first_quartile(attributes[col])
        row['3rd_quartile'] = qa.third_quartile(attributes[col])
        row['standard_deviation'] = qa.standard_deviation(attributes[col])

    # helpers.write_csv(df, 'numeric_qa.csv')
    # helpers.print_table(df)
    return df


# Perform dataset quality analysis for category type attributes
def categorical_qa(attributes):
    print('Performing dataset quality analysis for categorical attributes...\n')
    columns = ['total_number_of_values', 'percentage_of_missing_values', 'cardinality',
               'mode', 'frequency_of_mode', 'percentage_value_of_mode',
               'mode_2', 'frequency_of_mode_2', 'percentage_value_of_mode_2']
    df = pd.DataFrame(columns=columns, index=attributes.columns)

    for col in attributes.columns:
        row = df.loc[col]
        row['total_number_of_values'] = qa.total_number_of_values(attributes[col])
        row['percentage_of_missing_values'] = qa.percentage_of_missing_values(attributes[col])
        row['cardinality'] = qa.cardinality(attributes[col])
        row['mode'] = qa.mode(attributes[col], 0)
        row['frequency_of_mode'] = qa.frequency_of_mode(attributes[col], 0)
        row['percentage_value_of_mode'] = qa.percentage_value_of_mode(attributes[col], 0)
        row['mode_2'] = qa.mode(attributes[col], 1)
        row['frequency_of_mode_2'] = qa.frequency_of_mode(attributes[col], 1)
        row['percentage_value_of_mode_2'] = qa.percentage_value_of_mode(attributes[col], 1)

    # helpers.write_csv(df, 'categorical_qa.csv')
    # helpers.print_table(df)
    return df


def main():
    # 1. Read data
    airbnbs = helpers.read_data('airbnb_nyc_2019.csv')
    # Convert 'object' type attributes to 'category' type for correct storing of data attributes
    airbnbs = helpers.categorize(airbnbs)

    # Define numerical/categorical attributes
    numeric_attributes = airbnbs.iloc[:, [3, 4, 6, 7, 8, 9, 10, 11]].copy()
    categorical_attributes = airbnbs.iloc[:, [0, 1, 2, 5]].copy()

    # 2.Perform quality analysis for numeric data
    num_qa = numeric_qa(numeric_attributes)
    # 3.Perform quality analysis for categorical data
    cat_qa = categorical_qa(categorical_attributes)

    # 4.Draw histograms of attributes
    # helpers.histogram(airbnbs)
# Draw histogram for every attribute
    # for col in airbnbs.columns:
    #     helpers.single_histogram(airbnbs[col], col)

    # 5.Correcting data ('availability_365', 'calculated_host_listings_count', 'price')
    corrected = correctors.remove_zero(airbnbs, ['availability_365', 'calculated_host_listings_count', 'price'])
    # helpers.single_histogram(corrected['availability_365'], 'availability_365')
    # helpers.single_histogram(corrected['calculated_host_listings_count'], 'calculated_host_listings_count')
    # helpers.single_histogram(corrected['price'], 'price')


    # 6. Draw scatter plot
    # Draw SPLOM
    # helpers.splom(airbnbs.iloc[:, [6, 7, 8, 9, 10, 11]].copy())
    # Draw scatter plot for min_nights/price
    # helpers.scatter_plot(airbnbs, 'price', 'minimum_nights', 'Price per night/Minimum nights scatter plot')
    # # Draw scatter plot for availability_365/price
    # helpers.scatter_plot(airbnbs, 'price', 'availability_365', 'Price per night/Available days out of 365')
    # # Draw scatter plot for number_of_reviews/price
    # helpers.scatter_plot(airbnbs, 'number_of_reviews', 'price', 'Price per night/Number of reviews')
    # # Draw scatter plot for availability_365/number_of_reviews
    # helpers.scatter_plot(airbnbs, 'availability_365', 'number_of_reviews', 'Available days out of 365/Number of reviews')
    # # Draw bar chart for categorical data
    # helpers.bar_chart_categorical(airbnbs, 'room_type', 'neighbourhood_group')
    # helpers.bar_chart(airbnbs, 'room_type')
    # Draw bar chart for mixed data
    helpers.box_plot(airbnbs, 'minimum_nights', 'room_type')
    # helpers.box_plot(airbnbs, 'price', 'neighbourhood_group')

    # 7. Correlation and covariance values
    helpers.write_corr_cov_tables(airbnbs)

    # 8. Normalize
    normalized_airbnbs = helpers.normalize(airbnbs)


    # 9. Convert categorical data to numeric type variables
    helpers.categorical_to_numerical(airbnbs)


    # 8. Normalize data



if __name__ == "__main__":
    main()
