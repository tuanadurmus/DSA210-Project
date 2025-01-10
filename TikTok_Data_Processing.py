import pandas as pd
import ace_tools as tools  # For displaying results

# Load the dataset
file_path = "/mnt/data/tiktok_hashtags temmuz.xlsx"  # Update with your actual file path
df = pd.read_excel(file_path)

# Drop the 'URL' column if it exists
if "URL" in df.columns:
    df = df.drop(columns=["URL"])

# Define function to filter out error rows
def is_valid_hashtag(row):
    # Assuming errors contain NaN or non-standard entries
    return isinstance(row, str) and row.startswith("#")  # Keep only valid hashtags

# Apply filtering to remove error rows
df = df[df["Hashtag"].apply(is_valid_hashtag)]  # Adjust column name accordingly

# Save the cleaned dataset
cleaned_file_path = "/mnt/data/tiktok_hashtags_cleaned.xlsx"
df.to_excel(cleaned_file_path, index=False)

# Display the cleaned dataset
tools.display_dataframe_to_user(name="Cleaned TikTok Hashtags", dataframe=df)
