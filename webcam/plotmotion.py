from bokeh.models.annotations import Tooltip
from video import df 
from bokeh.plotting import output_file,show,figure
from bokeh.models import HoverTool,ColumnDataSource


df['start_str']=df['start'].dt.strftime("%Y-%m-%d %H:%M:%S")
df['end_str']=df['end'].dt.strftime("%Y-%m-%d %H:%M:%S")
cds=ColumnDataSource(df)

f=figure(width=500,height=500,x_axis_type="datetime")
f.yaxis.minor_tick_line_color=None

hover=HoverTool(tooltips=[("Start","@start_str"),("End","@end_str")])
f.add_tools(hover)

f.quad(left="start",right="end",top=1,bottom=0,color='green',source=cds)

output_file("2.html")
show(f)

