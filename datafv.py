import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Open the NetCDF file
dataset = nc.Dataset('20190701-ESACCI-L4_FIRE-BA-MODIS-fv5.1.1cds.nc')

# Read data
lon = dataset.variables['lon'][:]
lat = dataset.variables['lat'][:]
data = dataset.variables['burned_area_vegetation_area'][0, :, :]  # Selecting the first time slice (you can change the index as needed)

# Define the extent of the map for Greece
extent = [19, 29, 34, 42]  # [lon_min, lon_max, lat_min, lat_max]

# Create a figure and axis with a specific map projection and the defined extent
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(8, 8))
ax.set_extent(extent, crs=ccrs.PlateCarree())

# Plot the data on the map
im = ax.contourf(lon, lat, data, transform=ccrs.PlateCarree())

# Add a colorbar
cbar = plt.colorbar(im)

# Set the plot title
plt.title('Your Data in Greece')

# Show the plot
plt.show()

# Close the NetCDF file
dataset.close()
