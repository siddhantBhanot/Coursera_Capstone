# Coursera_Capstone
The objective of this capstone project is to analyze and select the best location suitable for a person to buy a house, based on the amenities offered in that location and price of the house. 

# Data
The following data is required 
<ul>
<li>List of neighborhoods along with average price per square feet of the house for the neighborhood for the city of New Delhi. </li>
<li>Latitude and Longitude of the given localities. </li>
<li>Amenities around the given location.</li>
</ul>

# Methodology
<ul>
  <li> Web scraping makaan.com page for neighbourhoods list along with prices of house. <l/i> 
  <li> Get latitude and longitude coordinates using Geocoder </li> 
  <li> Use Foursquare API to get venue data </li> 
  <li> Group data by neighbourhood and taking the mean of the frequency of  occurrence of each venue category </li> 
  <li> Perform clustering on the data by using k-means clustering </li> 
  <li> Visualize the clusters in a map using Folium </li> 
 </ul>


# Deployment
**Streamlit App**:
   A Streamlit application is deployed and can be accessed here: [Delhi Locality Recommender](https://courseracapstone-wh4aihzgahbjp2wpdysjae.streamlit.app/)


