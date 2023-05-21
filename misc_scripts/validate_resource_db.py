import sys
import os
import datetime as dt
import yaml
import argparse
import logging
from pathlib import Path
import pandas as pd

from jsonschema import Draft202012Validator, ValidationError


# Add the project root directory to the Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(-1, project_root)
from admin.admin_classes import prodAdmin, betaAdmin, testAdmin

# Import the schema from a YAML file in the same directory
RESOURCE_SCHEMA = Path(__file__).resolve().parent / "water_schema.yaml"

class DataValidator:
    def __init__(self, schema_path, log_path):
        # Load the schema and configure the logger
        with open(schema_path, 'r') as file:
            self.schema = yaml.safe_load(file)
        Draft202012Validator.check_schema(self.schema)
        self.configure_logger(log_path)

    def configure_logger(self, log_path):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        
        # Create a file handler
        handler = logging.FileHandler(log_path)
        handler.setLevel(logging.INFO)
        
        # Create a logging format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        
        # Add the handlers to the logger
        self.logger.addHandler(handler)

    def get_invalid_data(self, df, validator, resource):
        self.logger.info(f"Validating data in dataframe for resource: {resource}...")

        df_cols = df.columns.tolist()
        error_dict = {}
        for i, row in df.iterrows():
            invalid_data = row.to_dict()
            total_errors = 0
            try:
                validator.validate(invalid_data)
            except ValidationError:
                for error in sorted(validator.iter_errors(invalid_data), key=str):
                    self.logger.info(f"Error in row {i}: {error.message}")
                    total_errors += 1
                if resource == "water":
                    if "tapnum" not in df_cols:
                        self.logger.warning("No tapnum column in dataframe. Skipping row...")
                        continue
                    error_dict[i] = {"tapnum": invalid_data["tapnum"], "address": invalid_data["address"], "total_errors": total_errors}
                elif resource == "food":
                    if "foodnum" not in df_cols:
                        self.logger.warning("No foodnum column in dataframe. Skipping row...")
                        continue
                    error_dict[i] = {"foodnum": invalid_data["foodnum"], "address": invalid_data["address"], "total_errors": total_errors}
                elif resource == "forage":
                    if "Planting Site Id" not in df_cols:
                        self.logger.warning("No foragenum column in dataframe. Skipping row...")
                        continue
                    error_dict[i] = {"Planting_Site_Id": invalid_data["Planting Site Id"], "Street_Address": invalid_data["Street Address"], "total_errors": total_errors}
                else:
                    self.logger.warning(f"Unknown resource: {resource}. Skipping row {i}...")

        return error_dict

    def validate_and_log(self, df, admin_class_name, resource, db_env):
        self.logger.info("\n\n" + "="*60)
        self.logger.info(f"STARTING VALIDATION: {admin_class_name.upper()} DATABASE")
        self.logger.info("="*60 + "\n")

        validator = Draft202012Validator(self.schema)
        error_dict = self.get_invalid_data(df, validator, resource)

        if len(error_dict) == 0:
            self.logger.info("\t\tData is valid.")
        else:
            self.logger.info("\t\tData is invalid.")
            # Log the schema errors to a file
            csv_name = f"{resource}_{admin_class_name.lower()}_{db_env}_schema_errors_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
            csv_fp = validation_results_dir / csv_name
            error_df = pd.DataFrame.from_dict(error_dict, orient='index')
            error_df.to_csv(csv_fp, index=False)
            self.logger.info(f"\n\nSchema errors logged to {csv_fp}")

            for key, value in error_dict.items():
                self.logger.info(f"Row {key} Errors: {value}")

            self.logger.info(f"Total number of rows with errors: {len(error_dict)}")

        self.logger.info("\n" + "="*60)
        self.logger.info(f"FINISHED VALIDATION: {admin_class_name.upper()} DATABASE")
        self.logger.info("="*60 + "\n\n")

def eda_water_resource(df):
    # exploratory data analysis
    logging.info(f"Dataframe shape: {df.shape}")
    logging.info(f"Dataframe columns: {df.columns.tolist()}")
    
    # filter any columns without tamnum 
    df = df[df['tapnum'].notna()]
    logging.info(f"Dataframe shape after filtering on Null Taps: {df.shape}")

    # which rows  have null addresses? or empty strings?
    null_addresses = df[df['address'].isna() | df['address'].str.strip().eq('')]
    logging.info(f"Number of rows with null addresses: {len(null_addresses)}")

    # which rows have null lat/long?
    null_latlong = df[df['lat'].isna() | df['lon'].isna()]
    logging.info(f"Number of rows with null lat/long: {len(null_latlong)}")

    # WHICH ROWS HAVE NULL ZIP CODES?
    null_zip = df[df['zip_code'].isna()]
    logging.info(f"Number of rows with null zip codes: {len(null_zip)}")

    # Filter for non-null and non-empty zip codes
    df2 = df[df['zip_code'].notna() & df['zip_code'].str.strip().ne('')]
    logging.info(f"Most common zip codes (zip / count): {df2['zip_code'].value_counts().head(10)}")

    # how many with handicapped access?
    logging.info(f"Number of rows with handicapped access: {len(df[df['handicap'] == True])}")

    # type of quality by count
    logging.info(f"Quality by count: {df['quality'].value_counts()}")

    count_hours_too_short = len(df[df['hours'].str.len() < 5])
    count_hours_too_long = len(df[df['hours'].str.len() > 7])
    logging.info(f"Number of rows with hours too short: {count_hours_too_short}")
    logging.info(f"Number of rows with hours too long: {count_hours_too_long}")

    # analyze hours contents
    analyze_business_hours(df, 'hours')

    # duplicate addresses?
    duplicate_addresses = df[df.duplicated(subset=['address'], keep=False)]
    logging.info(f"Number of rows with duplicate addresses: {len(duplicate_addresses)}")

    if len(duplicate_addresses) > 0:
        logging.info(f"\t\t !! Found {len(duplicate_addresses)} duplicate addresses:")

        # print duplicating addresses line by line
        for i, row in duplicate_addresses.iterrows():
            logging.info(f"{row['address']}")


def analyze_business_hours(df, col):
    """
    This function analyzes a DataFrame column containing business hours, given as a list of dictionaries,
    and prints the count of businesses open during the morning, evening, and night for each weekday.

    :param df: DataFrame - DataFrame containing business hours data
    :param col: str - Name of the column in the DataFrame containing business hours data
    """
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    periods = ['Morning', 'Evening', 'Night']
    
    business_hours = {day: {period: 0 for period in periods} for day in days}
    
    for hours in df[col]:
        if isinstance(hours, list):
            daily_hours = {day: {period: False for period in periods} for day in days}
            for hour in hours:
                if 'open' in hour and 'time' in hour['open'] and 'day' in hour['open']:
                    opening_time = int(hour['open']['time'])
                    opening_day = int(hour['open']['day'])
                    
                    if 600 <= opening_time < 1200:
                        daily_hours[days[opening_day % 7]]['Morning'] = True
                    elif 1200 <= opening_time < 1800:
                        daily_hours[days[opening_day % 7]]['Evening'] = True
                    else:
                        daily_hours[days[opening_day % 7]]['Night'] = True

                if 'close' in hour and 'time' in hour['close'] and 'day' in hour['close']:
                    closing_time = int(hour['close']['time'])
                    closing_day = int(hour['close']['day'])

                    if closing_time < 600:
                        daily_hours[days[closing_day % 7]]['Morning'] = True
                    elif closing_time < 1200:
                        daily_hours[days[closing_day % 7]]['Evening'] = True
                    else:
                        daily_hours[days[closing_day % 7]]['Night'] = True
            
            # If the business is open during a particular period on a particular day, increment the count
            for day in days:
                for period in periods:
                    if daily_hours[day][period]:
                        business_hours[day][period] += 1
    
    logging.info('Business hours breakdown:')
    for day in days:
        logging.info(f'{day}:')
        for period in periods:
            logging.info(f'  {period}: {business_hours[day][period]}')




# def validate_and_log(df, validator, admin_class_name):
#     logging.info("\n\n" + "="*60)
#     logging.info(f"STARTING VALIDATION: {admin_class_name.upper()} DATABASE")
#     logging.info("="*60 + "\n")

#     error_dict = get_invalid_data(df, validator)
#     if len(error_dict) == 0:
#         logging.info("\t\tData is valid.")
#     else:
#         logging.info("\t\tData is invalid.")
#         csv_name = f"{admin_class_name.lower()}_schema_errors_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
#         csv_fp = Path(__file__).resolve().parent / "validation_results" / csv_name
#         error_df = pd.DataFrame.from_dict(error_dict, orient='index')
#         error_df.to_csv(csv_fp)
#         logging.info(f"\n\nSchema errors logged to {csv_fp}")
                
#         for key, value in error_dict.items():
#             logging.info(f"Row {key} Errors: {value}")

#         logging.info(f"Total number of rows with errors: {len(error_dict)}")

#     logging.info("\n" + "="*60)
#     logging.info(f"FINISHED VALIDATION: {admin_class_name.upper()} DATABASE")
#     logging.info("="*60 + "\n\n")

def main():
    """ validate_db.py
    Entry point for the script. This function initializes the schema validator with a specified schema and
    log file path. It then loops over a list of databases in production, beta, and testing environments. For each database,
    it pulls data, converts it into a DataFrame, conducts data analysis, and validates the data against the 
    specified JSON schema. Validation results and logs are written to a specified log file, and if any schema 
    validation errors are found, they are written to a separate CSV file.
    
    :return: None
    """
    parser = argparse.ArgumentParser(description='Validate a specific resource database.')
    parser.add_argument('resource', type=str, help='The type of resource to validate')
    args = parser.parse_args()

    # get the resource name from the command line arguments
    resource = args.resource
    RESOURCE_SCHEMA = Path(__file__).resolve().parent / f"{resource}_schema.yaml"

    # set up logging based on the resource name
    global validation_results_dir

    validation_results_dir = Path(__file__).resolve().parent / "validation_results" / resource 
    validation_results_dir.mkdir(parents=True, exist_ok=True)
    
    # Configure logging and log file
    log_name = f"{resource}_validation_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
    log_fp = validation_results_dir / log_name

    logging.basicConfig(level=logging.INFO, 
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        filename= str(log_fp), 
                        filemode='w')

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
    console.setFormatter(formatter)
    logging.getLogger('').addHandler(console)

    logging.info(f"Starting Script: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    logging.info(f"Using python interpreter: {sys.executable}")

    # Initialize custom validator with schema and log file path
    validator = DataValidator(
    schema_path=RESOURCE_SCHEMA,
    log_path= str(log_fp) )
    
    # Initialize the prod, beta, and test environment database references.
    databases = [
        (getattr(prodAdmin(), f"{resource}_db_live"), prodAdmin),
        (getattr(betaAdmin(), f"{resource}_db_live"), betaAdmin),
        (getattr(testAdmin(), f"{resource}_db_live"), testAdmin)
    ]
    for i, (db, admin_class) in enumerate(databases):
        if i == 0:
            admin_class_name = 'prodAdmin'
            db_env = "prod"
        elif i == 1:
            admin_class_name = 'betaAdmin'
            db_env = "beta"
        else:
            admin_class_name = 'testAdmin'
            db_env = "test"

        # Get the data from the database and convert to a dataframe)
        data = admin_class().getDb(db)
        df = pd.DataFrame(data)

        # print dataframe column names
        logging.info(f"\n\n{admin_class_name.upper()} database column names:\n{df.columns}")

        # exploratory data analysis - Water only
        if resource.lower() == 'water':
            logging.info(f"\n\nExploratory Data Analysis for {admin_class_name.upper()} database:")
            eda_water_resource(df)

        # JSON Schema Validation
        validator.validate_and_log(df, admin_class_name, resource, db_env)
        logging.info(f"\n\nFinished Script: {dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
