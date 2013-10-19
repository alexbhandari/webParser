import mysql.connector
from mysql.connector import errorcode
from abc import ABCMeta, abstractmethod

class connector(object):
    
    _config = {
      'user': 'vda8888',
      'password': '123456',
      'host': '127.0.0.1',
      'database': 'test',
      'raise_on_warnings': True,
    }
    
    def __init__(self):
        self.cnx = None
        
    def initConnection(self):
        try:
            self.cnx = mysql.connector.connect(**connector._config) 
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exists")
            else:
                print(err)
    def commit(self):
        self.cnx.commit()

    def get_cursor(self):
        return self.cnx.cursor()

    def closeConnection(self):
        self.cnx.close()


class table(metaclass=ABCMeta):
    
    def __init__(self, connector):
        self._connector = connector
        self._cursor = self._connector.get_cursor()
        self.name = None
        self.column_names = []
        
    def get_cursor(self):
        return self._cursor

    def destroy(self):
        if (self._cursor is not None):
            self._cursor.close()
            
    def view_full_table(self):
        query = ("SELECT * FROM %s")
        self._cursor.execute(query % (self.name,))
           
    #This method must NOT be overridden        
    def insert_row(self, inserted_dict):
        addCommand = "INSERT INTO " + self.name + " ("
        field_count = 0
        field_index = 0
        
        end = ""
        
        #Add column names
        while (field_index < len(self.column_names)):
            current_value = inserted_dict.get(self.column_names[field_index])
            if (current_value is not None):
                field_count += 1
                if (field_count != 1):
                    addCommand += ", "
                    end += ", "
                addCommand += self.column_names[field_index]
                end += self.insert_row_add_expression(field_index, current_value)
                
            field_index += 1
        addCommand += ") VALUES ("
        addCommand += end + ")"
        
        print (addCommand)
        self.get_cursor().execute(addCommand)
        self._connector.commit()
    
    #This method must NOT be overridden
    def find_row(self, key_dictionary):
        query = "SELECT * FROM " + self.name
        field_count = 0 #Always start with 1 since 0 is assumed to be 0
        field_index = 0
        
        while (field_index < len(self.column_names)):
            current_value = key_dictionary.get(str(self.column_names[field_index]))
            if (current_value is not None):
                field_count += 1
                if (field_count == 1):
                    query += " WHERE "
                else:
                    query += " AND "
                query += self.column_names[field_index] + " "
                print (field_index)
                query += self.find_row_add_expression(field_index, current_value)
                
            field_index += 1
        print (query)
        self._cursor.execute(query)
    
    def delete_row(self, delete_dict):
        query = "DELETE FROM " + self.name
        field_count = 0 #Always start with 1 since 0 is assumed to be 0
        field_index = 0
        
        while (field_index < len(self.column_names)):
            current_value = delete_dict.get(str(self.column_names[field_index]))
            if (current_value is not None):
                field_count += 1
                if (field_count == 1):
                    query += " WHERE "
                else:
                    query += " AND "
                query += self.column_names[field_index] + " "
                print (field_index)
                query += self.find_row_add_expression(field_index, current_value)
                
            field_index += 1
        print (query)
        self._cursor.execute(query)
        self._connector.commit()
    
    @abstractmethod
    def find_row_add_expression(self, column_index, value):
        pass
    
    @abstractmethod
    def insert_row_add_expression(self, column_index, value):
        pass
    
class words_table(table):
    def __init__(self, connector): #Pass in a _connector to database
        super().__init__(connector)
        self.name = "words"
        self.column_names = ["id", "name", "pos", "definition", "context", "rating", "french_name", "french_definition", "french_context"]
        
    def find_row_add_expression(self, column_index, value):
        if (column_index == 0):
            return "= " + str(value)
        elif (column_index == 1):  # name
            return "REGEXP " + "'" + value + "'" 
        elif (column_index == 2):  # pos
            return "REGEXP " + "'" + value + "'"
        elif (column_index == 3):  # definition
            return "REGEXP " + "'" + value + "'"
        elif (column_index == 4):  # context
            return "REGEXP " + "'" + value + "'"
        elif (column_index == 5):  # rating
            return "= " + str(value)
        elif (column_index == 6):  # french_name
            return "REGEXP " + "'" + value + "'"
        elif (column_index == 7):  # french_definition
            return "REGEXP " + "'" + value + "'"
        elif (column_index == 8):  # french_context
            return "REGEXP " + "'" + value + "'"       
    
    def insert_row_add_expression(self, column_index, value):
        if (column_index == 0):
            return str(value)
        elif (column_index == 1):  # name
            return "'" + value + "'" 
        elif (column_index == 2):  # pos
            return "'" + value + "'"
        elif (column_index == 3):  # definition
            return "'" + value + "'"
        elif (column_index == 4):  # context
            return "'" + value + "'"
        elif (column_index == 5):  # rating
            return str(value)
        elif (column_index == 6):  # french_name
            return "'" + value + "'"
        elif (column_index == 7):  # french_definition
            return "'" + value + "'"
        elif (column_index == 8):  # french_context
            return "'" + value + "'"   
    
#Always start with the following two lines
connector = connector()
connector.initConnection()
 
table = words_table(connector)

key = {}
key["name"] = "dog"
key["pos"] = "animal"

table.view_full_table()
table.find_row(key)
table.view_full_table()
#table.insert_row(key)

#Once a query is done, results are stored in get_cursor(). We MUST read the results before moving on
for (result) in table.get_cursor():
    print (result)

#table.delete_row(key)
for (result) in table.get_cursor():
    print (result)

 
#Once finish using a table, MUST destroy it
table.destroy()

#Always end with this line
connector.closeConnection()
