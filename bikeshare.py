#Import Libraries
import time
import pandas as pd
import numpy as np

#City Data Dictionary
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city not in CITY_DATA.keys():
        print("\nWould you like to see data for Chicago, New York, or Washington? \n")
        city = input().lower()

 

        if city not in CITY_DATA.keys():
            print("\nInvalid City! Please check your input and try again.")

 


    # TO DO: get user input for month (all, january, february, ... , june)
    MONTH_DATA = {'january': 1, 'february': 2, 'march': 3, 'april': 4, 'may': 5, 'june': 6, 'all': 7}
    month = ''
    while month not in MONTH_DATA.keys():
        print("\nWhich month would you like to filter the data by? January through June, or type \"All\" for no filter.\n")
        month = input().lower()

 

        if month not in MONTH_DATA.keys():
            print("\nInvalid Month! Please check your input and try again.")

 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    DAY_LIST = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = ''
    while day not in DAY_LIST:
        print("\nWhich day of the week would you like to filter the data by? (Type \"All\" for no filter.)\n")
        day = input().lower()

 

        if day not in DAY_LIST:
            print("n\Invalid Day! Please check your input and try again.")

 


    print('-'*40)
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
    # load data for city
    print("\nLoading Data...")
    df = pd.read_csv(CITY_DATA[city])

 

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

 

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

 

    # filter by month
    if month != 'all':
          months = ['january','february','march','april','may','june']
          month = months.index(month) + 1

 

          df = df[df['month'] == month]

 

    # filter by day
    if day != 'all':
          # filter by day of week to create the new dataframe
          df = df[df['day_of_week'] == day.title()]

 


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\nMost Common Month\n', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nMost Common Day\n', common_day)

    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_hour = df['Hour'].mode()[0]
    print('\nMost Common Start Hour\n', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('\nMost Commonly Used Start Station\n', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('\nMost Commonly Used End Station\n', common_end)


    # TO DO: display most frequent combination of start station and end station trip
    common_start_end = (df['Start Station'] + ' - ' + df['End Station']).mode()[0]
    print('\nMost Popular Combination of Start and End Stations\n', common_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time', total_time, 'seconds', total_time/3600, 'hours')


    # TO DO: display mean travel time
    avg_time = df['Trip Duration'].mean()
    print('Average Travel Time', avg_time, 'seconds', avg_time/3600, 'hours')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('Counts of User Types\n', df['User Type'].value_counts());

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print('\nGender Count\n', df['Gender'].value_counts());
    
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
     earliest_byear = int(df['Birth Year'].min())
     print('\nEarliest Birth Year\n', earliest_byear)
     recent_byear = int(df['Birth Year'].max())
     print('\nMost Recent Birth Year\n', recent_byear)
     common_byear = int(df['Birth Year'].mode()[0])
     print('\nMost Common Birth Year\n', common_byear)                   


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
#show raw data
    start_line = 0
    end_line = 5

 

    show_data = input("Would you like to see raw data?: (yes)(no) ").lower()
    if show_data == 'yes':
        while end_line <= df.shape[0] - 1:
            print(df.iloc[start_line:end_line,:])
            start_line += 5
            end_line += 5
            show_data_end = input("More?: ").lower()
            if show_data_end == 'no':
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
