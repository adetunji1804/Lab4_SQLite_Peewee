import sqlite3

# function to add record
def add_record(name, country, number):
    name = input('Enter name: ')
    country = input('Enter country: ')
    number = int(input('Enter number of Catches: '))
    #return name, country, number
    conn.execute('insert into chainsaw_tbl values(?, ?, ?)',(name, country, number))
    conn.commit()


#function to update record
def update_record(name, number):
    name = input('Enter name for record to update: ')
    number = int(input('Update number of catches: '))
    conn.execute('UPDATE chainsaw_tbl SET number = ? WHERE name = ?',(number, name))
    conn.commit()

#Function search on name
def search_record(name):
    name = input('Enter name to fetch record: ')
    searched_result = conn.execute('SELECT rowid, * From chainsaw_tbl WHERE name = ?',(name, ))
    return searched_result

# function to delete record
def delete_record(name):
    cur = conn.cursor()
    name = input('Enter name to delete record: ')
    cur.execute('DELETE From chainsaw_tbl WHERE name = ?',(name, ))
    conn.commit()
    return cur.rowcount
    
if __name__ == "__main__":
    
    #instruction guide
    print(' APP INSTRUCTION GUIDE\n----------------------------')
    print('Enter letter \'A\' to add data\nEnter letter \'S\' to search record by name\nEnter letter \'U\' to add data')
    print('Enter letter \'D\' to delete record by name\nEnter letter \'E\' to exit application\n----------------------------\n')

    while True:
        # create or open connection to the db file
        conn = sqlite3.connect('chainsaw_db.sqlite')

        # table created if not existed in database
        conn.execute('create table if not exists chainsaw_tbl(Name text, Country text, Number integer)')

        valid_choice = ['A', 'D', 'S', 'U', 'E'] # operation symbol
        print('\n') #line to demacate each operation

        operation_sign = input('Signify operation process: ') # prompt user for operation type
        choice = operation_sign.upper() # convert user input to cap

        try:
            # identify operation symbol
            if choice == 'A': 
                add_record("name","country", 2) # add data to database

            elif choice == 'U':
                update_record("name", number=2) # update data

            elif choice == 'S':
                for result in search_record("name"): # retrieve data when found
                    print(f'{result}')

            elif choice == 'D':
                deleted_record = delete_record("name") # delete record
                print(f'Number of record/s deleted: {deleted_record}')
            
            elif choice == 'E': # Exit application
                raise SystemExit(f'application terminated.......bye!')

            else:
                print('Invalid operation sign!') # message displayed when operation sign is not on list
        except sqlite3.Error as err: # handle database error
            print(f'Error! Operation aborted. {err}')
        finally:
            conn.close()