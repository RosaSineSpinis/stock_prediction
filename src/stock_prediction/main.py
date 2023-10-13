# pip install streamlit fbprophet yfinance plotly
from datetime import date

import yfinance as yf
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly

from prophet import Prophet
from plotly import graph_objs as go
from prophet.plot import plot_plotly, plot_components_plotly

print("hello world")