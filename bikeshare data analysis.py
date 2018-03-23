# -*- coding: utf-8 -*-
"""
Created on Mon Mar 05 19:27:20 2018

@author: Ankit Goyal
"""

#Arguments are input from the user during execution, hence no arguments are required in some of functions below
## Filenames
import datetime
import pandas as pd
import datetime as dt
import timeit
import calendar

chicago = 'chicago.csv'
new_york_city = 'new_york_city.csv'
washington = 'washington.csv'
def helper(city):
  f=open(city,'r')
  df=pd.read_csv(f)
  return df

'''
#Asks the user for a city and returns the filename for that city's bike share data.

   # Args:
  #      none.
 #   Returns:
#        (str) Filename for a city's bikeshare data.

'''

def get_city():
    while True:
        try:
            city =input('\nHello! Let\'s explore some US bikeshare data!\n'
                 'Would you like to see data for Chicago, New York City, or Washington?\n')
        except EOFError:
            return
        City=city.lower()
        if City.find(' '):
            City=City.replace(" ","_",City.find(' ')-1)
        else:
            City=City
        return City+'.csv'


def get_time_period():
    '''Asks the user for a time period and returns the specified filter.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    time_period =input('\nWould you like to filter the data by month, day, or not at'
                        ' all? Type "none" for no time filter.\n')
    inputs=['day','month','none']
    while time_period.lower() not in inputs:
         time_period=input('enter the correct input! Enter either day, month or none for no filter.\n')
    # TODO: handle raw input and complete function
    if time_period.lower()=='month' or time_period.lower()=='day':
      time_period=time_period.lower()
    elif time_period.lower()=='none':
      time_period=time_period.lower()
    return(time_period)



def get_month():
    '''Asks the user for a month and returns the specified month.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    months=['january','february','march','april','may','june']
    month =input('\nWhich month? January, February, March, April, May, or June?\n')
    month=month.lower()
    while month not in months:
         month=input('Enter the correct entry, Choose either January, February, March, April, May, June.\n')
    if month in months:
      month=month
    return(month)
  
def get_day():
    '''Asks the user for a day and returns the specified day.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    day = input('\nWhich day? Please type your response as an integer.\n')
    a=range(0,7)
    a=list(map(str,a))
    while day not in a:
      print('invalid input')
      day=input('\nEnter the correct value.\n')
    if day in a:
       return(int(day))
       
            
def popular_month(city,time_period):
    df=helper(city)
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular month for start time?
    '''
    # TODO: complete function
    if time_period=='none':
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['Start Time']=df['Start Time'].dt.month
        month_data=((df.groupby('Start Time')['Start Time'].value_counts()))
        popular_month=month_data.argmax()[1]
        if popular_month==6:
            popular_month='June'
        elif popular_month==5:
            popular_month='May'
        elif popular_month==4:
            popular_month='April'
        elif popular_month==3:
            popular_month='March'
        elif popular_month==2:
            popular_month='February'
        else:
            popular_month='January'
        return('The popular month for this city is'+' '+popular_month)
    else:()

def popular_day(city,time_period,month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    '''
    # TODO: complete function
    df=helper(city)
    '''
    filtering data by user input
    '''
    if time_period=='month':
        index=datetime.datetime.strptime(month,'%B').month
#getting month index
        df=df[pd.DatetimeIndex(df['Start Time']).month==index]
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['Start Time']=df['Start Time'].dt.dayofweek
#extracting day of week from the date and filling it in Start Time column
        day_data=((df.groupby('Start Time')['Start Time'].value_counts()))
        popular_day=day_data.argmax()[1]
        popular_day=calendar.day_name[popular_day]
    else:
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['Start Time']=df['Start Time'].dt.dayofweek
        day_data=((df.groupby('Start Time')['Start Time'].value_counts()))
        popular_day=day_data.argmax()[1]
        popular_day=calendar.day_name[popular_day]
    return(popular_day)


def popular_hour(city,time_period,days,month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular hour of day for start time?
    '''
    df=helper(city)
#script subests data based on day input by the user
    if time_period=='day':
        days=int(days)
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['index']=df['Start Time'].dt.dayofweek
        df=df[df['index']==days]
        df['Start Time']=df['Start Time'].dt.hour
        time_data=((df.groupby('Start Time')['Start Time'].value_counts()))
        popular_time=time_data.argmax()[1] 
#Script subsets data based on the month input by the user
    elif time_period=='month':
        index=datetime.datetime.strptime(month,'%B').month
        df=df[pd.DatetimeIndex(df['Start Time']).month==index]
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['Start Time']=df['Start Time'].dt.hour
        time_data=((df.groupby('Start Time')['Start Time'].value_counts()))
        popular_time=time_data.argmax()[1]
    else:
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['Start Time']=df['Start Time'].dt.hour
        time_data=((df.groupby('Start Time')['Start Time'].value_counts()))
        popular_time=time_data.argmax()[1]
    return(popular_time)
    
def trip_duration(city,time_period,days,month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the total trip duration and average trip duration?
    '''
    df=helper(city)
    # TODO: complete function
#filters based on day of week
    if time_period=='day':
        days=int(days)
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['index']=df['Start Time'].dt.dayofweek
        df=df[df['index']==days]
        duration=df['Trip Duration'].sum()
        duration_avg=df['Trip Duration'].mean()
        duration=str(datetime.timedelta(seconds=int(duration)))
        duration_avg=str(datetime.timedelta(seconds=int(duration_avg)))
#filters based on month
    elif time_period=='month':
        index=datetime.datetime.strptime(month,'%B').month
        df=df[pd.DatetimeIndex(df['Start Time']).month==index]
        duration=df['Trip Duration'].sum()
        duration_avg=df['Trip Duration'].mean()
        duration=str(datetime.timedelta(seconds=int(duration)))
        duration_avg=str(datetime.timedelta(seconds=int(duration_avg)))
    else:
        duration=df['Trip Duration'].sum()
        duration_avg=df['Trip Duration'].mean()
        duration=str(datetime.timedelta(seconds=int(duration)))
        duration_avg=str(datetime.timedelta(seconds=int(duration_avg)))
#returns a series of trip durations and average of duration for a filter)
    return('total trip duration in days:hr:mins:seconds '+ (duration)+'and average duration in hours:mins:seconds '+str(duration_avg))

def popular_stations(city,time_period,days,month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular start station and most popular end station?
    '''
    df=helper(city)
    # TODO: complete function
    if time_period=='day':
        days=int(days)
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['index']=df['Start Time'].dt.dayofweek
        df=df[df['index']==days]
        grouped=((df.groupby('Start Station')['Start Station'].value_counts()))
        grouped2=((df.groupby('End Station')['End Station'].value_counts()))
        popular=grouped.argmax()[1]
        popular_end=grouped2.argmax()[1]
    elif time_period=='month':
        index=datetime.datetime.strptime(month,'%B').month
        df=df[pd.DatetimeIndex(df['Start Time']).month==index]
        grouped=((df.groupby('Start Station')['Start Station'].value_counts()))
        grouped2=((df.groupby('End Station')['End Station'].value_counts()))
        popular=grouped.argmax()[1]
        popular_end=grouped2.argmax()[1]
    else:
        grouped=(df.groupby('Start Station')['Start Station'].value_counts())
        grouped2=((df.groupby('End Station')['End Station'].value_counts()))
        popular=grouped.argmax()[1]
        popular_end=grouped2.argmax()[1]
    return('start station'+' '+popular,'End station is'+' '+popular_end)
    

def popular_trip(city,time_period,days,month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What is the most popular trip?
    '''
    df=helper(city)
    # TODO: complete function
#filters most popular trip by day
    if time_period=='day':
        days=int(days)
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['index']=df['Start Time'].dt.dayofweek
        df=df[df['index']==days]
        df['Trip']=df['Start Station']+' TO '+df['End Station']
        grouped=((df.groupby('Trip')['Trip'].value_counts()))
        popular=grouped.argmax()[1]
#filters most popular trip by month
    elif time_period=='month':
        index=datetime.datetime.strptime(month,'%B').month
        df=df[pd.DatetimeIndex(df['Start Time']).month==index]
        df['Trip']=df['Start Station']+' TO '+df['End Station']
        grouped=((df.groupby('Trip')['Trip'].value_counts()))
        popular=grouped.argmax()[1]
    else:
        df['Trip']=df['Start Station']+' TO '+df['End Station']
        grouped=((df.groupby('Trip')['Trip'].value_counts()))
        popular=grouped.argmax()[1]
    return('most popular trip:'+' '+popular)
    


def users(city,time_period,days,month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of each user type?
    '''
    df=helper(city)
    # TODO: complete function
#filters most popular trip by day
    if time_period=='day':
        days=int(days)
        df['Start Time']=pd.to_datetime(df['Start Time'])
        df['index']=df['Start Time'].dt.dayofweek
        df=df[df['index']==days]
        grouped=((df.groupby('User Type')['User Type'].count()))
#filters most popular trip by month
    elif time_period=='month':
        index=datetime.datetime.strptime(month,'%B').month
        df=df[pd.DatetimeIndex(df['Start Time']).month==index]
        grouped=((df.groupby('User Type')['User Type'].count()))
    else:
        grouped=((df.groupby('User Type')['User Type'].count()))
    return('Different types of users are as follows:'+' '+str(grouped))

def gender(city,time_period,days,month):
    '''TODO: fill out docstring with description, arguments, and return values.
    Question: What are the counts of gender?
    '''
    df=helper(city)
    df=df.dropna()
    # TODO: complete function
    if city=='washington.csv':
        print('Gender Data is not available')
    else:
    #filters most popular gender by day
        if time_period=='day':
            days=int(days)
            df['Start Time']=pd.to_datetime(df['Start Time'])
            df['index']=df['Start Time'].dt.dayofweek
            df=df[df['index']==days]
            grouped=((df.groupby('Gender')['Gender'].value_counts()))
            popular=grouped
    #filters most popular trip by month
        elif time_period=='month':
            index=datetime.datetime.strptime(month,'%B').month
            df=df[pd.DatetimeIndex(df['Start Time']).month==index]
            grouped=((df.groupby('Gender')['Gender'].value_counts()))
            popular=grouped
        else:
            grouped=((df.groupby('Gender')['Gender'].value_counts()))
            popular=grouped
        return(popular)


def birth_years(city,time_period,days,month):
    df=helper(city)
    df=df.dropna()
    if city=='washington.csv':
        print('Birth year Data is not available')
    else:
 
    #filters most popular trip by day
        if time_period=='day':
            days=int(days)
            df['Start Time']=pd.to_datetime(df['Start Time'])
            df['index']=df['Start Time'].dt.dayofweek
            df=df[df['index']==days]
            grouped=((df.groupby('Birth Year')))
            popular_year=grouped['Birth Year'].value_counts()
            popular_year=int(popular_year.argmax()[1])
            oldest=int(min(df['Birth Year']))
            youngest=int(max(df['Birth Year']))
    #filters most popular trip by month
        elif time_period=='month':
            index=datetime.datetime.strptime(month,'%B').month
            df=df[pd.DatetimeIndex(df['Start Time']).month==index]
            grouped=((df.groupby('Birth Year')))
            popular_year=grouped['Birth Year'].value_counts()
            popular_year=int(popular_year.argmax()[1])
            oldest=int(min(df['Birth Year']))
            youngest=int(max(df['Birth Year']))
        else:
            grouped=((df.groupby('Birth Year')))
            popular_year=grouped['Birth Year'].value_counts()
            popular_year=int(popular_year.argmax()[1])
            oldest=int(min(df['Birth Year']))
            youngest=int(max(df['Birth Year']))
        return('Most popular year is'+' '+str(popular_year)
        +' '+'Oldest  user was born in'+' '+str(oldest)
        +' '+'Youngest user was born in'+' '+str(youngest))
        
def display_data(city):
    df=helper(city)
    display =input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    if display.lower()=='yes':              
        n=5
        trip_data=df.head(n)
        print(trip_data)
        while True:
            display =input('\nWould you like to view more individual trip data?'
                        'Type \'yes\' or \'stop\'.\n')
            if display=='yes':
                print(df[n:n+5])
                n+=5
            else:
                break
    else:
        print ('you entered no or did not enter correct input')
    return


def statistics():
    '''Calculates and prints out the descriptive statistics about a city and time period
    specified by the user via raw input.

    Args:
        none.
    Returns:
        none.
    '''
    city=get_city()
    time_period=get_time_period()
    days=0
    month=0
    if time_period=='day':
        days=get_day()
    elif time_period=='month':
        month=get_month()
    else:()
    print('Calculating the first statistic...')
    # What is the most popular month for start time?
    if time_period == 'none':
        start_time = timeit.default_timer()
        print(popular_month(city,time_period))
        elapsed = timeit.default_timer() - start_time
        #TODO: call popular_month function and print the results
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
    if time_period=='none' or time_period=='month':
        start_time = timeit.default_timer()
        print(popular_day(city,time_period,month))
        elapsed = timeit.default_timer() - start_time
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
    # What is the most popular day of week (Monday, Tuesday, etc.) for start time?
    #Popular_day functions has filters months, days
    if time_period == 'none' or time_period == 'month'or time_period=='day':
        # What is the most popular hour of day for start time?
        # TODO: call popular_hour function and print the results
        #Popular hour functions  has filters days and months'
        start_time = timeit.default_timer()
        print(popular_hour(city,time_period,days,month))
        elapsed = timeit.default_timer() - start_time
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
        # What is the total trip duration and average trip duration?
        # TODO: call trip_duration function and print the results
        #trip duration function is filtered by days and months
        start_time = timeit.default_timer()
        print(trip_duration(city,time_period,days,month))
        elapsed = timeit.default_timer() - start_time
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
        # What is the most popular start station and most popular end station?
        # TODO: call popular_stations function and print the results
        start_time = timeit.default_timer()
        print(popular_stations(city,time_period,days,month))
        elapsed = timeit.default_timer() - start_time
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
    # What is the most popular trip?
    # TODO: call popular_trip function and print the results
        start_time = timeit.default_timer()
        print(popular_trip(city,time_period,days,month))
        elapsed = timeit.default_timer() - start_time
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
    # What are the counts of each user type?
    # TODO: call users function and print the results
        start_time = timeit.default_timer()
        print(users(city,time_period,days,month))
        elapsed = timeit.default_timer() - start_time
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
    # What are the counts of gender?
    # TODO: call gender function and print the results
        start_time = timeit.default_timer()
        print(gender(city,time_period,days,month))
        elapsed = timeit.default_timer() - start_time
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
    # What are the earliest (i.e. oldest user), most recent (i.e. youngest user), and
    # most popular birth years?
        start_time = timeit.default_timer()
        print(birth_years(city,time_period,days,month))
        elapsed = timeit.default_timer() - start_time
        print("That took %s seconds." % elapsed)
        print("Calculating the next statistic...")
    # Display five lines of data at a time if user specifies that they would like to
    display_data(city)
    # Restart?
    restart =input('\nWould you like to restart? Type \'yes\' or \'no\'.\n')
    if restart.lower() == 'yes':
        statistics()    
if __name__ == "__main__":
	statistics()