from peewee import *


db = SqliteDatabase('chainsaw_orm_db.sqlite')

class Chainsaw(Model):
    name = CharField()
    country = CharField()
    number = IntegerField()

    class Meta:
        database = db

    def __str__(self):
        return f'\n{self.name} {self.country} {self.number}'
# function to add records
def add_record(obj_name, obj_country, obj_number):
    # prompt user for data
    obj_name = input('Enter name: ') 
    obj_country = input('Enter country: ')
    obj_number = int(input('Enter nunber: '))

    # create instance of the chainsaw class and pass data to properties 
    obj_chainsaw = Chainsaw(name = obj_name, country = obj_country, number = obj_number)
    obj_chainsaw.save()

# function to search records
def search_record(obj_name):
    obj_name = input('Enter name: ') 
    search_result = Chainsaw.select().where(Chainsaw.name == obj_name)
    return search_result

# function to delete record
def delete_record(obj_name):
    obj_name = input('Enter name: ')
    deleted = Chainsaw.delete().where(Chainsaw.name == obj_name)
    obj_deleted = deleted.execute()
    return f'Number of record/s deleted: {obj_deleted}'

# function to update  the chainsaw record
def update_record(obj_name, obj_number):
    #update input
    obj_name = input('Enter chainsaw name to update: ')
    obj_number = int(input('Enter number: ')) 
    #update value stored in updated
    updated = Chainsaw.update(number = obj_number).where(Chainsaw.name == obj_name)
    obj_updated = updated.execute()
    return f'Number of record/s updated: {obj_updated}'


if __name__ == "__main__":
    
    db.connect() #connection to database established
    db.create_tables([Chainsaw]) #table created in database

    #instruction guide
    print(' APP INSTRUCTION GUIDE\n----------------------------')
    print('Enter letter \'A\' to add data\nEnter letter \'S\' to search record by name\nEnter letter \'U\' to add data')
    print('Enter letter \'D\' to delete record by name\nEnter letter \'E\' to exit application\n----------------------------\n')
    check = True
    while check:
        operation_choice = ['A', 'D', 'S', 'U', 'E'] # operation symbol
        print('\n') #line to demacate each operation

        # prompt user for operation type
        operation_symbol = input('Signify operation process: ') 
        choice = operation_symbol.upper() # convert user input to cap
        try:
            if choice == 'S':
                # search chainsaw record
                for item in search_record("obj_name"):
                    print(item)

            elif choice == 'D':
                # delete chainsaw record
                item = delete_record("obj_name")
                print(item)

            elif choice == 'A':
                # add chainsaw record
                add_record("obj_name", "obj_country", obj_number=2)

            elif choice == 'U':
                # update chainsaw record
                updated_item = update_record("obj_name", obj_number=1)
                print(updated_item)

            elif choice == 'E': # exit application
                check = False
                raise SystemExit

            else:
                print('Invalid operation sign!')# message displayed if wrong symbol is input
        except:
            print('Erro! Operation aborted...')
        finally:
            db.close() # database closed
