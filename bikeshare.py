import time
import pandas as pd
import numpy as np

# Các hằng số
CITY_DATA = {
    '1': 'chicago.csv',
    '2': 'new_york_city.csv',
    '3': 'washington.csv'
}
MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
SEPARATOR = '-'*40

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city (chicago, new york city, washington)
    while True:
        print('Please choose a city:')
        print('1. Chicago')
        print('2. New York City')
        print('3. Washington')
        city = input('Enter the number corresponding to the city: ')
        if city in CITY_DATA:
            break
        else:
            print('Invalid input. Please enter a number between 1 and 3.')

    # Get user input for month (all, january, february, ... , june)
    while True:
        print('Please choose a month:')
        print('1. January')
        print('2. February')
        print('3. March')
        print('4. April')
        print('5. May')
        print('6. June')
        print('7. All')
        month = input('Enter the number corresponding to the month or "7" for no month filter: ')
        if month in [str(i) for i in range(1, 8)]:
            if month == '7':
                month = 'all'
            else:
                month = MONTHS[int(month) - 1]
            break
        else:
            print('Invalid input. Please enter a number between 1 and 7.')

    # Get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        print('Please choose a day of the week:')
        print('1. Monday')
        print('2. Tuesday')
        print('3. Wednesday')
        print('4. Thursday')
        print('5. Friday')
        print('6. Saturday')
        print('7. Sunday')
        print('8. All')
        day = input('Enter the number corresponding to the day or "8" for no day filter: ')
        if day in [str(i) for i in range(1, 9)]:
            if day == '8':
                day = 'all'
            else:
                day = DAYS[int(day) - 1]
            break
        else:
            print('Invalid input. Please enter a number between 1 and 8.')

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month != 'all':
        # Use the index of the months list to get the corresponding int
        month = MONTHS.index(month) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month
    popular_month = df['month'].mode()[0]
    print('Most Popular Month:', popular_month)

    # Display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most Popular Day of Week:', popular_day)

    # Display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(SEPARATOR)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Most Popular Start Station:', popular_start_station)

    # Display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Most Popular End Station:', popular_end_station)

    # Display most frequent combination of start station and end station trip
    df['trip'] = df['Start Station'] + " to " + df['End Station']
    popular_trip = df['trip'].mode()[0]
    print('Most Popular Trip:', popular_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(SEPARATOR)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_travel_time)

    # Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(SEPARATOR)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('User Types:\n', user_types)

    # Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print('\nGender Counts:\n', gender_counts)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_year = int(df['Birth Year'].min())
        recent_year = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nEarliest Year:', earliest_year)
        print('Most Recent Year:', recent_year)
        print('Most Common Year:', common_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print(SEPARATOR)


def display_raw_data(df):
    """Displays raw data upon request by the user."""
    row = 0
    while True:
        display = input('Would you like to see 5 lines of raw data? Enter yes or no: ').lower()
        if display == 'yes':
            print(df.iloc[row:row+5])
            row += 5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
    main()
