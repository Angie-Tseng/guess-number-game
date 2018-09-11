'''
Some costumized input function
'''

#A function that can input integer safely
def input_int(question):
    while True:
        try:
            ans = int(input(question))
            break
        except:
            print("Input error: please try again")
    return ans

#A function that can input integer by entry safely
def input_by_entry(entry):
    try:
        ans = int(entry.get())
        return ans
    except:
        print("Input error: please try again")
    

#A function to create y/n question and return True/False
def y_n_question(question):
    while True:
        answer = input(question + " (y/n): ")
        if answer == "y":
            return True
        if answer == "n":
            return False