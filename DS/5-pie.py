import justpy as jp
from pandas.core.dtypes.common import classes
import pandas

df=pandas.read_csv("reviews.csv",parse_dates=["Timestamp"])

df_avg=df.groupby(['Course Name'])['Rating'].count() 

chart_def="""
{
    chart: {
        type: 'pie'
    },
     plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""


def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp,text="Analysis",classes="text-h1 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="local grapth")
    hc=jp.HighCharts(a=wp,options=chart_def)
    #hc.options.series[0].name="tttt"
    #x=df_avg.index
    #hc.options.xAxis.categories=list(x)
    hc.options.series[0].data=[{"name":v1,"y":v2} for v1,v2 in zip(df_avg.index,df_avg)]
    #hc.options.series[0].data[0]["sliced"]=True
    #hc.options.series[0].data[0]["selected"]=True
    print(hc.options.series)
    # OR for x,y numbers can be used 
    #hc.options.series[0].data=list(zip(x,y))
    
    return wp



jp.justpy(app)