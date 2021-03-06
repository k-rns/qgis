# Folder structure and data location

## Data aggregation

The data in this project is aggregated from 4 different projects that have been carried out around the Galapagos in the Past:

* DRIFT4: 2007. Side scan sonar data and multibeam data has been acquired by shipboard. Dredges were taken during this cruise
* MV: MR1 is a Side scan system towed on its own right at the surface (under thermocline or something).EM122 is shipboard and should be imported too (second opinion EM122 does not really matter, Sept 8, 2021). Pictures were taking by using a tow system and 
* AL15080: Alucia cruise in 2015. Pictures and samples have been taken with the submersibles Nadir and Deep Rover II. A Remus AUV acquired high resolution side scan sonar
* NA064: OET Galapagos 2015. There is multibeam data and seabed picture data



## Data location

The data has been imported from the external SSD, called GALAP. The qgis project has been build in this drive and it is important to keep the data at the same location and not change folder names. Below a list of folder paths per cruise and data type can be found in case the links break or a reference to data needs to be refound. 

### General outline Galapagos

* D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\Galapagos-DRIFT4-cruise-data\Sheirer\Galapagos_compilation\coastline\Arc_files\gal_costa_poly_dddd.shp
* CRS = EPSG:4326 (WGS84).
* In order to be able to apply labels to the shapefiles, the data has been copied into and filtered by Island names that are necessary for this project


### DRIFT4 cruise, 2007

#### Side Scan Sonar imagery

* *8m:*
  * *D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\SSS_GeoTiff_WGS84; CRS=WGS84*
  
* *16m:* 
  
  * *D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\DRIFT4_Galapagos_newGrids\DRIFT4_new 16m_MR1-grids ; CRS Unknown (ARcGIS says CRS = UTM15N)*
  * *D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\SSS_16m_GeoTiff_WGS84; CRS WGS84*
  
* 8m and 16m grids together here: D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\8M-DRIFT4-SS-GRIDS-PAUL CRS = UTM15N

  * The 16m grids are complete (= total of 8 grids) [CRS = UTM15N]
  * The 8m grids are not complete: 40-01.8m; 50-01.8m to 50-12.8m and 50-16.8m to 50-20.8m [CRS = UTM15N]
    * Here are the missing 8m grids: D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\SSS_GeoTiff_WGS84 [CRS = WGS84] [processing: applied no data value =0 to these grids (transparancy add 0]

  Bathymetry

*D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\Galapagos-DRIFT4-cruise-data\Drift4Bathy_ArcImport*

*D:\Galapagos-Bathy-Grids*

* Bathymetry around Fernandia: 
  * *D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\Galapagos-DRIFT4-cruise-data\Sheirer\Galapagos_compilation\bathy_topo\Fernandina.100m.Combined_filled.topo_bathy*   
* General bathy maps
  * *D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\galapagos-grids* 

#### Dredge data

The dredge start and end points could not be found on the drive. However, they were exported from a fleddermaus proect into a .xyz file. The location of this exported file is here: *D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\drift4-dredge-tracks.xyz.txt*

### Melville cruise MV1007, 2010

#### Side Scan Sonar

* EM122 - 50m
  * D:\MV1007-Melville-2010\MV1007-EM122-Sidescan
* MR1 - 10m (folders with 50)
* MR1 - 15m (folders with 100)
* MR1 - 25m (folders with 200)
* MR1 - 40m (folders with 400)

#### Bathymetry

*D:\MV1007-Melville-2010\MV1007-EM122-Bathymetry\mv1007-60m-em122-june16.grd*

#### TowCam data

MV Towcam logs are here: D:\MV1007-Melville-2010\MV1007-TowCam-Data\mv1007-TowCam-Logs

5 minute intervals, but needs to be interpolated to match the Mellevelle has tow cam data (pictures), but the nav file seems to be missing.

### Alucia cruise AL150801, 2015

Divide them up in Islands? Floreana, Fernandia, Santiage and Santa Cruz (no Remus data for the last one)

#### Hull mounted
* Hull mounted multibeam Alucia - gridded at 20m
  * D:\AL150801-Alucia-2015-Galapagos-Data\AL150801-multibeam-data\Multibeam -> 
  * not sure with what this bathymetry got acquire, seems not to be cleaned out. stretch from 0 to -2600 with quantile color ramp
  * WGS84
  * Singleband pseudocolor
#### Remus bathymetry - 1m - TO DO**
  * D:\AL150801-Alucia-2015-Galapagos-Data\kurras-Galapagos-AL1508-Remus-grids-geotifs 
  * Look in the "to WHOI" folders for the poststamp xyz bathymetry files, do not use the sss files
  * 1m resolution?
  * what gregg Kurass produced since REMUS couldn;t do it.
* Remus side scan sonar - 0.5m - HF and LF
  * D:\AL150801-Alucia-2015-Galapagos-Data\kurras-Galapagos-AL1508-Remus-grids-geotifs\from_kurras_20210827 [high frequency and low frequency sss from remus]
  * 0.5 m resolution?
  * for both HR and LR (high and low resolution tiffs): qgis imports wrong color scheme, change to singleband grey and 255 as no data
  * what gregg Kurass produced since REMUS couldn;t do it.

#### Nadir and Deep Rover II dive tracks

#### Nadir seabed pictures 

* Dives happened with 2 vehicels: Deep Rover 2 (DR)  and Nadir (N)
* date, xyz files of those vehicles can be found here: D:\AL150801-Alucia-2015-Galapagos-Data\AL150801-DIVE-DATA-DEPTH-NAV 
* Use the .txt files from those folders, format is: YYYY,MM,DD,HH,MM,SS.S, Dec Long,  Dec Lat,  UTM X,  UTM Y,  -DEPTH (M) 
* pictures can be found here: D:\AL150801-Alucia-2015-Galapagos-Data\AL150801-Nadir-GoPro-images 
* 

### OET-Galapagos 2015

Pictures are here: D:\NAUTILUS-OET-Galapagos-2015\NA064-herc_MISO-gopro_corrected_time

Correct nav files to use: "D:\NAUTILUS-OET-Galapagos-2015\NA064\processed\dive_reports\H1441\merged\H1441.NAV3D.M1.sampled.tsv" 

sampled  dive resampled to 1 second intervals, with depth. 



## Seabed pictures 

Seabed pictures are aggregated from the following cruises and sampling methods:

* OET Galapagos -NA064 Hercules ROV
* AL150801 - Nadir HOW
* MV1007 - TowCam Data

Picture locations are derived from the navigational files and joined based on the picture names (year, mm, dd, hh, mm, ss) and those same columns in the navigational files

## Data sources in QGIS

Right click on the layer to see where the data is located/referenced. -> information
