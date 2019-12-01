import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
#1
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
    city=input('Would you like to see data for New york, Washington or Chicago?\n').lower()
    while(True):
        if city in ['chicago','washington','new york']:
           break
        else:
           city=input('Enter the city name again\n').lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month=input('Which month all? January, February, March, April, May OR June?\n').lower()
    while(True):
        if month in ['all','january', 'february', 'march', 'april', 'may', 'june']:
           break
        else:
           month=input('Enter the month again.. all, January, February, March, April, May or June?\n').lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day=input('Which day?\n').lower()
    while(True):
        if day in ['all','sunday','monday','tuesdat','wednesday','thursday','friday','saturday']:
           break
        else:
           day=input('Enter the day again.. Type your response as an integer (e.g. Sun=1)?\n').lower()


    print('-'*40)
    return city, month, day

#2
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
    if city[0]=='n':
        city="new_york_city"
    filename=city+'.csv'
    df=pd.read_csv(filename)

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

    print('\n------------------HEAD OF TABLE----------------------')
    print(df.head())
    print('\n------------------TAIL OF TABLE----------------------')
    print(df.tail())
    return df

#3
def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if( month == 'all'):
        mostCommonMonth=df['Start Time'].dt.month.mode()[0]
        print('Most common month: '+str(mostCommonMonth))
    # TO DO: display the most common day of week
    if(day=='all'):
        mostCommonDay=df['Start Time'].dt.day.mode()[0]
        print('Most common Day: '+str(mostCommonDay))
    # TO DO: display the most common start hour
    mostCommonHour=df['Start Time'].dt.hour.mode()[0]
    print('Most common hour: '+str(mostCommonHour))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#4
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    #to calculate total time of method calculations
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_used_start_SStation=df["Start Station"].mode()[0]
    print('\nMost common start station is: ',most_used_start_SStation)

    # TO DO: display most commonly used end station
    most_used_end_SStation=df["End Station"].mode()[0]
    print('\nMost common end station is: ',most_used_end_SStation)

    # TO DO: display most frequent combination of start station and end station trip
    combination=df['Start Station'].astype(str) + " to " + df['End Station'].astype(str)
    freq_combination=combination.mode()[0]
    print('\nMost frequent combination of start station and end station trip: ',freq_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#5
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel=df['Trip Duration'].sum()
    day=total_travel // (24*3600)
    total_time=total_travel % (24*3600)
    hour=total_time // 3600
    total_time %= 3600
    mintues=total_time//60
    total_time %= 60
    seconds=total_time
    print('\ntotal travel time: ',day,' days',hour,' ,hours',mintues,' ,mintues',seconds,' ,seconds')

    # TO DO: display mean travel time
    total_travel_mean=df['Trip Duration'].mean()
    dayM=total_travel_mean // (24*3600)
    total_time_mean=total_travel_mean % (24*3600)
    hourM=total_time_mean // 3600
    total_time_mean %= 3600
    mintuesM=total_time_mean//60
    total_time_mean %= 60
    secondsM=total_time_mean
    print('\ntotal travel time: ',dayM,' days',hourM,' ,hours',mintuesM,' ,mintues',secondsM,' ,seconds')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

#6
def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count1=df['User Type'].str.count('Subscriber').sum()
    print('\nCount of Subscribers: ',user_type_count1)
    user_type_count2=df['User Type'].str.count('Customer').sum()
    print('\nCount of Customers: ',user_type_count2)

    # TO DO: Display counts of gender
    if( 'Gender' in df.columns):
       male_count=df['Gender'].str.count('Male').sum()
       print('\nCount of Males: ',male_count)
       female_count=df['Gender'].str.count('Female').sum()
       print('\nCount of Females: ',female_count)


    # TO DO: Display earliest, most recent, and most common year of birth
    if('Birth Year' in df):
       earliest=df['Birth Year'].min()
       print('\nEarliest year of birht: ',earliest)
       recent=df['Birth Year'].max()
       print('\nrecent year of birth: ',recent)
       freq=df['Birth Year'].mode()[0]
       print('\nMost common year of birth: ',freq)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        rowsDisplay = input('\nWould you like to see five rows of data? Enter yes or no.\n')
        if rowsDisplay.lower() == 'yes':
            counter=0
            while(True):
                counter=counter+10000000
                print(df.head(counter))
                rowsDisplay2 = input('\nWould you like to see more five rows of data? Enter yes or no.\n')
                if rowsDisplay2.lower() != 'yes':
                   break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
