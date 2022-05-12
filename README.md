<h1> Power Consumption and Renewable Resources </h1>
   <details> <summary> <h4>Disclamer</h4> </summary> This repository contains all of the files for the Final project for COE332.
  Due to complication with site resources of data some data was made unavailable 
   </details>
   
<h2> Introduction </h2>
This project should allow users to go throuhg large amounts of data from Prediction of Worldwide Energy Resource or POWER and access specified and general data about worldwide meterological and radiation data. The project uses dynamically updated monthly data which contains mmeteorological data and radiation data about the world.

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
  
