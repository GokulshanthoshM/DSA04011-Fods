import pandas as pd

# Sample property data
data = {
    'property_id': [1, 2, 3, 4, 5],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'number_of_bedrooms': [3, 4, 3, 5, 2],
    'area_sq_ft': [1500, 2000, 1800, 2500, 1200],
    'listing_price': [250000, 320000, 280000, 420000, 180000]
}

property_data = pd.DataFrame(data)

# 1. Average Listing Price of Properties in Each Location
average_price_by_location = property_data.groupby('location')['listing_price'].mean()
print("Average Listing Price by Location:\n", average_price_by_location)

# 2. Number of Properties with More Than Four Bedrooms
properties_with_more_than_four_bedrooms = property_data[property_data['number_of_bedrooms'] > 4]
num_properties_with_more_than_four_bedrooms = properties_with_more_than_four_bedrooms.shape[0]
print("Number of Properties with More Than Four Bedrooms:", num_properties_with_more_than_four_bedrooms)

# 3. Property with the Largest Area
property_with_largest_area = property_data[property_data['area_sq_ft'] == property_data['area_sq_ft'].max()]
print("Property with Largest Area:\n", property_with_largest_area)
