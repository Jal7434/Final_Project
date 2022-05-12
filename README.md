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
   
   
   
   <h1> Sources Cited </h1> 
   Stackhouse, D. P. (n.d.). Prediction of worldwide energy resources (power). NASA. Retrieved May 12, 2022, from https://data.nasa.gov/Earth-Science/Prediction-Of-Worldwide-Energy-Resources-POWER-/wn3p-qsan 
