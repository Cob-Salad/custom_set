true_list = []

class CustomSet():
    

    def add(put: str):
        if put in true_list:
            print("Invalid Input, No Duplicates Allowed")
        else:
            true_list.append(put)

    def remove(take: str):
        count = 0
        for i in true_list:
            if i == take:
                true_list.pop(count)
                return true_list
            count += 1
        raise KeyError

    def as_list():
        print(true_list)
    
    def clear():
        true_list.clear()



def main():
    CustomSet.add("hello")
    CustomSet.add("hello")
    CustomSet.add("hifeoaf")
    CustomSet.add("fhauewk")
    CustomSet.as_list()
    CustomSet.remove("hello")
    CustomSet.as_list()
    CustomSet.add("adjfioea")
    CustomSet.add("fhiae")
    CustomSet.clear()
    CustomSet.as_list()


main()
