# Interactive Map Application

This project is a Django web application that uses **Folium** and **GeoPandas** to create an interactive map that visualizes geographical data stored in GeoJSON files. The application loads multiple shapefiles from a specified directory and displays them on a map using OpenStreetMap tiles. The "geemap" name of the main project folder, comes from google earth engine map which i used initially when created, but at some point I had trouble with gee api and authentication, thus switched to OpenStreetMap tiles to render the background map.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Dynamic loading of multiple GeoJSON shapefiles from a designated folder.
- Visualization of geographical features on an interactive map using Folium.
- Layer control to toggle visibility of different shapefiles.
- Styled layers for better visual differentiation.
- User-friendly error messages for easier debugging.

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/interactive-map-app.git
   cd interactive-map-app
2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install the required packages:**:

   ```bash
   pip install django folium geopandas
4. **Set up your Django project:**:
    
    Follow the Django documentation to set up your project.
5. **Create the static/gis directory:**:

   Place your GeoJSON files in the static/gis directory.
4. **Set up your Django project:**:
    
    Follow the Django documentation to set up your project.
## Usage
1. **Run the Django development server:**;
    ```bash
    python manage.py runserver

2. **Open your browser and navigate to http://127.0.0.1:8000/ (or the appropriate URL for your app).**;

## Directory Structure

    ```bash
    interactive-map-app/
    │
    ├── core/                      # Django app containing the main functionality
    │   ├── views.py              # Contains the map rendering logic
    │   └── templates/
    │       └── core/
    │           └── map.html      # Template for rendering the map
    │
    ├── static/
    │   └── gis/                  # Directory containing GeoJSON shapefiles
    │       ├── pnb_3844_poly.geojson
    │       ├── ROSCI_0013_3844_poly.geojson
    │       ├── RO_limits_3844_poly.geojson
    │       └── UAT_limits_3844_poly.geojson
    │
    └── manage.py                  # Django management script





