queries = ["" for i in range(0, 11)]

### 0. List all airport codes and their cities. Order by the city name in the increasing order. 
### Output column order: airportid, city

queries[0] = """
select airportid, city 
from airports
order by city;
"""

### 1. Write a query to find the names of the customers whose names are at least 15 characters long, and the second letter in the  name is "l".
### Order by name.
queries[1] = """
select 0;
"""


### 2. Write a query to find any customers who flew on their birthday.  Hint: Use "extract" function that operates on the dates. 
### Order output by Customer Name.
### Output columns: all columns from customers
queries[2] = """
select 0;
"""

### 3. Write a query to generate a list: (source_city, source_airport_code, dest_city, dest_airport_code, number_of_flights) for all source-dest pairs with at least 3 flights. 
### Order first by number_of_flights in decreasing order, then source_city in the increasing order, and then dest_city in the increasing order.
### Note: You must generate the source and destination cities along with the airport codes.
queries[3] = """
select 0;
"""

### 4. Find the name of the airline with the maximum number of customers registered as frequent fliers.
### Output only the name of the airline. If multiple answers, order by name.
queries[4] = """
select 0;
"""

### 5. For all flights from OAK to IAD, list the flight id, airline name, and the 
### duration in hours and minutes. So the output will have 4 fields: flightid, airline name,
### hours, minutes. Order by flightid.
queries[5] = """
select 0;
"""

### 6. Write a query to find empty flights (flight, flight date) on any date
###	which someone flew. Assume that if anyone flew on a given date, all
###	flights took off as scheduled, with or without passengers. Order by flight
###	id in increasing order, and then by date in increasing order. 
queries[6] = """
select 0;
"""

### 7. Write a query to generate a list of customers who don't list Southwest as their frequent flier airline, but
### actually flew the most (by number of flights) on that airline.
### Output columns: customerid, customer_name
### Order by: customerid
queries[7] = """
select 0;
"""

# fall17
### 8. Write a query to generate a list of customers where the interval between first and last flight is 5 days.
### Order by the customer name. 
queries[8] = """
select 0;
"""


# fall17
### 9. Name of customer whose max interval between any two consecutive flights is 4 days.
### The output should be simply a list of names
### Order by the customer name. 
queries[9] = """
select 0;
"""

### 10. Write a query that outputs a list: (AirportID, Airport-rank), where we rank the airports 
### by the total number of flights that depart that airport. So the airport with the maximum number
### of flights departing gets rank 1, and so on. If two airports tie, then they should 
### both get the same rank, and the next rank should be skipped.
### Order the output in increasing order by rank, and then airport ID.

queries[10] = """
select 0;
"""

