from io import TextIOBase
import justpy as jp
from pandas.core.dtypes.common import classes

def app():
    wp=jp.QuasarPage()
    h1=jp.QDiv(a=wp,text="Analysis",classes="text-h1 text-center q-pa-md")
    p1=jp.QDiv(a=wp,text="local grapth")
    return wp



jp.justpy(app)