import os
from django.shortcuts import render
import folium
import geopandas as gpd
from django.contrib import messages

def home(request):
    try:
        # Path to the folder containing the shapefiles (GeoJSON format)
        shapefile_folder = 'static/gis/'
        
        # Store GeoDataFrames in a dictionary for easy management
        geo_data = {}

        # Loop through all the files in the shapefile folder
        for file in os.listdir(shapefile_folder):
            if file.endswith(".geojson"):
                file_path = os.path.join(shapefile_folder, file)
                
                # Load each file using GeoPandas
                gdf = gpd.read_file(file_path)
                
                # Ensure the file is in EPSG:4326 (WGS84) coordinate system
                gdf = gdf.to_crs("EPSG:4326")
                
                # Store in the dictionary
                geo_data[file] = gdf

        # Show a success message after loading the files
        messages.success(request, "Interactive map loaded successfully with all shapefiles.")
    except Exception as e:
        messages.error(request, f"Error loading shapefiles: {e}")
        return render(request, 'core/map.html', {'map': None})

    # Create a Folium Map centered at a specific location using OpenStreetMap tiles
    m = folium.Map(location=[45.38, 25.444], zoom_start=10, tiles='OpenStreetMap', control_scale=True)

    # Define styles for different layers
    style1 = {'fillColor': 'transparent', 'color': '#FF8C00'}
    style2 = {'fillColor': 'transparent', 'color': '#FFD700'}
    style3 = {'fillColor': 'transparent', 'color': '#008080'}
    style4 = {'fillColor': 'transparent', 'color': '#708090'}

    # Style mapping for different shapefiles based on filename (can be customized)
    style_mapping = {
        'pnb_3844_poly.geojson': style1,
        'ROSCI_0013_3844_poly.geojson': style2,
        'RO_limits_3844_poly.geojson': style3,
        'UAT_limits_3844_poly.geojson': style4,
    }

    # Add each shapefile to the map
    for file, gdf in geo_data.items():
        # Get the style for the specific file
        style = style_mapping.get(file, {'fillColor': 'transparent', 'color': '#000000'})  # Default style if not mapped
        folium.GeoJson(
            data=gdf['geometry'],
            name=file,  # Use filename as layer name
            style_function=lambda x, style=style: style,
            show=True
        ).add_to(m)

    # Add a layer control panel to the map
    m.add_child(folium.LayerControl())

    # Render the map to HTML
    map_html = m._repr_html_()

    # Pass the map HTML to the context
    context = {'map': map_html}
    return render(request, 'core/map.html', context)