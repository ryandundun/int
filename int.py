import pandas as pd

# Load the data
file_path = 'My_data.csv'  # Replace with your actual file path
data = pd.read_csv(file_path)

# Fix potential issues in the DateModified column by handling incorrect dates
def fix_date(date_str):
    try:
        return pd.to_datetime(date_str, errors='coerce')
    except ValueError:
        return pd.NaT

data['DateModified'] = data['DateModified'].apply(fix_date)

# Define the date 6 months ago from the most recent date in the dataset
most_recent_date = data['DateModified'].max()
six_months_ago = most_recent_date - pd.DateOffset(months=6)

# Classify articles into recent updates and older updates
data['UpdateStatus'] = data['DateModified'].apply(lambda x: 'Recent' if x >= six_months_ago else 'Older')

# Group by UpdateStatus and calculate mean performance metrics
performance_metrics = data.groupby('UpdateStatus').agg({
    'Average Position': 'mean',
    'Url Clicks': 'mean',
    'URL CTR': 'mean'
}).reset_index()

# Print the performance metrics
print(performance_metrics)
