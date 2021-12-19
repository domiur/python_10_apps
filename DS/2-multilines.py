import justpy as jp
from pandas.core.dtypes.common import classes
import pandas

df=pandas.read_csv("reviews.csv",parse_dates=["Timestamp"])
df['month']=df["Timestamp"].dt.strftime("%Y-%m")
df_avg=df.groupby(['month','Course Name'])['Rating'].mean().unstack()
print(df_avg.head())

chart_def="""
{
    chart: {
        type: 'spline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor: '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""


def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp,text="Analysis",classes="text-h1 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="local grapth")
    hc=jp.HighCharts(a=wp,options=chart_def)
    hc.options.xAxis.categories=list(df_avg.index)

    hc.options.series=[ {"name":v1,"data":[v2 for v2 in df_avg[v1]]} for v1 in df_avg.columns ]
    
    #x=df_avg.index
    #y=df_avg['Rating']
    #hc.options.xAxis.categories=list(x)
    #hc.options.series[0].data=list(y)
    # OR for x,y numbers can be used 
    #hc.options.series[0].data=list(zip(x,y))
    
    return wp



jp.justpy(app)