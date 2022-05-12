<h1> Power Consumption and Renewable Resources </h1>
   <details> <summary> <h4>Disclamer</h4> </summary> This repository contains all of the files for the Final project for COE332.
  Due to complication with site resources of data some data was made unavailable 
   </details>
   
<h2> Introduction </h2>
This project should allow users to go throuhg large amounts of data from Prediction of Worldwide Energy Resource or POWER and access specified and general data about worldwide meterological and radiation data. The project uses dynamically updated monthly data which contains mmeteorological data and radiation data about the world.

<details> <summary> <h3> What's in the Project </h3></summary>
   The files in the project are:
   
   -<code> Dockerfiles</code>: Functions to download necassary dependencies and environment variables to set up needed operations for the application.
   -<code> api.py</code>: python script that provides routes to download and returns information from the two data sets.
   6 yml files:
app-prod-api-deployment.yml 
app-prod-api-service.yml
app-prod-db-deployment.yml
app-prod-db-pvc.yml
app-prod-db-service.yml
app-prod-wrk-deployment.yml
   </details>
<h2> Important Information Before starting use of code </h2> 
Before beginning two files are going to be required for this which contains the data for this project. 
<h4> Meteorology and Radiation </h4>
The two files will need to be downloaded which can be found <a href="https://opendap.larc.nasa.gov/opendap/POWER/monthly/contents.html">here</a> or can be downloaded to one's terminal by using the <code>wget</code> command

```
wget https://opendap.larc.nasa.gov/opendap/POWER/monthly/power_901_monthly_meteorology_utc.nc.covjson  
```

and 

```
wget https://opendap.larc.nasa.gov/opendap/POWER/monthly/power_901_monthly_radiation_utc.nc.covjson
```

<h2> More Setup </h2>
<details> <summary> <h3> Building Docker Containers </h3> </summary>
   -Dockerfile
      - to begin touch a file named Dockerfile to create the file in the directory by using <code> touch Dockerfile </code>
      - A Makefile is also available to facilitate the proccess and have all of the images created in one step, simply use <code> make all </code>
</details>
<h2> Deploying the Application on Kubernetes </h2>
To deploy the application on the kubernetes cluster, you must first ssh to k8s like the following:

```
ssh username@coe332-k8s.tacc.cloud
```

When inside the kubernetes you can clone the repository 

```
git clone https://github.com/Jal7434/Final_Project/edit/main/README.md
```

then you can make each of the 6 tests found in the kubernetes folder of this repository.
you can use <code> make app-prod(rest of yml) </code> to set up the kubernetes service.

once inside the kubernetes enviornment you should also ensure that pytest and requests are installed by doing 

```
pip3 install --user pytest 

and

pip3 install --user request
```
To test the scripts simply type pytest

<h2> How to interact with CRUD Operations </h2>
to add the data to Redis database 

```
curl localhost:(redisip) -X POST
```
to read the data that was uploaded you can
```
curl localhost:(redisip)/data
```

the output of this will be
```
"type": "Coverage",
  "domain": {
    "type" : "Domain",
    "domainType": "Grid",
    "axes": {
      "x": {
        "values": [-179.5, -178.5, -177.5, -176.5, -175.5, -174.5, -173.5, -172.5, -171.5, -170.5, -169.5, -168.5, -167.5, -166.5, -165.5, -164.5, -163.5, -162.5, -161.5, -160.5, -159.5, -158.5, -157.5, -156.5, -155.5, -154.5, -153.5, -152.5, -151.5, -150.5, -149.5, -148.5, -147.5, -146.5, -145.5, -144.5, -143.5, -142.5, -141.5, -140.5, -139.5, -138.5, -137.5, -136.5, -135.5, -134.5, -133.5, -132.5, -131.5, -130.5, -129.5, -128.5, -127.5, -126.5, -125.5, -124.5, -123.5, -122.5, -121.5, -120.5, -119.5, -118.5, -117.5, -116.5, -115.5, -114.5, -113.5, -112.5, -111.5, -110.5, -109.5, -108.5, -107.5, -106.5, -105.5, -104.5, -103.5, -102.5, -101.5, -100.5, -99.5, -98.5, -97.5, -96.5, -95.5, -94.5, -93.5, -92.5, -91.5, -90.5, -89.5, -88.5, -87.5, -86.5, -85.5, -84.5, -83.5, -82.5, -81.5, -80.5, -79.5, -78.5, -77.5, -76.5, -75.5, -74.5, -73.5, -72.5, -71.5, -70.5, -69.5, -68.5, -67.5, -66.5, -65.5, -64.5, -63.5, -62.5, -61.5, -60.5, -59.5, -58.5, -57.5, -56.5, -55.5, -54.5, -53.5, -52.5, -51.5, -50.5, -49.5, -48.5, -47.5, -46.5, -45.5, -44.5, -43.5, -42.5, -41.5, -40.5, -39.5, -38.5, -37.5, -36.5, -35.5, -34.5, -33.5, -32.5, -31.5, -30.5, -29.5, -28.5, -27.5, -26.5, -25.5, -24.5, -23.5, -22.5, -21.5, -20.5, -19.5, -18.5, -17.5, -16.5, -15.5, -14.5, -13.5, -12.5, -11.5, -10.5, -9.5, -8.5, -7.5, -6.5, -5.5, -4.5, -3.5, -2.5, -1.5, -0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5, 11.5, 12.5, 13.5, 14.5, 15.5, 16.5, 17.5, 18.5, 19.5, 20.5, 21.5, 22.5, 23.5, 24.5, 25.5, 26.5, 27.5, 28.5, 29.5, 30.5, 31.5, 32.5, 33.5, 34.5, 35.5, 36.5, 37.5, 38.5, 39.5, 40.5, 41.5, 42.5, 43.5, 44.5, 45.5, 46.5, 47.5, 48.5, 49.5, 50.5, 51.5, 52.5, 53.5, 54.5, 55.5, 56.5, 57.5, 58.5, 59.5, 60.5, 61.5, 62.5, 63.5, 64.5, 65.5, 66.5, 67.5, 68.5, 69.5, 70.5, 71.5, 72.5, 73.5, 74.5, 75.5, 76.5, 77.5, 78.5, 79.5, 80.5, 81.5, 82.5, 83.5, 84.5, 85.5, 86.5, 87.5, 88.5, 89.5, 90.5, 91.5, 92.5, 93.5, 94.5, 95.5, 96.5, 97.5, 98.5, 99.5, 100.5, 101.5, 102.5, 103.5, 104.5, 105.5, 106.5, 107.5, 108.5, 109.5, 110.5, 111.5, 112.5, 113.5, 114.5, 115.5, 116.5, 117.5, 118.5, 119.5, 120.5, 121.5, 122.5, 123.5, 124.5, 125.5, 126.5, 127.5, 128.5, 129.5, 130.5, 131.5, 132.5, 133.5, 134.5, 135.5, 136.5, 137.5, 138.5, 139.5, 140.5, 141.5, 142.5, 143.5, 144.5, 145.5, 146.5, 147.5, 148.5, 149.5, 150.5, 151.5, 152.5, 153.5, 154.5, 155.5, 156.5, 157.5, 158.5, 159.5, 160.5, 161.5, 162.5, 163.5, 164.5, 165.5, 166.5, 167.5, 168.5, 169.5, 170.5, 171.5, 172.5, 173.5, 174.5, 175.5, 176.5, 177.5, 178.5, 179.5]
      },

```
 <details> <summary> <h1> What routes are available and a minor description about them do </h1> </summary> 
ALLSKY_SFC_LW_DWN: 
   
Downward Thermal Infrared (Longwave) Radiative Flux

ALLSKY_SFC_SW_DWN:
   
All Sky Insolation Incident on a Horizontal Surface

ALLSKY_SFC_SW_DWN_00_GMT: 
   
All Sky Insolation Incident On A Horizontal Surface at 00 GMT

ALLSKY_SFC_SW_DWN_03_GMT: 
   
All Sky Insolation Incident On A Horizontal Surface at 03 GMT

ALLSKY_SFC_SW_DWN_06_GMT: 
   
All Sky Insolation Incident On A Horizontal Surface at 06 GMT

ALLSKY_SFC_SW_DWN_09_GMT:
   
All Sky Insolation Incident On A Horizontal Surface at 09 GMT

ALLSKY_SFC_SW_DWN_12_GMT:
   
All Sky Insolation Incident On A Horizontal Surface at 12 GMT

ALLSKY_SFC_SW_DWN_15_GMT:
   
All Sky Insolation Incident On A Horizontal Surface at 15 GMT

ALLSKY_SFC_SW_DWN_18_GMT: 
   
All Sky Insolation Incident On A Horizontal Surface at 18 GMT

ALLSKY_SFC_SW_DWN_21_GMT: 
   
All Sky Insolation Incident On A Horizontal Surface at 21 GMT

ALLSKY_SFC_SW_DWN_MAX_DIFF: 
   
Maximum Monthly Difference From Monthly Averaged All Sky Insolation

ALLSKY_SFC_SW_DWN_MIN_DIFF: 
   
Minimum Monthly Difference From Monthly Averaged All Sky Insolation

ALLSKY_TOA_SW_DWN:
   
Top-of-atmosphere Insolation

CDD0:
   
Cooling Degree Days Above 0 C

CDD10:
   
Cooling Degree Days Above 10 C

CDD18_3:
   
Cooling Degree Days Above 18.3 C

CLD_AMT:
   
Daylight Cloud Amount

CLD_AMT_00_GMT:
   
Cloud Amount at 00 GMT

CLD_AMT_03_GMT:
   
Cloud Amount at 03 GMT

CLD_AMT_06_GMT:
   
Cloud Amount at 06 GMT

CLD_AMT_09_GMT:
   
Cloud Amount at 09 GMT

CLD_AMT_12_GMT:
   
Cloud Amount at 12 GMT

CLD_AMT_15_GMT:
   
Cloud Amount at 15 GMT

CLD_AMT_18_GMT:
   
Cloud Amount at 18 GMT

CLD_AMT_21_GMT:
   
Cloud Amount at 21 GMT

CLRSKY_DIFF:
   
Clear Sky Diffuse Radiation On A Horizontal Surface

CLRSKY_NKT:
   
Normalized Clear Sky Insolation Clearness Index

CLRSKY_SFC_SW_DWN:
   
Clear Sky Insolation Incident on a Horizontal Surface

DIFF:
   
Diffuse Radiation On A Horizontal Surface

DIFF_MAX:
   
Maximum Diffuse Radiation On A Horizontal Surface

DIFF_MIN:
   
Minimum Diffuse Radiation On A Horizontal Surface

DNR:
   
Direct Normal Radiation

DNR_MAX:
   
Maximum Direct Normal Radiation

DNR_MAX_DIFF:
   
Maximum Difference From Monthly Averaged Direct Normal Radiation

DNR_MIN:
   
Minimum Direct Normal Radiation

DNR_MIN_DIFF:
   
Minimum Difference From Monthly Averaged Direct Norma l Radiation

EQVLNT_NO_SUN_BLACKDAYS_1:
   
Equivalent Number Of NO-SUN Or BLACK Days Over A Consecutive 1-day Period

EQVLNT_NO_SUN_BLACKDAYS_14:
   
Equivalent Number Of NO-SUN Or BLACK Days Over A Consecutive 14-day Period

EQVLNT_NO_SUN_BLACKDAYS_21:
   
Equivalent Number Of NO-SUN Or BLACK Days Over A Consecutive 21-day Period

EQVLNT_NO_SUN_BLACKDAYS_3:
   
Equivalent Number Of NO-SUN Or BLACK Days Over A Consecutive 3-day Period

EQVLNT_NO_SUN_BLACKDAYS_7:
   
Equivalent Number Of NO-SUN Or BLACK Days Over A Consecutive 7-day Period

EQVLNT_NO_SUN_BLACKDAYS_MONTH:
   
Equivalent Number Of NO-SUN Or BLACK Days Over A Consecutive Month Period

FROST_DAYS:
   
Frost Days

FRQ_BRKNCLD_10_70_00_GMT:
   
Frequency Of Broken-cloud Skies 10 - 70 % At 00 GMT

FRQ_BRKNCLD_10_70_03_GMT:
   
Frequency Of Broken-cloud Skies 10 - 70 % At 03 GMT

FRQ_BRKNCLD_10_70_06_GMT:
   
Frequency Of Broken-cloud Skies 10 - 70 % At 06 GMT

FRQ_BRKNCLD_10_70_09_GMT:
   
Frequency Of Broken-cloud Skies 10 - 70 % At 09 GMT

FRQ_BRKNCLD_10_70_12_GMT:
   
Frequency Of Broken-cloud Skies 10 - 70 % At 12 GMT

FRQ_BRKNCLD_10_70_15_GMT:
   
Frequency Of Broken-cloud Skies 10 - 70 % At 15 GMT

FRQ_BRKNCLD_10_70_18_GMT:
   
Frequency Of Broken-cloud Skies 10 - 70 % At 18 GMT

FRQ_BRKNCLD_10_70_21_GMT:
   
Frequency Of Broken-cloud Skies 10 - 70 % At 21 GMT

FRQ_CLRSKY_0_10_00_GMT:
   
Frequency Of Clear Skies < 10 % At 00 GMT

FRQ_CLRSKY_0_10_03_GMT:
                             
Frequency Of Clear Skies < 10 % At 03 GMT

FRQ_CLRSKY_0_10_06_GMT:
   
Frequency Of Clear Skies < 10 % At 06 GMT

FRQ_CLRSKY_0_10_09_GMT:
                             
Frequency Of Clear Skies < 10 % At 09 GMT

FRQ_CLRSKY_0_10_12_GMT:
   
Frequency Of Clear Skies < 10 % At 12 GMT

FRQ_CLRSKY_0_10_15_GMT:
                             
Frequency Of Clear Skies < 10 % At 15 GMT

FRQ_CLRSKY_0_10_18_GMT:
   
Frequency Of Clear Skies < 10 % At 18 GMT

FRQ_CLRSKY_0_10_21_GMT:
                             
Frequency Of Clear Skies < 10 % At 21 GMT

FRQ_NROVRCST_70_00_GMT:
   
Frequency Of Near-overcast Skies >= 70 % At 00 GMT

FRQ_NROVRCST_70_03_GMT:
   
Frequency Of Near-overcast Skies >= 70 % At 03 GMT

FRQ_NROVRCST_70_06_GMT:
   
Frequency Of Near-overcast Skies >= 70 % At 06 GMT

FRQ_NROVRCST_70_09_GMT:
   
Frequency Of Near-overcast Skies >= 70 % At 09 GMT

FRQ_NROVRCST_70_12_GMT:
   
Frequency Of Near-overcast Skies >= 70 % At 12 GMT

FRQ_NROVRCST_70_15_GMT:
   
Frequency Of Near-overcast Skies >= 70 % At 15 GMT

FRQ_NROVRCST_70_18_GMT:
   
Frequency Of Near-overcast Skies >= 70 % At 18 GMT

FRQ_NROVRCST_70_21_GMT:
   
Frequency Of Near-overcast Skies >= 70 % At 21 GMT

HDD0:
   
Heating Degree Days Below 0 C

HDD10:
   
Heating Degree Days Below 10 C

HDD18_3:
   
Heating Degree Days Below 18.3 C

INSOL_MIN_CONSEC_1:
   
Minimum Available Insolation Over A Consecutive 1-day Period

INSOL_MIN_CONSEC_14:
   
Minimum Available Insolation Over A Consecutive 14-day Period

INSOL_MIN_CONSEC_21:
   
Minimum Available Insolation Over A Consecutive 21-day Period

INSOL_MIN_CONSEC_3:
   
Minimum Available Insolation Over A Consecutive 3-day Period

INSOL_MIN_CONSEC_7:
   
Minimum Available Insolation Over A Consecutive 7-day Period

INSOL_MIN_CONSEC_MONTH:
   
Minimum Available Insolation Over A Consecutive Month Period

KT:
   
Insolation Clearness Index

KT_CLEAR:
   
Clear Sky Insolation Clearness Index

MIDDAY_INSOL:
   
Midday Insolation Incident On A Horizontal Surface

NKT:
   
Normalized Insolation Clearness Index

NO_SUN_BLACKDAYS_MAX:
   
Maximum NO-SUN Or BLACK Days

PHIS:
   
Surface Geopotential

PRECTOT:
   
Precipitation

PS:
   
Surface Pressure

PSC:
   
Corrected Atmospheric Pressure (Adjusted For Site Elevation)

QV2M:
   
Specific Humidity at 2 Meters

RH2M:
   
Relative Humidity at 2 Meters

SG_DAY_COZ_ZEN_AVG:
   
Daylight Average Of Hourly Cosine Solar Zenith Angles

SG_DAY_HOUR_AVG:
   
Daylight Hours

SG_DEC_AVG:
   
Declination

SG_HR_AZM_ANG_AVG:
   
Hourly Solar Azimuth Angles

SG_HR_HRZ_ANG_AVG:
   
Hourly Solar Angles Relative To The Horizon

SG_HR_SET_ANG:
   
Sunset Hour Angle

SG_MAX_HRZ_ANG:
   
Maximum Solar Angle Relative To The Horizon

SG_MID_COZ_ZEN_ANG:
   
Cosine Solar Zenith Angle At Mid-Time Between Sunrise And Solar Noon

SG_NOON:
   
Solar Noon

SI_EF_TILTED_SURFACE_HORIZONTAL:
   
Solar Irradiance for Equator Facing Horizontal Surface

SI_EF_TILTED_SURFACE_LAT_MINUS15:
   
Solar Irradiance for Equator Facing Latitude Minus 15 Tilt

SI_EF_TILTED_SURFACE_LATITUDE:
   
Solar Irradiance for Equator Facing Latitude Tilt

SI_EF_TILTED_SURFACE_LAT_PLUS15:
   
Solar Irradiance for Equator Facing Latitude Plus 15 Tilt

SI_EF_TILTED_SURFACE_VERTICAL:
   
Solar Irradiance for Equator Facing Vertical Surface

SI_EF_OPTIMAL:
   
Solar Irradiance Optimal

SI_EF_OPTIMAL_ANG:
   
Solar Irradiance Optimal Angle

SI_EF_OPTIMAL_ANG_ORT:
   
Solar Irradiance Tilted Surface Orientation

SI_EF_TRACKER:
   
Solar Irradiance Irradiance Tracking the Sun

SI_EF_TILTED_SURFACE:
   
Solar Irradiance for Equator Facing Tilted Surfaces (Set of Surfaces)

SI_EF_MIN_TILTED_SURFACE_HORIZONTAL:
   
Minimum Solar Irradiance for Equator Facing Horizontal Surface

SI_EF_MIN_TILTED_SURFACE_LAT_MINUS15:
   
Minimum Solar Irradiance for Equator Facing Latitude Minus 15 Tilt

SI_EF_MIN_TILTED_SURFACE_LATITUDE:
   
Minimum Solar Irradiance for Equator Facing Latitude Tilt

SI_EF_MIN_TILTED_SURFACE_LAT_PLUS15:
   
Minimum Solar Irradiance for Equator Facing Latitude Plus 15 Tilt

SI_EF_MIN_TILTED_SURFACE_VERTICAL:
   
Minimum Solar Irradiance for Equator Facing Vertical Surface

SI_EF_MIN_OPTIMAL:
   
Minimum Solar Irradiance Optimal

SI_EF_MIN_OPTIMAL_ANG:
   
Minimum Solar Irradiance Optimal Angle

SI_EF_MIN_OPTIMAL_ANG_ORT:
   
Minimum Solar Irradiance Tilted Surface Orientation

SI_EF_MIN_TRACKER:
   
Minimum Solar Irradiance Irradiance Tracking the Sun

SI_EF_MIN_TILTED_SURFACE:
   
Minimum Solar Irradiance for Equator Facing Tilted Surfaces (Set of Surfaces)

SI_EF_MAX_TILTED_SURFACE_HORIZONTAL:
   
Maximum Solar Irradiance for Equator Facing Horizontal Surface

SI_EF_MAX_TILTED_SURFACE_LAT_MINUS15:
   
Maximum Solar Irradiance for Equator Facing Latitude Minus 15 Tilt

SI_EF_MAX_TILTED_SURFACE_LATITUDE:
   
Maximum Solar Irradiance for Equator Facing Latitude Tilt

SI_EF_MAX_TILTED_SURFACE_LAT_PLUS15:
   
Maximum Solar Irradiance for Equator Facing Latitude Plus 15 Tilt

SI_EF_MAX_TILTED_SURFACE_VERTICAL:
   
Maximum Solar Irradiance for Equator Facing Vertical Surface

SI_EF_MAX_OPTIMAL:
   
Maximum Solar Irradiance Optimal

SI_EF_MAX_OPTIMAL_ANG:
   
Maximum Solar Irradiance Optimal Angle

SI_EF_MAX_OPTIMAL_ANG_ORT:
   
Maximum Solar Irradiance Tilted Surface Orientation

SI_EF_MAX_TRACKER:
   
Maximum Solar Irradiance Irradiance Tracking the Sun

SI_EF_MAX_TILTED_SURFACE:
   
Maximum Solar Irradiance for Equator Facing Tilted Surfaces (Set of Surfaces)

SR:
   
Surface Roughness

SRF_ALB:
   
Surface Albedo

T10M:
   
Temperature at 10 Meters

T10M_MAX:
   
Maximum Temperature at 10 Meters

T10M_MIN:
   
Minimum Temperature at 10 Meters

T10M_RANGE:
   
Temperature Range at 10 Meters

T2M:

Temperature at 2 Meters

T2MDEW:
   
Dew/Frost Point at 2 Meters

T2MWET:
   
Wet Bulb Temperature at 2 Meters

T2M_MAX:
   
Maximum Temperature at 2 Meters

T2M_MIN:
   
Minimum Temperature at 2 Meters

T2M_RANGE:
   
Temperature Range at 2 Meters

TM_ZONES:
   
Climate Thermal and Moisture Zones

TQV:

Total Column Precipitable Water

TS:
   
Earth Skin Temperature

TS_AMP:
   
Earth Skin Temperature Amplitude

TS_MAX:
   
Maximum Earth Skin Temperature

TS_MIN:
   
Minimum Earth Skin Temperature

TS_RANGE:
   
Earth Skin Temperature Range

T_ZONES:
   
Climate Thermal Zones

U10M:
   
Eastward Wind at 10 Meters

V10M:
   
Northward Wind at 10 Meters

WS10M:
   
Wind Speed at 10 Meters

WS10M_MAX:
   
Maximum Wind Speed at 10 Meters

WS10M_MIN:
   
Minimum Wind Speed at 10 Meters

WS10M_RANGE:
   
Wind Speed Range at 10 Meters

WS2M:
   
Wind Speed at 2 Meters

WS2M_MAX:
   
Maximum Wind Speed at 2 Meters

WS2M_MIN:
   
Minimum Wind Speed at 2 Meters

WS2M_RANGE:
   
Wind Speed Range at 2 Meters

WS50M:
   
Wind Speed at 50 Meters

WS50M_MAX:
   
Maximum Wind Speed at 50 Meters

WS50M_MIN:
   
Minimum Wind Speed at 50 Meters

WS50M_RANGE:
   
Wind Speed Range at 50 Meters

WSC:
   
Corrected Wind Speed (Adjusted For Elevation)
</details>
   
   <h1> Sources Cited </h1> 
   Stackhouse, D. P. (n.d.). Prediction of worldwide energy resources (power). NASA. Retrieved May 12, 2022, from https://data.nasa.gov/Earth-Science/Prediction-Of-Worldwide-Energy-Resources-POWER-/wn3p-qsan 
