Create a project location that can be used during the cruise and the links will not break. 

Read mac formatted drives -> buy software 

QGIS Project CRS = WGS84 - UTM15N



### Outline Galapagos

* D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\Galapagos-DRIFT4-cruise-data\Sheirer\Galapagos_compilation\coastline\Arc_files\gal_costa_poly_dddd.shp

* CRS = EPSG:4326 (WGS84)


### DRIFT4 Cruise - 2001

​	Side Scan Sonar data has been acquired with...

​	Multibeam data has been acquired with...

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

* *25m - Did not find*

  

#### Bathymetry

*D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\Galapagos-DRIFT4-cruise-data\Drift4Bathy_ArcImport*

*D:\Galapagos-Bathy-Grids*

* Bathymetry around Fernandia: 
  * D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\Galapagos-DRIFT4-cruise-data\Sheirer\Galapagos_compilation\bathy_topo\Fernandina.100m.Combined_filled.topo_bathy   
* General bathy maps
  * D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\galapagos-grids 

### MV Cruise, 2010

MR1 is a Side scan system towed on its own right at the surface (under thermocline or something).EM122 is shipboard and should be imported too (second opinion EM122 does not really matter, Sept 8, 2021)

#### Side Scan Sonar

* EM122 - 50m
  * D:\MV1007-Melville-2010\MV1007-EM122-Sidescan
* MR1 - 10m (folders with 50)
* MR1 - 15m (folders with 100)
* MR1 - 25m (folders with 200)
* MR1 - 40m (folders with 400)

#### Bathymetry

D:\MV1007-Melville-2010\MV1007-EM122-Bathymetry\mv1007-60m-em122-june16.grd



### AL150801, 2015

Divide them up in Islands? Floreana, Fernandia, Santiage and Santa Cruz (no Remus data for the last one)

* Hull mounted multibeam Alucia - gridded at 20m
  * D:\AL150801-Alucia-2015-Galapagos-Data\AL150801-multibeam-data\Multibeam -> 
  * not sure with what this bathymetry got acquire, seems not to be cleaned out. stretch from 0 to -2600 with quantile color ramp
  * WGS84
  * Singleband pseudocolor
* **Remus bathymetry - 1m - TO DO**
  * D:\AL150801-Alucia-2015-Galapagos-Data\kurras-Galapagos-AL1508-Remus-grids-geotifs 
  * Look in the "to WHOI" folders for the poststamp xyz bathymetry files, do not use the sss files
  * 1m resolution?
  * what gregg Kurass produced since REMUS couldn;t do it.
* Remus side scan sonar - 0.5m - HF and LF
  * D:\AL150801-Alucia-2015-Galapagos-Data\kurras-Galapagos-AL1508-Remus-grids-geotifs\from_kurras_20210827 [high frequency and low frequency sss from remus]
  * 0.5 m resolution?
  * for both HR and LR (high and low resolution tiffs): qgis imports wrong color scheme, change to singleband grey and 255 as no data
  * what gregg Kurass produced since REMUS couldn;t do it.



### Pictures to map project

* Dives happened with 2 vehicels: Deep Rover 2 (DR)  and Nadir (N)
* date, xyz files of those vehicles can be found here: D:\AL150801-Alucia-2015-Galapagos-Data\AL150801-DIVE-DATA-DEPTH-NAV 
* Use the .txt files from those folders, format is: YYYY,MM,DD,HH,MM,SS.S, Dec Long,  Dec Lat,  UTM X,  UTM Y,  -DEPTH (M) 
* pictures can be found here: D:\AL150801-Alucia-2015-Galapagos-Data\AL150801-Nadir-GoPro-images 
* 



September 8, 2021

cubic spline of nav files (get 1 second intervals to be able to join the picture files that have different second intervals). 

drift 4 has dredges (are not on the disk)

Mellevelle has tow cam data (pictures), but the nav file seems to be missing.

Create maps of each in 



OET-Galapagos 2015

Pictures are here: D:\NAUTILUS-OET-Galapagos-2015\NA064-herc_MISO-gopro_corrected_time

Correct nav files to use: "D:\NAUTILUS-OET-Galapagos-2015\NA064\processed\dive_reports\H1441\merged\H1441.NAV3D.M1.sampled.tsv" 

sampled  dive resampled to 1 second intervals, with depth. 

Drift 4 dredge points: "D:\DRIFT4-2001-Revelle-Galapagos-Data-Figures\drift4-dredge-tracks.xyz.txt" 

MV Towcam logs are here: D:\MV1007-Melville-2010\MV1007-TowCam-Data\mv1007-TowCam-Logs

5 minute intervals, but needs to be interpolated to match the 
