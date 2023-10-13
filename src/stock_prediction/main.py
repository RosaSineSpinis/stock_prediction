# pip install streamlit fbprophet yfinance plotly
from datetime import date

import yfinance as yf
# from fbprophet import Prophet
# from fbprophet.plot import plot_plotly

from prophet import Prophet
from plotly import graph_objs as go
from prophet.plot import plot_plotly, plot_components_plotly

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

stocks = ('GOOG', 'AAPL', 'MSFT', 'GME')
selected_stock = stocks[0]

# n_years = st.slider('Years of prediction:', 1, 4)
n_years = 1
period = n_years * 365

data = yf.download(selected_stock , START, TODAY)
data.reset_index(inplace=True)
print("data ", data.head(), data.tail())

print('\nLoading data... done!')


# Plot raw data
def plot_raw_data():
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
    fig.layout.update(title_text='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
    fig.show()


plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date', 'Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# # Show and plot forecast
print(forecast.tail())

print(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
fig1.show()

# plot_components_plotly
# fig2 = m.plot_components(forecast)
fig2 = plot_components_plotly(m, forecast)
fig2.show()