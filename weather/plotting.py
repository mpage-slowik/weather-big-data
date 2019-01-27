import matplotlib.pyplot as plt
import mplleaflet
import numpy as np
import pandas as pd
from random import randint
from string import Template
import io
import base64
def plotPoints(map_name):
    fig, ax = plt.subplots()
    x = [randint(-10100, -9400)/100 for i in range(30)]
    y = [randint(3700, 4000)/100 for i in range(30)]
    ax.plot(x, y, 'bo')
    maps="templates/"+map_name+".html"
    f=open(maps,"w")
    f.write(mplleaflet.fig_to_html(fig=fig))
    f.close()
   # return mplleaflet.fig_to_html()
    # img = io.BytesIO()
    # df = pd.DataFrame(np.random.randn(4, 4), index=list('ABCD'),columns=list('ABCD'))
    # lat = [1.1,2.0,1.3]
    # lon = [2.2,4.0,2.3]
    # count = [1000,2,3]
    # plt.scatter(lat, lon, c=count)
    # plt.colorbar()
    # plt.savefig(img, format='png')
    # img.seek(0)
    # graph_url = base64.b64encode(img.getvalue()).decode()
    # plt.close()
    #return 'data:image/png;base64,{}'.format(graph_url)
if __name__ == '__main__':
    plotPoints()