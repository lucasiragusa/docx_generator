import pandas as pd

def read_airport_data(filepath):
    return pd.read_pickle(filepath)

def filter_ssim_records(df):
    return df[df['Record type'] == 3]

def merge_country_data(df, df_airports):
    # Merge country of departure airport
    df = pd.merge(left=df, right=df_airports[['iata_code', 'iso_country']], left_on='Dept Stn', right_on='iata_code')
    df.rename(columns={'iso_country': 'Departure_country'}, inplace=True)
    df.drop(columns='iata_code', inplace=True)

    # Merge country of arrival airport
    df = pd.merge(left=df, right=df_airports[['iata_code', 'iso_country']], left_on='Arvl Stn', right_on='iata_code')
    df.rename(columns={'iso_country': 'Arrival_country'}, inplace=True)
    df.drop(columns='iata_code', inplace=True)

    return df

def read_ssim (ssim, df_airports): 

    # Input constants for headers (list of strings) and column length (list of tuples)
    col_headers = ['Record type','Operational suffix',
    'Airline designator','Flight number',
    'Itinerary variation identifier','Leg sequence Number',
    'Service Type','Eff','Dis',
    'Day(s) of operation','Frequency rate','Dept Stn',
    'Dept time (pax)','Dept time (AC)',
    'UTC/Local Time variation (dept)','Passenger terminal',
    'Arvl Stn','Arvl time (AC)','Arvl time (pax)',
    'UTC/Local Time variation','Passenger terminal',
    'Equipment','PRBD','PRBM','Meal service note',
    'Joint operation Airline designators',
    'MCT Status','Secure flight Indicator',
    'Itinerary variation identifier Overflow','Aircraft owner',
    'Cockpit crew employer','Cabin crew employer',
    'Onward Airline designator','Onward Flight number',
    'Aircraft rotation layover','Onward Operational suffix',
    'Automated Check-in','Flight transit layover',
    'Operating airline','Traffic restriction code',
    'Traffic restriction code leg overflow indicator',
    'Aircraft configuration','Date variation',
    'Record serial number']

    cols_to_keep = [
    'Airline designator',
    'Flight number',
    'Service Type',
    'Eff',
    'Dis',
    'Day(s) of operation',
    'Dept Stn',
    'Dept time (pax)', 
    'Arvl Stn',
    'Arvl time (pax)',
    'Equipment', 
    'Aircraft configuration']

    col_length = [(0,1),(1,2),
    (2,5),(5,9),
    (9,11),(11,13),
    (13,14),(14,21),(21,28),
    (28,35),(35,36),(36,39),
    (39,43),(43,47),
    (47,52),(52,54),
    (54,57),(57,61),(61,65),
    (65,70),(70,72),
    (72,75),(75,95),(95,100),(100,110),
    (110,119),
    (119,121),(121,122),
    (127,128),(128,131),
    (131,134),(134,137),
    (137,140),(140,144),
    (144,145),(145,146),
    (146,147),(147,148),
    (148,149),(149,160),
    (160,161),
    (172,192),(192,194),
    (194,200)]

# Read SSIM file and split into appropriate column length & filter for flights only
    df = pd.read_fwf(ssim, widths=[t[1] - t[0] for t in col_length])
    df.columns = col_headers

    # Filter rows and columns
    df = filter_ssim_records(df)
    df = df[cols_to_keep]

    # Merge country data
    df = merge_country_data(df, df_airports)

    # Create unique country list
    country_list = pd.concat([df['Departure_country'], df['Arrival_country']]).unique().tolist()

    d = {}
    for country in country_list:
        d[country] = pd.DataFrame(df[(df['Departure_country'] == country) | (df['Arrival_country'] == country)])
    return d