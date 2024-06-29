import streamlit as st
import pandas as pd
import numpy as np
import time

# Các hằng số
CITY_DATA = {
    'Chicago': 'chicago.csv',
    'New York City': 'new_york_city.csv',
    'Washington': 'washington.csv'
}
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'All':
        month = MONTHS.index(month) + 1
        df = df[df['month'] == month]

    if day != 'All':
        df = df[df['day_of_week'] == day.title()]

    return df

def calculate_stats(df):
    stats = {}
    stats['popular_month'] = df['month'].mode()[0]
    stats['popular_day'] = df['day_of_week'].mode()[0]
    df['hour'] = df['Start Time'].dt.hour
    stats['popular_hour'] = df['hour'].mode()[0]
    stats['popular_start_station'] = df['Start Station'].mode()[0]
    stats['popular_end_station'] = df['End Station'].mode()[0]
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    stats['popular_trip'] = df['trip'].mode()[0]
    stats['total_travel_time'] = df['Trip Duration'].sum()
    stats['mean_travel_time'] = df['Trip Duration'].mean()
    stats['user_types'] = df['User Type'].value_counts().to_dict()
    if 'Gender' in df:
        stats['gender_counts'] = df['Gender'].value_counts().to_dict()
    if 'Birth Year' in df:
        stats['earliest_year'] = int(df['Birth Year'].min())
        stats['recent_year'] = int(df['Birth Year'].max())
        stats['common_year'] = int(df['Birth Year'].mode()[0])
    return stats

def main():
    st.title('Explore US Bikeshare Data')

    st.sidebar.header('User Input Parameters')
    city = st.sidebar.selectbox('Select a city', list(CITY_DATA.keys()))
    month = st.sidebar.selectbox('Select a month', ['All'] + MONTHS)
    day = st.sidebar.selectbox('Select a day of the week', ['All'] + DAYS)

    df = load_data(city, month, day)
    
    st.write(f"Displaying data for {city}")
    st.write(df.head())

    stats = calculate_stats(df)
    
    st.subheader('Statistics')
    st.write('Most Popular Month:', stats['popular_month'])
    st.write('Most Popular Day:', stats['popular_day'])
    st.write('Most Popular Start Hour:', stats['popular_hour'])
    st.write('Most Popular Start Station:', stats['popular_start_station'])
    st.write('Most Popular End Station:', stats['popular_end_station'])
    st.write('Most Popular Trip:', stats['popular_trip'])
    st.write('Total Travel Time:', stats['total_travel_time'])
    st.write('Mean Travel Time:', stats['mean_travel_time'])
    st.write('User Types:', stats['user_types'])
    if 'gender_counts' in stats:
        st.write('Gender Counts:', stats['gender_counts'])
    if 'earliest_year' in stats:
        st.write('Earliest Year:', stats['earliest_year'])
        st.write('Most Recent Year:', stats['recent_year'])
        st.write('Most Common Year:', stats['common_year'])

    if st.checkbox('Show raw data'):
        st.subheader('Raw Data')
        st.write(df)

if __name__ == "__main__":
    main()
