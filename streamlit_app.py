  
import streamlit as st
import pandas as pd
import numpy as np
import requests
from plotly.offline import iplot
import plotly.graph_objs as go
import plotly.express as px
from pandas.io.json import json_normalize
from streamlit.script_runner import StopException, RerunException

st.write('Coronavirus is officially a pandemic. Since the first case in december the disease has spread fast reaching almost every corner of the world.'+
         'They said it\'s not a severe disease but the number of people that needs hospital care is growing as fast as the new cases.'+
         'Some governments are taking measures to prevent a sanitary collapse to be able to take care of all these people.'+
         'I\'m tackling this challenge here. Let\'s see how some countries/regions are doing!')
