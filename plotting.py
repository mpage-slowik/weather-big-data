import matplotlib.pyplot as plt
import mplleaflet
import threading, time
from Model import earthquake,tsunami,weather
import pandas as pd
from random import randint
from string import Template
class Threading(object):
    def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.plotPoints, args=("earthquakes",earthquake.getData(),'go'))
        thread.daemon = True
        thread.start()
        thread = threading.Thread(target=self.plotPoints, args=("tsunami",tsunami.getDataTsunami(),'bo'))
        thread.daemon = True
        thread.start()
        thread = threading.Thread(target=self.plotWeather, args=("weather","weather",weather.getHailReports(),weather.getWindReports(),weather.getTornadoReports()))
        thread.daemon = True
        thread.start()

    def plotPoints(self,map_name,lat_long,cl):
        while(True):
            fig, ax = plt.subplots()
            x = [lat_long['lng']]
            y = [lat_long['lat']]
            ax.plot(x, y, cl)
            maps="templates/"+map_name+".html"
            f=open(maps,"w")
            f.write(mplleaflet.fig_to_html(fig=fig))
            f.close()
            time.sleep(self.interval)
    def plotWeather(self,map_name,hail_la_ln,wind_la_ln,tornado_la_ln):
        while(True):
            fig, ax = plt.subplots()
            x = [hail_la_ln['lng']]
            y = [hail_la_ln['lat']]
            ax.plot(x, y, 'b*')
            x = [wind_la_ln['lng']]
            y = [wind_la_ln['lat']]
            ax.plot(x, y, 'b>')
            x = [tornado_la_ln['lng']]
            y = [tornado_la_ln['lat']]
            ax.plot(x, y, 'b^')
            maps="templates/"+map_name+".html"
            f=open(maps,"w")
            f.write(mplleaflet.fig_to_html(fig=fig))
            f.close()
            time.sleep(self.interval)
#start threading
threads = Threading(600)
# if __name__ == '__main__':
#     plotPoints("templates/default.html")