import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington' ]
MONTHS = ['all','january', 'february', 'march', 'april', 'may', 'june']
DAYS = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!\n I\'m Nabila and here to help you...')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Which city you want to overview? You can choose between chicago, new york city, washington \n>").lower()
        if city in CITIES:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input("Which month you want to overview? You can choose between all, january, february, march, april, may, june \n>").lower()
        if month in MONTHS:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Which day you want to overview? You can choose between all, monday, tuesday, wednesday, thursday, friday, saturday, sunday \n>").lower()
        if day in DAYS:
            break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):

    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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


    print('\nPlease wait while I\'m calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month is: ", common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("The most common day of week is: ", common_day)

    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print("The most common start hour is: ", common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):


    print('\nPlease wait while I\'m calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print("The most commonly used start station: ", common_start_station)

    # TO DO: display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print("The most commonly used end station: ", common_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    combos = df['Start To End'].mode()[0]

    print("\nThe most frequent combination of trips are from ", combos)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):


    print('\nPlease wait while I\'m calculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    #duration in minutes and seconds
    minute, second = divmod(total_travel_time, 60)
    #duration in hour and minutes
    hour, minute = divmod(minute, 60)
    print("The total trip duration is:\n")
    print('hours: {} \n minutes: {} \n seconds: {} '.format(hour, minutes, seconds))

    # TO DO: display mean travel time
    average_travel_time = round(df['Trip Duration'].mean())
    #average duration in min and sec
    mins, sec = divmod(average_travel_time, 60)
    #prints the time in hours, mins, sec
    if mins > 60:
        hrs, mins = divmod(mins, 60)
        print("\nThe average trip duration is \n")
        print("hours: ", hrs)
        print("minutes: ", mins)
        print("seconds: ", sec)
    else:
        print("\nThe average trip duration is \n ")
        print("minutes: ", mins)
        print("seconds: ", sec)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    print('\nPlease wait while I\'m calculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()

    print("Here are the numbers of users (both type):\n", user_type)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print("\nYou can see the types of users by gender below:\n", gender)
    except:
        print("\nThere is no 'Gender' column in this file.")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = int(df['Birth Year'].min())
        recent = int(df['Birth Year'].max())
        common_year = int(df['Birth Year'].mode()[0])
        print('\nThe earliest year of birth: {}'.format(earliest))
        print('\nThe most recent year of birth: {}'.format(recent))
        print('\nThe most common year of birth: {}'.format(common_year))
    except:
        print("There are no birth year details in this file.")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print("Hey thanks for your patience!\n")

def display_raw_data(df):
    option = input('Would you like to read some of the raw data? Enter Yes/No \n').lower()

    if option == 'yes'or option =='y':
        option = True
    elif option =='no' or option =='n':
        option = False
    else:
        print('You did not enter a valid choice. Please try that again. ')
        display_raw_data(df)
        return

    raw_data = 0

    while True:
        for i in range(raw_data ,raw_data+5):
            raw_data += 5
            print(df.iloc[raw_data : raw_data + 5])
            print()
        again = input('Would you like to see five more? Enter Yes/No ').lower()
        if again == 'yes' or again == 'y':
            continue
        elif again == 'no' or again == 'n':
            break
        else:
            print('You did not enter a valid choice.')
            return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart and find out more? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
