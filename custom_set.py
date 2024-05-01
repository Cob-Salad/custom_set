

class CustomSet():
    
    def __init__(self):
        self.custom_set = []    
    
    def add(self, item: str):
        if item in self.custom_set:
            print("Invalid Input, No Duplicates Allowed")
        else:
            self.custom_set.append(item)

    def remove(self, item: str):
        try:
           self.custom_set.remove(item)
        except ValueError:
           print("Item not removed, moving forward")    
   

    def as_list(self):
        return self.custom_set        

    def clear(self):
        self.custom_set.clear()



def main():
    my_set = CustomSet()
    my_set.add("item 1")
    my_set.add("item 2")
    my_set.add("item 3")
    my_set.remove("soemtingn")

    print(my_set.as_list()) # ["item 1", "item 2", "item 3"]

    my_set.remove("item 2")
    print(my_set.as_list()) # ["item 1", "item 3"]

    my_set.clear()
    print(my_set.as_list()) # []

if __name__ == "__main__":
    main()
