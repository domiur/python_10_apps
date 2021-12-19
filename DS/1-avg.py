import justpy as jp
from pandas.core.dtypes.common import classes
import pandas

df=pandas.read_csv("reviews.csv",parse_dates=["Timestamp"])
df['Day']=df["Timestamp"].dt.date
df_avg=df.groupby('Day').mean()


chart_def="""
{
  chart: {
    type: 'spline',
    inverted: false
  },
  title: {
    text: 'Averate rating'
  },
  xAxis: {
    reversed: false,
    title: {
      enabled: true,
      text: 'Date'
    },
    labels: {
      format: '{value}'
    },
    maxPadding: 0.05,
    showLastLabel: true
  },
  yAxis: {
    title: {
      text: 'Average rating'
    },
    labels: {
      format: '{value}'
    },
    lineWidth: 2
  },
  legend: {
    enabled: true
  },
  tooltip: {
    headerFormat: '<b>{series.name}</b><br/>',
    pointFormat: '{point.x} {point.y}'
  },
  plotOptions: {
    spline: {
      marker: {
        enable: false
      }
    }
  },
  series: [{
    name: 'average rating',
    data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
      [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
  }]
}
"""


def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp,text="Analysis",classes="text-h1 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="local grapth")
    hc=jp.HighCharts(a=wp,options=chart_def)
    hc.options.series[0].name="tttt"
    x=df_avg.index
    y=df_avg['Rating']
    hc.options.xAxis.categories=list(x)
    hc.options.series[0].data=list(y)
    # OR for x,y numbers can be used 
    #hc.options.series[0].data=list(zip(x,y))
    
    return wp



jp.justpy(app)