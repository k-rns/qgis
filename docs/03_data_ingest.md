# Importing data

This chapter will discuss the way of adding Ingest data per type



Adding data using the "Data Source Manager" and choose the correct type of data to ingest:

## Data Source Manager

### Delimited text

Apart from rasters, this is the most used data type there is in the whole disk. 

The **format of the file** **to import** is important. It is easiest to work with a **.csv or .txt file** that has column headers in the file itself. Take this into account when exporting a .txt file from Fleddermaus or any other program. 

Steps to import a .csv file with xy coordinates:

1. Data Source Manager -> Delimited text.

2. Fill in:
   * file format: 
   * Geometry definition: will be the columns that represent the point locations. In the geographic system (WGS84), the Y is the latitude and X the longitude. In a projected system (UTM15N), X normally is X and Y normally Y.
   * Set the correct coordinate reference system! If this is wrong, the points will show up somewhere else on the map, i.e. will be projected at the wrong location. 

### Rasters

The easiest format to work with when importing rasters into your qgis project is using GeoTiff for both side scan sonar and multibeam data. Side note: side scan sonar will always be imagery data, while multibeam data can also be imported as gridded points or processed soundings and interpolated in QGIS. 

The easiest way to import rasters is to drag/drop them into your project. This will work only with Geotiff rasters.

When doing the drag and drop way, you'll probably will have to set the CRS after import. To do this, do right click on layer -> CRS-> choose WGS84 or projected system used on the cruise.  

It is easiest if the data processor imbeds the projection system in the filename so there is no confusion or guessing once of the vessel. 

### Vector

### Setting the file path

If a file has been imported into your qgis project, but doesn't show up when you open the project again, it probably has been moved its location when the project was closed. You can always check the file you're working with by right clicking the layer-> properties.  



Some data management principles to make life easier on and off the cruise shio:

* imbed the projection system in the file name, i.e utm15N or WGS84

* imbed the resolution in the filename i.e 15m
* 

