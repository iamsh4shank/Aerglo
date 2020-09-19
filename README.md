# Aerglo :milky_way:
A python-based tool to fetch astronomical images  - 
- Astronomical Picture of the Day (APOD)
- taken by Mars Rover
- Earth Polychromatic Imaging Camera (EPIC)
- Earth Observation Data

By using this tool you will know how beautiful our universe it :heart_eyes: It also allows you to classify galaxies based on the galaxy data which contains parameters like frequency bands, various visual angles, geometry, temperature, etc. All the data is fetched from NASA open [APIs](https://api.nasa.gov/). 


## :camera: Screenshots
<table>
     <tr>
          <td><img src="https://i.imgur.com/4L7xONq.png" /><br /><center><b>APOD</b></center></td>
          <td><img src="https://i.imgur.com/Sh50US8.png" /><br /><center><b>Mars</b></center></td>
          <td><img src="https://i.imgur.com/t0HRysk.png" /><br /><center><b>Earth Observation Data</b></center></td>
     </tr>
     <tr>
         <td><img src="https://i.imgur.com/df2NZBX.png" /><br /><center><b>EPIC</b></center></td>
         <td><img src="https://i.imgur.com/Cr7Vvcg.png" /><br /><center><b>Galaxy Classifier</b></center></td>
         <td><img src="https://i.imgur.com/AFufcgJ.png" /><br /><center><b>CLI demo</b></center></td>
       </tr>
</table>


## :question: How it Works

This tool provides you a feature to fetch images based on your choice. For running this you need to write ```python3.6 aerglo_fetch.py <choice>```. Here ```<choice>``` can be - 
- -apod ------> for APOD  
- -marsR ------> for fetching images taken by Mars Rover
- -epic ------> for images by earth polychromatic imaging camera
- -earth ------> for images by earth observation data
- -clGal ------> for galaxy classification 
- -help ------> for any help

It provides data filtering based on various parameters like date, name, id, etc. For galaxy-classification, it provides a demo dataset that contains data of 780 galaxies by SDSS having various kinds of shapes like rectangular, elliptical, merger, spiral, etc. Users can also provide his dataset by providing a file.npy which contains galaxy records.




## :satellite: Technology Stack

* Python 3.6
* NASA open APIs
* Jupyter Notebook
* Astropy library
* Scimage library
* MatplotLib
* Json
* Sklearn library

## :key: Contribution
This project is far away from perfect so it would be great if you contribute to make it great. Few ideas I can provide like you can enhance this tool by adding more API functionalities or also enable .csv instead of just processing on .npy for galaxy classification. Also, a lot of analysis part can be introduced in the tool. Hope to see good your contributions. 


## :wrench: How to use Aerglo

1. Clone the repository
1. Go to the folder and type ```python3.6 aerglo_fetch <choice>```, for choice see ```How it Works```section.

