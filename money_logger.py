#imports
import decimal #seeing as how the software will be dealing with money values, gonna need decimal
import pickle #python based serialization module, will be used for serializing objects mainly
import tkinter as tkntr #wanna have a decent graphical interface
import sqlite3 as SQL3 #think a database will be a bit nicer than a txt file to store values

#variables

#classes
class value: #this is going to be the main class for this project
 def __init__(self, month, date, year, money):
  self.month = month
  self.date = date
  self.year = year
  self.money = money

 def __lt__(self, other): #not completely sure if this will work but dont have enough built to test it yet so we'll see ¯\_(ツ)_/¯
  return self.year < other.year
  return self.month < other.month
  return self.date < other.date
 
#functions
def loadGui(): #used to load the GUI via tkinter
 pass