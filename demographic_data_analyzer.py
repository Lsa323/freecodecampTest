import pandas as pd
#importation of the dataframe
df=pd.read_csv('dataset')
#how many people of each race are presented in this dataset
def racePerPeople(df) -> Series:
    return df['race'].value_count()
def averageOfmen(df)-> float:
    return df[df['gender'] =='male']['age'].mean()
def percentageBachelor(df)-> float:
    studiesMendatory=['Bachelors', 'Masters', 'Doctorate']
    #create a dataframe
    educationdf=df[df['education'].isin(studiesMendatory)]
    income = educationdf[educationdf['salary'] == '>50K']
    return (len(income)/len(educationdf))*100
def minHour(df) -> int:
    return df['hours-per-week'].min()
def minHourPerWeek(df)-> float:
    valmin = df['hours-per-week'].min()
    nbreHourperweekdf = df[df['hours-per-week']==valmin]
    nHp = (nbreHourperweekdf['salary'] == '>50K').sum()
    return (nHp/len(nbreHourperweekdf))*100
def countryHighPercentage(df):
    nbCountries = df['native-country'].value_counts()
    highSalary = df[df['salary']=='>50K']['native-country'].value_counts()
    perc = (highSalary/nbCountries)*100
    return perc.idxmax(), perc.max()
def mostPopOccupation():
    mdf = df[(df['native-country']=='India') and (df['salary']=='>50K')]
    return mdf['occupation'].value_counts().idxmax()