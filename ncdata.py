import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt

file_path = '/mnt/fc34c8a9-cef6-4002-8d6d-e9a21c4d4ceb/data/DWR_01_12_2015_10_UTC.nc'

dataset = nc.Dataset(file_path, mode='r')

print("Dataset:", dataset)

variables = dataset.variables.keys()
print("Variables:", variables)

lon = dataset.variables['lon'][:]
lat = dataset.variables['lat'][:]
elev = dataset.variables['elev'][:]

print("Longitude shape:", lon.shape)
print("Latitude shape:", lat.shape)
print("Elevation shape:", elev.shape)

if 'Reflectivity' in dataset.variables and 'velocity' in dataset.variables:
    reflectivity = dataset.variables['Reflectivity'][:]
    velocity = dataset.variables['velocity'][:]

    print("Reflectivity shape:", reflectivity.shape)
    print("Velocity shape:", velocity.shape)

    elevation_layer = 0
    reflectivity_layer = reflectivity[:, :, elevation_layer]
    velocity_layer = velocity[:, :, elevation_layer]

    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(reflectivity_layer, origin='lower', extent=(lon.min(), lon.max(), lat.min(), lat.max()), cmap='jet')
    plt.colorbar(label='Reflectivity (dBZ)')
    plt.title(f'Reflectivity at Elevation {elevation_layer}')

    plt.subplot(1, 2, 2)
    plt.imshow(velocity_layer, origin='lower', extent=(lon.min(), lon.max(), lat.min(), lat.max()), cmap='seismic')
    plt.colorbar(label='Velocity (m/s)')
    plt.title(f'Velocity at Elevation {elevation_layer}')

    plt.tight_layout()
    plt.show()
else:
    print("Reflectivity or velocity variable not found in the dataset")

dataset.close()

