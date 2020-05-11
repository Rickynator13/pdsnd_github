import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
        try:
            city = input('Which city would you like to explore data from: Chicago, New York or Washington: ').lower()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if city in ('chicago', 'new york', 'washington'):
            break
        else:
            print("Not an appropriate choice.")
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        try:
            month = input('Which month would you like to filter data from: ').lower()
        except ValueError:
            print("Sorry, please try again.")
            continue
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        if month in (months):
            break
        else:
            print("Not an appropriate choice.")
            continue


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day = input('Which day would you like to explore data from: ').lower()
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue
        days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        if day not in (days):
            print("Not an appropriate choice.")
            continue
        else:
            #We are happing with the value given
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
    df['day_of_week'] =  df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour


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

    print('The most common month is: {}'.format( popular_month))
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day of the week: {}'.format(popular_day))
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hours: {}'.format(popular_hour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_StartStation = df['Start Station'].mode()[0]
    print('The most common start station is: {}'.format(most_common_StartStation))

    # TO DO: display most commonly used end station
    most_common_EndStation = df['End Station'].mode()[0]
    print('The most common end station is: {}'.format(most_common_EndStation))

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df.groupby('Start Station')['End Station'].max()[0]
    print('The most common trip is: {}'.format(most_common_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('\nThe total travel time is: {}\n'.format(total_travel_time))

    # TO DO: display mean travel time
    avg_travel_time = df['Trip Duration'].mean()
    print('\nThe average travel time is: {}\n'.format(avg_travel_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_count = df['User Type'].value_counts()
    print('\nThe total users count is: {}\n'.format(user_count))

    #In case city doesn't collects user gender and age data
    try:
        # TO DO: Display counts of gender
        gender_count = df['Gender'].value_counts()
        print('\nThe total of male and female users: {}\n'.format(gender_count))

        # TO DO: Display earliest, most recent, and most common year of birth
        youngest_user = df['Birth Year'].max()
        oldest_user = df['Birth Year'].min()
        mode_user = df['Birth Year'].mode()
        print('The youngest user year of birth is: {}'.format(youngest_user))
        print('The oldest user year of birth is: {}'.format(oldest_user))
        print('The most common user year of birth is: {}'.format(mode_user))

    except:
        print("\nWashigton does not contain gender\n'")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def explore_more_data(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    raw_data = input('Would you like to explore more data? Type \'yes\' or \'no\'.\n').lower()
    n = 0

    while raw_data == 'yes':
        print(df[n:n+5])
        n += 5
        raw_data = input('Would you like to explore more data? Type \'yes\' or \'no\'.\n')

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
        explore_more_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
