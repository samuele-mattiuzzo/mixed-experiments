import pandas as pd

df = pd.read_csv("Automobile_data.csv",
                 na_values={
                    'price':["?","n.a", "NaN"],
                    'stroke':["?","n.a"],
                    'horsepower':["?","n.a"],
                    'peak-rpm':["?","n.a"],
                    'average-mileage':["?","n.a"]
                })
print(df [['company','price']][df.price==df['price'].max()])

car_Manufacturers = df.groupby('company')

print(car_Manufacturers[['company','average-mileage']].mean('average-mileage'))
print(df['company'].value_counts())
print(car_Manufacturers.get_group('toyota'))

df = df.sort_values(by=['price', 'horsepower'], ascending=False)
print(df.head(10))

Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925 , 71400]}
CarPriceDf = pd.DataFrame.from_dict(Car_Price)
Car_HP = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Horsepower': [141, 80, 182 , 160]}
CarsHorsepowerDf = pd.DataFrame.from_dict(Car_HP)
carsDf = pd.merge(CarPriceDf, CarsHorsepowerDf, on="Company")
print(carsDf)

GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925 , 71400]}
carsDf1 = pd.DataFrame.from_dict(GermanCars)
JapaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500 , 58900]}
carsDf2 = pd.DataFrame.from_dict(JapaneseCars)
carsDf = pd.concat([carsDf1, carsDf2], keys=["Germany", "Japan"])
print(carsDf)
