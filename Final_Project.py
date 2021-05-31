"""
File: Final_Project.py
---------------------------------------------------------

The program shows gender ratio across 500 different Indian cities in the form of a
graphic.

"""

from simpleimage import SimpleImage

#Dimesions of the image
VISUALIZATION_WIDTH = 350
VISUALIZATION_HEIGHT = 300

# The limits of the position coordinates are set as per the maximun and minimum
# latitudes and longitudes for India
MAX_LATITUDE = 35
MIN_LATITUDE = 8
MAX_LONGITUDE = 95
MIN_LONGITUDE = 65

MAX_GREEN_VALUE = 255
MAX_BLUE_VALUE = 255
MAX_RED_VALUE = 255

def main():
    visualization = SimpleImage.blank(VISUALIZATION_WIDTH, VISUALIZATION_HEIGHT)
    
    lat_list = []
    lon_list = []
    gender_ratio_list = []
    with open("cities_r2.csv") as f:
        next(f)
        for line in f:
            line = line.strip()
            lat_list.append(float(line.split(',')[-5].strip('"')))
            lon_list.append(float(line.split(',')[-4].strip('"')))
            gender_ratio_list.append(float(line.split(',')[13]))
    
    plot_cities(visualization, lat_list, lon_list, gender_ratio_list)
    
    visualization.show()
    
def plot_cities(visualization, lat_list, lon_list, gender_ratio_list):
    """
    The function takes the blank image and list of latitude, longitude and
    gender ratio for the cities. It then loops over these lists and sends one 
    city at a time to the plot_pixel function.
    """
    for i in range(len(lat_list)):
        y = latitude_to_y(lat_list[i])
        x = longitude_to_x(lon_list[i])
        
        if 0 < x < visualization.width and 0 < y < visualization.height:
            plot_pixel(visualization, x, y, gender_ratio_list[i])
            
def plot_pixel(visualization, x, y, gender_ratio):
    """
    It takes the x, y coordinates for a pixel and decides its color based on 
    the gender ratio for that city.
    If the gender ratio is poor, then the city is shown in red color.
    If the gender ratio is moderate, then the city is shown in blue color.
    If the gender ratio is healthy, then the city is shown in green color.
    """
    pixel = visualization.get_pixel(x, y)
    if gender_ratio < 900:
        pixel.red = MAX_RED_VALUE
        pixel.green = 0
        pixel.blue = 0
    elif gender_ratio < 1000:
        pixel.red = 0
        pixel.green = 0
        pixel.blue = MAX_BLUE_VALUE
    else:
        pixel.red = 0
        pixel.green = MAX_GREEN_VALUE
        pixel.blue = 0
        
def longitude_to_x(longitude):
    """
    Takes the longitude for a city and converts it to correspoding x coordinate
    on the image scale.
    """
    return VISUALIZATION_WIDTH * (longitude - MIN_LONGITUDE)/(MAX_LONGITUDE - MIN_LONGITUDE)

def latitude_to_y(latitude):
    """
    Takes the latitude for a city and converts it to correspoding y coordinate
    on the image scale.
    """
    return VISUALIZATION_HEIGHT * (1-(latitude - MIN_LATITUDE)/(MAX_LATITUDE - MIN_LATITUDE))
    
if __name__ == '__main__':
    main()
            
        
        
        