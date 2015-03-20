'''
Anthony Karnati
akarnat1@binghamton.edu
CS110-A55
Lab 12
Chelsea Montgomery

'''

'''
This program finds the population of a city via database query
Output:
  query result (str)
Input:
  city (str)
Classes Used:
  BadArgument
  QueryWorldBD
'''

import sqlite3

# ---------------------------------------------------------------------
'''
User defined exception class (subclass of Exception)
Used to signal program that query should not be issued
'''

class BadArgument(Exception):
  
#-- Constructor --------------------------------------------------------
  
  def __init__(self):
    self.__title = 'Bad Argument'
    self.__message = 'City is blank or contains invalid characters'

#-- Accessors ----------------------------------------------------------
    
  # return title (str)
  def getTitle(self):
    return self.__title
    
#-- to String ----------------------------------------------------------
  
  def __str__(self):
    return self.__message

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------



'''
Encapsulates a  population query sent to world database
'''
class QueryWorldDB:
  
  # Connect to database and get cursor
  # param dbName (str)
  def __init__(self, dBName):
    conn = sqlite3.connect(dBName)
    self.__cursor = conn.cursor()
    # Must make city instance variable so that it is accessible to all methods
    self.__currentCity = ''
    self.__answer = ''

# -- Accessors ---------------------------------------------------------------

  def getAnswer(self):
    return self.__answer

# -- Mutators ----------------------------------------------------------------

  # param cityName (str)
  def setCity(self, cityName):
    self.__currentCity = cityName

  # Note that if city isn't in database, then answer will be None
  # If city is in database, answer will be a tuple object
  # Will have to get element[0] of tuple in order to use it
  def setAnswer(self):
    result = self.__cursor.fetchone()
    self.__answer = '' if result == None else str(result[0]) 
    

  # raises BadArgument Exception if city is blank or contains invalid chars
  def popQuery(self):
    if self.__currentCity.replace('_','A').isalpha():
      self.__cursor.execute('select population from city where name = ?',\
                          (self.__currentCity,))
    else:
      raise BadArgument()


  # Close connection to db
  def closeConnection(self):
    self.__cursor.close()

# -- toString ----------------------------------------------------------------

  # return result (str)
  def __str__(self):
    # Note that 4th format specifier denotes a string rather than an int in 
    # order to accommodate possibility that answer is None
    return '%s %s %s %s\n' % (
      ('The population of' if self.__answer else 'There is no city named'),
      self.__currentCity,
      ('is' if self.__answer else 'in the database'),
      self.__answer )


  
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
 
# Find population of any city stored in world database
# Cities must contain only alphabetic characters with the exeception of mult-
#   word cities, which must be connected with '_' (no spaces allowed)
'''def main():
  # set up connection and create cursor
  query = QueryWorldDB('worldDB')

  # get input from user (priming read)
  city = input("Find the population of a city\nEnter the city name, " + \
               "separate multi-word cities by '_'\n" + \
               "(Press <Enter> to quit):  ")
  
  # let user get as many results as desired
  while city:
    try:
      # set up and issue query
      query.setCity(city.strip())
      query.popQuery()
      query.setAnswer()
      # show results
      print(query)
    except BadArgument as err:
      # city input empty or malformed
      print('\n%s: %s\n' % (err.getTitle(), str(err) ))
       
    # let user enter another city (continuation read)
    city = input("Find the population of a city\nEnter the city name, " + \
                 "separate multi-word cities by '_'\n" + \
                 "(Press <Enter> to quit):  ")
    
  # close connection to db
  query.closeConnection()

main()'''
                           
                            
                    
