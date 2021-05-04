import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px


df_sm = pd.read_csv('player_stats_sm.csv', index_col=0)
df_sm.head()


def filter_by_weeks(weeks, df):
    round_list = []
    latest_round = df['round'].max()
    round_list.append(latest_round)
    for i in range(weeks-1):
        latest_round -= 1
        round_list.append(latest_round)
    return round_list


position = 'Defender'
weeks = 4
# ['Midfielder' 'Defender' 'Forward' 'Goalkeeper']


st.title('Premier League Dashboard')
position = st.selectbox('Position', options=[
    'Midfielder', 'Defender', 'Forward', 'Goalkeeper'])
weeks = int(st.text_input('How many weeks back? ', 4))
st.text('Total points per game for the last ' +
        str(weeks) + ' games for ' + position + 's')


filtered_df = df_sm[(df_sm['round'].astype(
    'int64').isin(filter_by_weeks(weeks, df_sm)))]
filtered_df = filtered_df[filtered_df['position_name'] == position]
# which goalie has hightest total poiints
total_points_by_pos = filtered_df.groupby(['element', 'name', 'team_name'])[
    'total_points'].sum()
tp_by_points = total_points_by_pos[total_points_by_pos > 10]
tp_by_points = tp_by_points.sort_values(ascending=False)
tp_by_points = tp_by_points.to_frame().reset_index().set_index('element')

#tp_by_points_chart = tp_by_points.drop('element', axis=1)
st.write(tp_by_points)

# data wrangle for charts
top_ids = tp_by_points.index.to_list()
top_ids = top_ids[0:5]

df_top = filtered_df[filtered_df['element'].isin(top_ids)]

# plot
fig = px.line(df_top, x='round', y='total_points',
              color='name', hover_name='name', title='Performance of top players by week')

st.plotly_chart(fig, use_container_width=True)
