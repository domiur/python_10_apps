from video import df 
from bokeh.plotting import output_file,show,figure

f=figure(width=500,height=500,x_axis_type="datetime")
f.yaxis.minor_tick_line_color=None
#f.ygrid.ticker.desired_num_ticks=1
f.quad(left=df["start"],right=df["end"],top=1,bottom=0,color='green')
output_file("2.html")
show(f)

