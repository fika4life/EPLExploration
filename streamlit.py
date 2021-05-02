import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


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
total_points_by_pos = filtered_df.groupby(['name', 'team_name'])[
    'total_points'].sum()
tp_by_points = total_points_by_pos[total_points_by_pos > 10]
tp_by_points = tp_by_points.sort_values(ascending=False)


st.write(tp_by_points)

# data wrangle for charts
tp_by_points
st.line_chart(tp_by_points)
