import pandas as pd

def filter_by_country(ssim_data, country_code):
    """
    Filters the SSIM data by the specified country (either as departure or arrival).

    Args:
        ssim_data (dict): A dictionary of DataFrames containing the SSIM data.
        country_code (str): The ISO country code to filter by.

    Returns:
        dict: A dictionary of filtered DataFrames for the specified country.
    """
    filtered_data = {}
    for key, df in ssim_data.items():
        filtered_df = df[(df['Departure_country'] == country_code) | (df['Arrival_country'] == country_code)]
        if not filtered_df.empty:
            filtered_data[key] = filtered_df

    return filtered_data


def filter_by_service_type(ssim_data, service_type):
    """
    Filters the SSIM data by the specified service type.

    Args:
        ssim_data (dict): A dictionary of DataFrames containing the SSIM data.
        service_type (str): The service type to filter by.

    Returns:
        dict: A dictionary of filtered DataFrames for the specified service type.
    """
    filtered_data = {}
    for key, df in ssim_data.items():
        filtered_df = df[df['Service Type'] == service_type]
        if not filtered_df.empty:
            filtered_data[key] = filtered_df

    return filtered_data

def filter_by_country_and_service_type(df, country_code, service_type):
    """
    Filter a DataFrame by country code (either Departure_country or Arrival_country)
    and Service Type.

    Args:
        df (pandas.DataFrame): The DataFrame to filter.
        country_code (str): The ISO country code to filter by.
        service_type (str): The Service Type to filter by.

    Returns:
        pandas.DataFrame: The filtered DataFrame.
    """
    filtered_df = df.loc[((df['Departure_country'] == country_code) | (df['Arrival_country'] == country_code)) &
                         (df['Service Type'] == service_type)]
    
    return filtered_df
