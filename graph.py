import matplotlib.pyplot as plt

years = [2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017, 2018, 2019, 2020, 2021, 2022,2023,2024]
young_unemployment = [48.1,42.3,40.4,34.4,30.6,43.5,38.4,29.5,29.9,31.7,29.7,34.1,31.1,25.5,25.1,23.0,35.5,26.3,20.1,16.6,16.6]
middle_unemployment = [70.6,55.8,49.1,41.8,37.2,59.6,48.0,40.6,38.8,39.0,37.0,35.8,40.4,40.4,35.8,37.4,72.0,62.8,52.0,37.6,36.6]
old_unemployment = [120.5,99.5,81.6,69.0,60.2,89.5,70.7,56.5,55.5,60.3,60.9,59.4,61.5,57.8,51.3,55.9,120.1,111.2,91.0,58.6,60.6]


plt.figure(figsize=(10, 5))

plt.plot(years, young_unemployment, color='blue', label='15-24')
plt.plot(years, middle_unemployment, color='orange', label='25-39')
plt.plot(years, old_unemployment, color='gray', label='40 and above')

plt.title('Total number of unemployed persons of each age group')
plt.xlabel('Year')
plt.ylabel("Total number of unemployed persons ('000)")

plt.grid()

plt.xticks(years, rotation=45)  

plt.legend()

plt.tight_layout() 
plt.show()
