from peewee import *
from os import path

connection = path.dirname(path.realpath(__file__))
db = SqliteDatabase(path.join(connection, "cynthia.db"))

#creating our first table
class Student(Model):
    stud_name = CharField()
    stud_email = CharField()
    stud_password = CharField()

    class Meta:
        database = db
Student.create_table(fail_silently=True)


class Teacher(Model):
    teach_name = CharField()
    teach_email = CharField()
    teach_password = CharField()

    class Meta:
        database = db
Teacher.create_table(fail_silently=True)




class Users(Model):
    users_name = CharField()
    users_email = CharField()
    users_password = CharField()
    users_phone = CharField()

    class Meta:
        database = db
Student.create_table(fail_silently=True)

class Product(Model):
    price = IntegerField()
    quantity = IntegerField()
    desc = CharField()
    colour = CharField()

    class Meta:
        database = db


Product.create_table(fail_silently=True)



