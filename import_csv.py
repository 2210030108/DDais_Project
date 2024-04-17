import os
import django
import csv
import re  # Import the regular expression module

# Manually configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "washing_machine_recommendation.settings")
django.setup()

from recommender.models import WashingMachine


def extract_numeric_value(value):
    try:
        # Try to extract numeric value using regular expression
        numeric_value = re.search(r'\d+(\.\d+)?', value).group()
        return float(numeric_value)  # Convert the numeric part to float
    except (ValueError, AttributeError):
        # If extraction fails, return None
        return None


def import_washing_machines_from_csv(csv_file):
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Extract numeric part from maximum_spin_speed
            maximum_spin_speed = extract_numeric_value(row['Maximum Spin Speed'])

            # Remove commas from the price field
            price = row['Price'].replace(',', '')

            # Extract numeric value from washing capacity
            washing_capacity = extract_numeric_value(row['Washing Capacity'])

            # Create WashingMachine object if maximum_spin_speed and washing_capacity are not None
            if maximum_spin_speed is not None and washing_capacity is not None:
                WashingMachine.objects.create(
                    product_name=row['Product Name'],
                    price=price,
                    ratings=row['Ratings'],
                    brand_name=row['Brand Name'],
                    model_name=row['Model Name'],
                    washing_capacity=washing_capacity,
                    color=row['Color'],
                    maximum_spin_speed=maximum_spin_speed,
                    function_type=row['Function Type'],
                    inbuilt_heater=row['Inbuilt Heater'] == 'Yes',
                    washing_method=row['Washing Method'],
                    product_url=row['Product_Url']
                )


if __name__ == "__main__":
    import_washing_machines_from_csv("dataset.csv")
