Jupyter Notebook Database Connection  

-Uses the SQLAlchemy create_engine() function to connect to SQLite database  

-Uses the SQLAlchemy automap_base() function to reflect tables into classes  

-Saves references to the classes named station and measurement  

-Links Python to the database by creating a SQLAlchemy session  

-Closes session at the end of notebook  


Precipitation Analysis  

-Creates a query that finds the most recent date in the dataset (8/23/2017)  

-Creates a query that collects only the date and precipitation for the last year of data without passing the date as a variable  

-Saves the query results to a Pandas DataFrame to create date and precipitation columns  

-Sorts the DataFrame by date  

-Plots the results by using the DataFrame plot method with date as the x and precipitation as the y variables  

-Uses Pandas to print the summary statistics for the precipitation data  


Station Analysis  

-Designs a query that correctly finds the number of stations in the dataset (9)  

-Designs a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281)  

-Designs a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281)  

-Designs a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations  

-Saves the query results to a Pandas DataFrame  

-Correctly plots a histogram with bins=12 for the last year of data using tobs as the column to count  


API SQLite Connection & Landing Page  

-Correctly generates the engine to the correct sqlite file  

-Uses automap_base() and reflect the database schema  

-Correctly saves references to the tables in the sqlite file (measurement and station)  

-Correctly creates and binds the session between the python app and database  

-Displays the available routes on the landing page  


API Static Routes  

-Includes a precipitation route that:  

  &ensp;-Returns json with the date as the key and the value as the precipitation  
	
  &ensp;-Only returns the jsonified precipitation data for the last year in the database  
	
-Includes a stations route that:  

  &ensp;-Returns jsonified data of all of the stations in the database  
	
-Includes a tobs route that:  

  &ensp;-Returns jsonified data for the most active station (USC00519281)  
	
  &ensp;-Only returns the jsonified data for the last year of data  
	

API Dynamic Route  

-Includes a start route that:  

  &ensp;-Accepts the start date as a parameter from the URL  
	
  &ensp;-Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset  
	
-Includes a start/end route that:  

  &ensp;-Accepts the start and end dates as parameters from the URL  
	
  &ensp;-Returns the min, max, and average temperatures calculated from the given start date to the given end date  
	

Coding Conventions and Formatting  

-Places imports at the top of the file, just after any module comments and docstrings, and before module globals and constants  

-Names functions and variables with lowercase characters, with words separated by underscores  

-Follows DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code  

-Uses concise logic and creative engineering where possible
