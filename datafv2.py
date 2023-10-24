import netCDF4 as nc
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.colors as mcolors

# Open the NetCDF file
#dataset = nc.Dataset('./dataold/20200701-ESACCI-L4_FIRE-BA-MODIS-fv5.1.nc')
dataset = nc.Dataset('20190701-ESACCI-L4_FIRE-BA-MODIS-fv5.1.1cds.nc')
dataset1 = nc.Dataset('20190801-ESACCI-L4_FIRE-BA-MODIS-fv5.1.1cds.nc')

# Read data
lon = dataset.variables['lon'][:]
lat = dataset.variables['lat'][:]
data = dataset.variables['burned_area'][0, :, :]  # Select the desired time slice
data1 = dataset1.variables['burned_area'][0, :, :]  # Select the desired time slice

# Define the extent of the map for Greece
extent = [19, 29, 34, 42]  # [lon_min, lon_max, lat_min, lat_max]

# Create a figure and axis with a specific map projection and the defined extent
fig, ax = plt.subplots(subplot_kw={'projection': ccrs.PlateCarree()}, figsize=(10, 10))
ax.set_extent(extent, crs=ccrs.PlateCarree())

combined_data = data + data1
# Plot the data on the map
#im = ax.contourf(lon, lat, data, transform=ccrs.PlateCarree())
#im = ax.pcolormesh(lon, lat, data, shading='auto', cmap='viridis', transform=ccrs.PlateCarree())
#im = ax.scatter(lon, lat, c=data, cmap='viridis', s=10, transform=ccrs.PlateCarree())
#im = ax.imshow(data, extent=(lon.min(), lon.max(), lat.min(), lat.max()), origin='upper', cmap='viridis', transform=ccrs.PlateCarree())
#im = ax.contour(lon, lat, data, levels=10, colors='k', linewidths=0.5, transform=ccrs.PlateCarree())
colors = ['red', 'blue', 'green', 'orange']
im = ax.contour(lon, lat, combined_data, levels=5, colors=colors, linewidths=0.8, transform=ccrs.PlateCarree())




# Add a colorbar
#cbar = plt.colorbar(im)

# Add map features like coastlines, gridlines, etc.
#ax.coastlines()
ax.coastlines(resolution='10m', color='green', linewidth=1)  # Set coastline color and line width


#ax.gridlines()

# Set the plot title
plt.title('Burned Area in Greece')

# Show the plot
plt.show()

# Close the NetCDF file
dataset.close()

