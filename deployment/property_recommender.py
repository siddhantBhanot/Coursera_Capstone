import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

# Load the dataset
def load_data():
    df = pd.read_csv("deployment/delhi_locality_data.csv")
    return df

# Function to filter locations based on user input
def filter_locations(df, budget, amenities):
    # Filter by price per sqft
    filtered_df = df[df['price per sqft'] <= budget]
    
    # Compute how many amenities match for each locality
    filtered_df['match_count'] = filtered_df.iloc[:, 4:14].apply(lambda row: sum(venue in amenities for venue in row), axis=1)
    
    # Sort by the number of matching amenities (descending)
    filtered_df = filtered_df.sort_values(by='match_count', ascending=False)
    
    return filtered_df[['locality name', 'latitude', 'longitude', 'price per sqft', 'match_count']]

# Load data
df = load_data()

# Streamlit UI
st.title("🏡 Delhi Locality Recommender")
st.write("Enter your budget and select amenities to find the best localities for you.")

# User inputs
budget = st.number_input("Enter your budget (price per sq ft):", min_value=1000, max_value=100000, step=500, value=20000)

# Get unique amenities dynamically
amenities_list = sorted(set(df.iloc[:, 4:14].values.flatten()))
amenities_selected = st.multiselect("Select up to 5 preferred amenities:", amenities_list, max_selections=5)

# Filter results if amenities are selected
if st.button("Find Localities"):
    if amenities_selected:
        result_df = filter_locations(df, budget, amenities_selected)
        
        if not result_df.empty:
            st.success(f"Found {len(result_df)} matching localities!")
            st.dataframe(result_df)
            
            # Map visualization
            m = folium.Map(location=[28.6139, 77.2090], zoom_start=11)
            
            for _, row in result_df.iterrows():
                folium.Marker(
                    location=[row['latitude'], row['longitude']],
                    popup=f"{row['locality name']}\nPrice per sqft: {row['price per sqft']}\nMatching Amenities: {row['match_count']}",
                    icon=folium.Icon(color='blue')
                ).add_to(m)
            
            folium_static(m)
        else:
            st.warning("No matching localities found! Try adjusting your budget or amenities.")
    else:
        st.error("Please select at least one amenity.")
