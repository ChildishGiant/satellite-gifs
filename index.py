import urllib.request
from datetime import datetime

day_of_year = datetime.now().timetuple().tm_yday

print(day_of_year)

testURL = "https://gibs.earthdata.nasa.gov/image-download?TIME=2018205&extent=-2.632324,50.124023,2.386231,54.268066&epsg=4326&layers=MODIS_Terra_CorrectedReflectance_TrueColor,Coastlines&opacities=1,1&worldfile=false&format=image/png&width=2284&height=1886"

urllib.request.urlretrieve(testURL, "new_file.png")