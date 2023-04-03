class Pagination:
    def __init__(self, items, pageSize) -> None:
        self.items = items
        self.pageSize = self.treating_number(pageSize)
        self.pages = self.split_items(items, self.pageSize)
        self.current_page = 1

    def split_items(self, items, pageSize):
        loop_number = len(items)/pageSize
        if loop_number%1 != 0:
            loop_number += 1
        loop_number = int(loop_number)
        return {i+1: items[i*pageSize:i*pageSize+pageSize] for i in range(loop_number)}
    
    def treating_number(self, number):
        try:
            return int(number)
        except:
            raise ValueError("The value should be a number")
            
    
    def getVisibleItems(self):
        print(self.pages[self.current_page])
    
    def nextPage(self):
        if self.current_page == len(self.pages):
            print("You are on the last page")
        else:
            self.current_page += 1
        return self
    
    def previousPage(self):
        if self.current_page == 1:
            print("You are on the first page")
        else:
            self.current_page -= 1
        return self
    
    def firstPage(self):
        if self.current_page == 1:
            print("You are already on the first page")
        else:
            self.current_page = 1

    def lastPage(self):
        if self.current_page == len(self.pages):
            print("You are already on the last page")
        else:
            self.current_page = len(self.pages)

    def goToPage(self, number):
        number = self.treating_number(number)
        if self.current_page == number:
            print(f"You are already on page {number}")
        elif number > len(self.pages):
            self.current_page = len(self.pages)
        elif number < 1:
            self.current_page = 1
        else:
            self.current_page = number

import string

p = list(string.ascii_lowercase)

p = Pagination(p, 4)

p.getVisibleItems() 
# ["a", "b", "c", "d"]

p.nextPage().previousPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]

p.goToPage(3)
p.getVisibleItems()

p.goToPage(-12)
p.getVisibleItems()