import time
import pandas as pd
import numpy as np

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
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New york, or Washington? do not include spaces ").lower()
        if city not in CITY_DATA.keys():
            print( "something is wrong, make sure city is exsit and will written")
            continue
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input( "select a month:january, february, march, april, may, june , all? " ).lower()
        if month not in ('january', 'february', 'march', 'april', 'may', 'june' , 'all'):
            print ('try again')
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("select a day: all, monday, tuesday,.....").lower()
        if day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday','sunday','all'):
            print('try agian')
            continue
        else:
            break

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
# load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print("most popular month",popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print("most popular day",popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]
    print('Most popular start station',popular_start)

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]
    print('Most popular end station',popular_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['combination'] = df['Start Station'] + " to " + df['End Station']
    popular_combination = df['combination'].mode()[0]
    print('most popular most is from ',popular_combination)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('total travel time',total_travel_time)

    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time',mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # TO DO: Display counts of gender
    try:
        gender_counts = df['Gender'].value_counts()
        print(gender_counts)
    except KeyError:
        print("this city does not hold data for gender")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest= df['Birth Year'].min()
        print('earliest year of birth' , earliest)
    except KeyError:
        print("this city does not hold data for birth year")
        
    try:
        recent = df['Birth Year'].max()
        print('recent year of birth' , recent)
    except KeyError:
        print("this city does not hold data for birth year")
        
    try:
        common = df['Birth Year'].mode()[0]
        print('most popular year of birth' , common)
    except KeyError:
        print("this city does not hold data for birth year")
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        first_row = 0
        fifth_row = 5
        
        row_data = input('whould you like to see 5 lines of row data? type yes or no ').lower()
        if row_data == 'yes':
                
                while True:
                    print (df.iloc[first_row:fifth_row])
                    first_row += 5
                    fifth_row += 5
                    more_data = input(' would you like to see more row data? type yes or no ').lower()
                    if more_data != 'yes':
                        break
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
