from flask import Flask, render_template
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import squarify as sq
import plotly.io as pio
pio.templates
import seaborn as sns
import resample as rs

app = Flask(__name__)

def load_data():
    df = pd.read_csv('dataset/funding.csv')
    return df

def load_data1():
    df_top_industry_vertical = pd.read_csv('dataset/funding.csv')
    return df_top_industry_vertical

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graphs')
def graphs():
   df=load_data()
   fig1 = px.pie(df, values='Amount in USD', names='Industry Vertical', title='Amount in USD by Industry Vertical',
            color='Industry Vertical',
            labels={'Industry Vertical':'Industry Vertical'},
            width=1000, height=600, template='none',
            color_discrete_sequence=px.colors.sequential.RdBu)
            fig.update_traces(textposition='inside', textinfo='percent+label', hole=0.4, marker=dict(line=dict(color='#000000', width=2)),
                   opacity=0.8, rotation=45, textfont_size=15, texttemplate='%{label}<br>%{value:$,.2f}'
                        and '%{percent}')
   
   fig2 = px.histogram(df_top_industry_vertical,
                    x="Amount in USD", y="Industry Vertical", color="Industry Vertical", hover_name="Startup Name", log_x=True,width=1000, height=600,
                title="Amount in USD by Industry Vertical", labels={"Amount in USD": "Amount in USD", "Industry Vertical": "Industry Vertical"}, template='plotly_white',
                color_discrete_sequence=px.colors.qualitative.Dark24, nbins=100, )
   
   fig6= px.scatter_polar(df[:70], r="Amount in USD", theta="Industry Vertical", color="Industry Vertical", hover_name="Startup Name", log_r=True, size_max=60,
                title="Amount in USD by Industry Vertical", labels={"Amount in USD": "Amount in USD", "Industry Vertical": "Industry Vertical"},  width=1000, height=600, symbol="Industry Vertical",
                color_discrete_sequence=px.colors.qualitative.Dark24, template='none')
   return render_template('graphs.html',fig1=fig1.html(),fig2=fig2.html(),fig6=fig6)

@app.route('/graphs1')
def 
         

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 