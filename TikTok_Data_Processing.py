import pandas as pd
import ace_tools as tools  # For displaying results

# Load the dataset
file_path = "/mnt/data/tiktok_hashtags.csv"  # Update with your actual file path
df = pd.read_csv(file_path)

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
cleaned_file_path = "/mnt/data/tiktok_hashtags_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)

# Display the cleaned dataset
tools.display_dataframe_to_user(name="Cleaned TikTok Hashtags", dataframe=df)

print(f"Cleaned dataset saved at: {cleaned_file_path}")
