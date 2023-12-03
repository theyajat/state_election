import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


colors = ['#EB4141', '#808080', '#808080']
raj_colors=['#EB4141', '#808080', '#808080', '#808080', '#808080', '#808080', '#808080']
telan_colors = ['#EB4141', '#808080', '#808080','#808080','#808080']
chat_colors=['#EB4141', '#808080', '#808080']

mp_data=pd.read_csv("MP_seats.csv")
rajasthan_data=pd.read_csv("Rajasthan_seats.csv")
telangana_data=pd.read_csv("telangana_data.csv")
chattisgarh_data=pd.read_csv("chattisgarh_data.csv")

state_option=['Madhya Pradesh','Rajasthan','Telangana','Chhattisgarh']
st.title("State Assembly Elections DEC2023")
options=st.selectbox("Choose the State you want to visualize",state_option)

if options=='Madhya Pradesh':
    fig=go.Figure(go.Bar(
        x=mp_data['Party'],
        y=mp_data['Seats'],text=mp_data['Seats'],
        marker_color=colors,
        width=0.5,base=dict(
            color='white',  # Set the border color
            width=2  # Set the border width
        )))
    fig.update_xaxes(tickfont=dict(size=13),title_text='')
    fig.update_yaxes(tickfont=dict(size=12),title_text='')
    fig.update_traces(textangle=0, textposition="outside",cliponaxis=False,hovertemplate="%{x}, %{y} <extra></extra>")
    fig.update_layout(font=dict(size=16),hoverlabel=dict(font=dict(size=16)))
    st.plotly_chart(fig)



if options=='Rajasthan':
    fig=go.Figure(go.Bar(
        x=rajasthan_data['Party'],
        y=rajasthan_data['Seats'],text=rajasthan_data['Seats'],
        marker_color=raj_colors,
        width=0.7))
    fig.update_xaxes(tickfont=dict(size=14),title_text='')
    fig.update_yaxes(tickfont=dict(size=12),title_text='')
    fig.update_traces(textangle=0, textposition="outside",cliponaxis=False,hovertemplate="%{x}, %{y} <extra></extra>")
    fig.update_layout(font=dict(size=16),hoverlabel=dict(font=dict(size=16)))
    st.plotly_chart(fig)


if options=='Telangana':
    fig=go.Figure(go.Bar(
        x=telangana_data['Party'],
        y=telangana_data['Seats'],text=telangana_data['Seats'],
        marker_color=raj_colors,
        width=0.7))
    fig.update_xaxes(tickfont=dict(size=13),title_text='')
    fig.update_yaxes(tickfont=dict(size=12),title_text='')
    fig.update_traces(textangle=0, textposition="outside",cliponaxis=False,hovertemplate="%{x}, %{y} <extra></extra>")
    fig.update_layout(font=dict(size=16),hoverlabel=dict(font=dict(size=16)))
    st.plotly_chart(fig)

if options=='Chhattisgarh':
    fig=go.Figure(go.Bar(
        x=chattisgarh_data['Party'],
        y=chattisgarh_data['Seats'],text=chattisgarh_data['Seats'],
        marker_color=chat_colors,
        width=0.5))
    fig.update_xaxes(tickfont=dict(size=13),title_text='')
    fig.update_yaxes(tickfont=dict(size=12),title_text='')
    fig.update_traces(textangle=0, textposition="outside",cliponaxis=False,hovertemplate="%{x}, %{y} <extra></extra>")
    fig.update_layout(font=dict(size=16),hoverlabel=dict(font=dict(size=16)))
    st.plotly_chart(fig)
