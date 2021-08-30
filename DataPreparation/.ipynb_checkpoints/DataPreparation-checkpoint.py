import pandas as pd
import psycopg2


def queryreturn(query):
    con = psycopg2.connect(database="mid_term_project", user="lhl_student", password="lhl_student", host="mid-term-project.ca2jkepgjpne.us-east-2.rds.amazonaws.com", port="5432")
    cur = con.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    df = pd.DataFrame(rows)
    con.close()
    return df

query = 'SELECT * FROM passengers ORDER BY RANDOM() LIMIT 700000'

passengers = queryreturn(query)


query = 'SELECT * FROM flights ORDER BY RANDOM() LIMIT 700000'

flights = queryreturn(query)


query = 'SELECT * FROM fuel_comsumption LIMIT 700000'

fuel_consumption = queryreturn(query)


query = 'SELECT * FROM flights_test LIMIT 700000'


flights_test = queryreturn(query)

# Organizing test data and cleaning it up

flights_test = flights_test[flights_test['fl_date']<= '2020-01-07']


# Getting column names using smaller csv files


flightscolumns = pd.read_csv('Columns/FlightsColumns.csv')

flights.columns = flightscolumns.columns.tolist()


passengerscolumns = pd.read_csv('Columns/PassengersColumns.csv')

passengers.columns = passengerscolumns.columns.tolist()


fuel_consumptioncolumns = pd.read_csv('FCColumns.csv')

fuel_consumption.columns = fuel_consumptioncolumns.columns.tolist()


flights_testcolumns = pd.read_csv('Columns/Flights_testColumns.csv')

flights_test.columns = flights_testcolumns.columns.tolist()



pd.DataFrame.to_csv(flights,'flights.csv')




pd.DataFrame.to_csv(passengers,'passengers.csv')




pd.DataFrame.to_csv(fuel_consumption,'fuel_consumption.csv')


pd.DataFrame.to_csv(flights_test,'flights_test.csv')