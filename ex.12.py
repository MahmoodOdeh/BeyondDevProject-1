# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 00:59:30 2023

@author: odehm
"""

#Suppose you're building a logging library for a web application that needs to keep
#track of all requests and responses. You want to use the Singleton pattern to ensure
#that there's only one instance of the logger class throughout the application.

class Library:
    instance = None
    books = {}

       
    def __new__(cls, books=None):
        if cls.instance is None:
            cls.instance = super(Library, cls).__new__(cls) # intilize the books array
            cls.instance.books = {} if books is None else books
        return cls.instance

    def returns(self, bookName):   # return all the books in the library
       if((bookName not in self.instance.books)):     
           self.instance.books[bookName] = 1
       else:
           self.instance.books[bookName]=self.instance.books[bookName] + 1
           
           
    def request(self, bookName):   # ask for abook if exist in the library
        if((bookName not in self.instance.books) or self.instance.books[bookName] <= 0):
            self.instance.books[bookName]=self.instance.books[bookName] - 1
            print("Tshe book is not found in the library")
        else:
            self.instance.books[bookName]=self.instance.books[bookName] - 1

   
    def getBook(self):
       return self.instance.books # get the book
   
    
    def setBook(self, setbook):
        self.instance.books = setbook # set a new book
       
  

def main():
    logger1 = Library({"One piece" : 0, "Sanderella" : 0, "Naruto" : 2})
    logger2 = Library()
    logger2.returns("One piece")
    logger2.request("One piece")
    logger2.setBook({"One piece" : 0, "Sanderella" : 0, "Naruto" : 2})
    print(logger1.getBook())
    print(logger2.getBook())
   
if __name__ == "__main__":
    main()
