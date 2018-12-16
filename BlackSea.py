from netCDF4 import Dataset
import numpy as np

from mpl_toolkits.basemap import Basemap, cm

import matplotlib.pyplot as plt

import numpy as np

#import h5py as h5py

nc_file = '../3B-DAY-L.MS.MRG.3IMERG.20181112-S000000-E235959.V05.nc4.nc'
dataset = Dataset(nc_file, mode='r')


 
precip1 = dataset.variables['precipitationCal'][:]
precip1 = np.transpose(precip1)

precip = precip1  

theLats= dataset['lat'][:]
theLons = dataset['lon'][:]
 

# Plot the figure, define the geographic bounds

fig = plt.figure(dpi=300)

latcorners = ([38,46])

loncorners = ([34,45])

 

m = Basemap(projection='cyl',llcrnrlat=latcorners[0],urcrnrlat=latcorners[1],llcrnrlon=loncorners[0],urcrnrlon=loncorners[1],resolution="h")

 

# Draw coastlines, state and country boundaries, edge of map.

m.drawcoastlines(linewidth=1.2, linestyle='solid', color='k', antialiased=3, ax=None, zorder=None)
m.drawcountries(linewidth=0.8, linestyle='solid', color='k', antialiased=3, ax=None, zorder=None)

m.bluemarble(scale=3)
#m.shadedrelief(scale=2)
#m.etopo(scale=3)

#scale=2

#m.drawstates()

#m.drawcountries()

 

# Draw filled contours.

clevs = np.arange(0,60,5)   #color scale changing

#clevs = [2,5,10,20,30,40,50,60,70,100]

#clevs = np.arange(0,1000,20)

 

# Define the latitude and longitude data

x, y = np.float32(np.meshgrid(theLons, theLats))

 

# Mask the values less than 0 because there is no data to plot.

masked_array = np.ma.masked_where(precip < 0,precip)

 

# Plot every masked value as white

#cmap = cm.GMT_drywet
cmap = cm.GMT_drywet


cmap.set_bad('w',1.)

 

# Plot the data

cs = m.contourf(x,y,precip,clevs,cmap=cmap,latlon=True)

 

parallels = np.arange(-60.,61,20.)

m.drawparallels(parallels,labels=[True,False,True,False])

meridians = np.arange(-180.,180.,60.)

m.drawmeridians(meridians,labels=[False,False,False,True])

 

# Set the title and fonts

plt.title('Black Sea Total Rain Rate')

font = {'weight' : 'bold', 'size' : 6}

plt.rc('font', **font)

 

# Add colorbar

cbar = m.colorbar(cs,location='right',pad="5%")

cbar.set_label('mm/h')

 

#plt.savefig('../*.png',dpi=200)   #change to your directory
