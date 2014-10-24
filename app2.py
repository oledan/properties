import easygui as eg
import MySQLdb
import db

#We use the easy_gui module for the graphical user interface.
#We use db and MySQLdb for interactions with the MySQL database.

#To facilitate the login process, we created a user class which takes in a name and user id.
#This user object is instantiated once a user has either logged in or signed up.
#This object is called multiple times throughout the app for authentication/identification purposes.
class User:
  #Instantiate the user
  def __init__(self, user_id, fname, lname):
      self.user = user_id
      self.fname = fname
      self.lname = lname
  #User methods to return data
  def name(self):
    return self.fname
  def user_id(self):
    return str(self.user)

#Welcome page for user to either login or sign up
def start():
  global current_user
  msg = "Hello and welcome to the App!"
  title = "Real Estate App"
  choices = ['Sign up', 'Login']
  form = eg.choicebox(msg=msg, title=title, choices=choices)
  if (form == 'Sign up'):
    #Calls the create new user view
    create_user()
  elif (form == 'Login'):
    #Calls the login user view
    login()


#Starts the login process.
def login():
  global current_user
  #Data to be displayed in the window: message, title, login labels and inputs
  msg = "Hello and welcome to the App!"
  title = "Real Estate App"
  fieldNames = ["Email", "Password"]
  fieldValues = []

  #Loop until user is authenticated/until login = 0
  login = 1
  while login == 1:
    form = eg.multpasswordbox(msg,title, fieldNames)
    entered_email = form[0]
    entered_pass = form[1]
    #Uses the get_from_db function that is equivalent to execute
    #This query returns a list of email, password, cust_id, and full name from customer table where the email is the same as the entered email
    user = db.get_from_db("SELECT cust_email, password, cust_id, fname, lname FROM customer WHERE cust_email =" + "'"+str(entered_email)+"'")
    #Get_from_db function returns a list of rows which consist of a single row; inside row are fields from select statement

    #User email and password verification
    if user:
      email = user[0][0];   #User is a list inside of a list of users
      password = user[0][1]
      user_id = user[0][2]
      fname = user[0][3]
      lname = user[0][4]
      if (email == entered_email):
        if (password == entered_pass):
          current_user = User(user_id, fname, lname)
          login = 0
          #If the user has been authenticated, we let them know now via a message:
          msg = "Thank you for logging in, " + current_user.name() + "."+" \n Press ok to get started."
          eg.msgbox(msg)
          menu()
        else:
          #If the user uses the incorrect password, we let them know via a message:
          msg = "Wrong password."
    b = list(user)  #Check to see if the SQl query returns anything that matches specific email/password combination
    #Check to see if credentials match the database
    if (len(b) <= 0): #If there is nothing in the user list, there is no email and password combination in the database
      #If the user inputs an incorrect email and password combination, we let them know via a message:
      msg = "No such email and password combination."


#This view finds the details of a selected property via an ID sent from the property menu
def viewProperty(prop_id):
  #Return all details of one property
  #Query to select fields from one property
  prop = db.get_from_db("SELECT address, city, zipcode, bedrooms, bathrooms, sqft, MINprice, MAXprice  FROM properties WHERE property_id=" + prop_id)

  msg = ""

  fields = ["Address", "City", "Zip", "Beds", "Baths", "Sqft", "Min Price", "Max Price"]

  #Formatting view with fields and values
  i = 0
  for value in prop[0]: #Prop is a list of rows from property table; here we are selecting the first item
    if value:   #Loop through the fields in property to see if it is not null
      msg += fields[i] + ": \t  " + str(value) + " \n"    #Msg is a string that we add fields to (with indentation) if they are not empty
      i = i + 1

  eg.msgbox(msg)

#In the view all properties menu, users are shown a list of all existing properties.
def property_list():
  #Return a list of rows of properties from the databae
  properties = db.get_from_db("SELECT property_id, property_type, address FROM properties") #Users are shown a list of all existing properties
  choices = []  #List of strings that you can click on
  number = len(properties) #Count number of properties
  for row in properties:
    choices.append(str(row[0]) + "\t " + str(row[1]) + "\t" + str(row[2]))  #Append a string of formatted property title to list of choices

  property_list = eg.choicebox(msg='Showing: ' + str(number) +" properties", title=' ', choices=choices) #Sending data to easy gui
  prop_id = property_list.split()[0]
  #Divides all the choices, so that when one is selected it will take you to property_menu
  if (prop_id):
    property_menu(prop_id)

#Helper function for database inserts
def wrap(string):
  if (type(string) is str):
    string = "'"+string+"', "
    return string
  else: return string

#Sign up form for new user
def create_user():
  global current_user
  msg = "Please enter the new account details:"
  error_msg= ''
  title = "Create New User"
  fieldNames = ["First Name:", "Last Name:", "Phone Number:", "Email:", "Password:"]
  fieldValues = []
  form = eg.multenterbox(msg,title, fieldNames, values=fieldValues) #Easy_gui's form

  #Assign form elements to correct fields
  fname = form[0]
  lname = form[1]
  phone_number = form[2]
  cust_email = form[3]
  password = form[4]
  fieldList = [fname, lname, phone_number, password, cust_email]
  fields = "(fname, lname, phone_number, password, cust_email)"

  #Prepare a query to be sent to SQL
  query = "INSERT INTO customer" + fields + "VALUES ("
  values = ''   #Set up blank string that will be appended to query
  for field in fieldList: #Loop through each field and add to values
    values += wrap(field)  #Helper function to format string

  values = values[:-2] #-2 to remove excess )' from string
  query += values + ")" #End query

  db.add_to_db(str(query)) #Send query to database

  #Go back to database once user created to get the new user id
  query = "SELECT cust_id FROM customer where cust_email =" + "'"+str(cust_email)+"'"
  row = db.get_from_db(query)
  user_id = int(row[0][0])  #Selecting first row from list of rows

  current_user = User(user_id,fname,lname) #After the user registers, we instantiate the user object

  #After sign up is completed, we let them know via message:
  msg = "Thank you for logging in, " + current_user.name() + " \n Press ok to get started."
  eg.msgbox(msg)

#Create a new property listing
def add_property():
  global current_user
  msg = "Please enter the following details to add a listing:"
  error_msg = ''
  title = "Add a listing"
  fieldNames = ["Address", "City", "Zip", "Type", "Bedrooms", "Bathrooms", "Area (sqft)", "Lotsize (sqft)", "Min. Price", "Max Price" ]
  fieldValues = []
  form = eg.multenterbox(msg,title, fieldNames, values= fieldValues) #Easy_gui's form

  #Assign form elements to correct fields
  address = form[0]
  city = form[1]
  zipcode = form[2]
  property_type = form[3]
  bedrooms = form[4]
  bathrooms = form[5]
  sqft = form[6]
  lotsize = form[7]
  minprice = form[8]
  maxprice = form[9]
  fieldList = [address,city,zipcode,property_type,bedrooms,bathrooms,sqft, minprice, maxprice]
  fields = "(address, city, zipcode, property_type, bedrooms, bathrooms, sqft, MINprice, MAXprice, user)"

  #Prepare a query to be sent to SQL
  query = "INSERT INTO properties" + fields + " VALUES ("
  values = '' #Set up blank string that will be appended to query

  for field in fieldList:  #Loop through each field and add to values
    values += wrap(field)  #Helper function to format string

  values = values[:-2]  #-2 to remove excess )' from string
  values += ", " + current_user.user_id() +")"

  query += values

  db.add_to_db(str(query))


#In the Manage My Properties tab, users are shown a list of all properties they own.
def dashboard():
  #An inner join is used to display the property address, city, and property type of the..
  #..properties that belong to the current user.
  query = "SELECT b.address, b.city, b.property_type  from properties.customer a inner join properties.properties b on a.cust_id=b.user WHERE a.cust_id =" + current_user.user_id()
  rows = db.get_from_db(query)  #Rows is a list of properties that SQL returns
  msg = ""
  for row in rows: #For loop goes through each property
    address = row[0]
    city = row[1]
    property_type = row[2]
    #Adding fields to view
    msg += "Address: " + str(address) + "\n" + "City: " + str(city) + "\n" + "Type: " + str(property_type) + "\n" + "\n"

  eg.msgbox(msg=msg, title="Your Properties", ok_button="OK")

#The main menu for the interface.
def menu():
  while True:
    #Users can view a property, add a property, manage their properties...
    #...or view existing offers on their properties
    choices = ["View All Properties", "Add A Property", "Manage My Properties", "Existing Offers"]
    menu = eg.choicebox(msg="What do you want to do?", title="Property App:", choices=choices)
    #Choice returns what the user clicks
    choice = menu.split()[0]

    #Provide four choices in main menu
    if (choice == "View"): property_list()
    elif (choice == "Add"): add_property()
    elif (choice == "Manage"): dashboard()
    elif (choice == "Existing"): decide_offer()

#List of all offers on a single property
def offer_history(prop_id):
  #Select bid amount and customer id from offers table for a single property
  query = "SELECT bid, cust_id FROM offers WHERE property_id=" + prop_id
  prop = db.get_from_db(query) #Prop is a list of offers that SQL returns
  msg = "Offer History \n"
  for row in prop:
    #Adding fields to view
    msg += "Bid: " + str(row[0]) + "\t" + "From: Customer #" + str(row[1]) +" \n"

  eg.msgbox(msg)

#Make an offer on a single property
def make_offer(prop_id):
  #Get the details of property
  query = "SELECT address, MINprice, MAXprice FROM properties WHERE property_id =" + str(prop_id)
  prop = db.get_from_db(query)
  address = prop[0][0]
  minprice = prop[0][1]

  msg = "How much would like to offer? (Minimum offer is: $ " + str(minprice) +")" #Add min price to message
  form = eg.enterbox(msg=msg, title="Make An Offer For" + str(address), default='', strip=True) #Add address to title

  insert_offer = ''

  if (form): #If anything is entered to form
    #Add offer to database
    insert_offer = "INSERT INTO offers (property_id, cust_id, bid) VALUES (" + wrap(prop_id) + wrap(current_user.user_id()) + wrap(form)

  insert_offer = insert_offer[:-2] + ")" #-2 to remove excess )'; add ) to end query

  db.add_to_db(insert_offer)

#View existing offers.
def decide_offer():
  #Display the property which the user owns and existing offer on the property via inner join
  #Selecting the property that has an offer that is owned by current customer
  myQ = "SELECT a.address, b.decision, b.amtsold from properties a inner join offers b on a.property_id=b.property_id where b.cust_id =" + current_user.user_id()
  myD = db.get_from_db(myQ)
  decision = myD[0][1] #Get the decision of property from offers table

  if (decision >= 1):
    eg.msgbox(msg="No current offers.")

  elif (decision == 0):
    query = "SELECT a.property_type, a.address, a.MINprice, b.bid, b.amtsold, a.property_id FROM properties a inner join offers b on a.user=" + current_user.user_id()
    prop = db.get_from_db(query)
    property_type = prop[0][0]
    address = prop[0][1]
    minprice = prop[0][2]
    bid = prop[0][3]
    amtsold = prop[0][4]
    prop_id = prop[0][5]
    msg = "Property Type: " + str(property_type) + "\n" + "Address: " + str(address) + "\n" + "Minimum Price: " + str(minprice) + "\n" + "Bid: " + str(bid) + "\n" + "Maximum Bid: " + str(amtsold) + "\n"

    text = "Accept or Reject Existing Offer?"
    choices = ["Accept", "Reject"]
    reply=eg.boolbox(msg, title=text, choices=choices) #Boolbox returns 1 if the first button is chosen. Otherwise returns 0.

    #If offer is accepted
    if (reply == 1):
      eg.msgbox(msg="Offer Accepted")
      acceptoffer = "UPDATE offers set decision=1 where cust_id=" + current_user.user_id()
      db.add_to_db(acceptoffer)
    #If offer is rejected
    if (reply == 0):
      eg.msgbox(msg="Offer Rejected")
      rejectoffer = "UPDATE offers set decision=3 where cust_id=" + current_user.user_id()
      db.add_to_db(rejectoffer)


#Menu for individual properties
def property_menu(prop_id):
  prop = db.get_from_db("SELECT address, city, property_type, MAXprice FROM properties WHERE property_id=" + prop_id)
  msg = str(prop[0][0]) +" "+ str(prop[0][1])
  choices = ["View Full Details", "View Offer History", "Make An Offer"]
  menu = eg.choicebox(msg=msg, title="Property App:", choices=choices)

  if (menu == "View Full Details" ): viewProperty(prop_id)
  if (menu == "View Offer History" ): offer_history(prop_id)
  if (menu == "Make An Offer") : make_offer(prop_id)




#Start login process:
start()
menu()
