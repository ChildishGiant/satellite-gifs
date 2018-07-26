# satellite-gifs

A script used to make gifs of the earth through time

## The anatomy of a url

`https://gibs.earthdata.nasa.gov/image-download?TIME=2018205&extent=-2.632324,50.124023,2.386231,54.268066&epsg=4326&layers=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines&opacities=1,1&worldfile=false&format=image/png&width=2284&height=1886`

Each argument is separated by an ampersand `&`

<http://gibs.earthdata.nasa.gov/image-download?>

- TIME=2018205
- extent=-2.632324,50.124023,2.386231,54.268066
- epsg=4326
- layers=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines
- opacities=1,1
- worldfile=false
- format=image/png
- width=2284
- height=1886

### TIME

This consists of 7 digits, the first 4 are the year you want to capture and the other 3 are the number of the day following [ISO 8601 Ordinal_dates](https://en.wikipedia.org/wiki/Ordinal_date)

``` python
from datetime import datetime
day_of_year = datetime.now().timetuple().tm_yday
```

### extent

Made up of four numbers, longitude and latitude of two points but are for some reason in reverse. I assumed that these would be the two corners of the capture area but this doesn't seem to be the case. The error messages call these MinX, MinY and MaxX, MaxY. It also says that MinX and MinY should be less than MaxX and MaxY respectively.

For example the URL we're looking through has these coordinates:

`2.632324,50.124023,2.386231,54.268066`

This is read by the computer as:

- 50.124023° North (Latitude), 2.632324° East (Longitude)
- -54.268066° North (Latitude), 2.386231° East (Longitude)
