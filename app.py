from flask import Flask

app = Flask(__name__)

print("pr3")

@app.route('/')

def print_item(box, itemname):
    print(f'There is a price of {itemname}: ')
    return(box[itemname])

def add_bread(box):
    itemname = 'bread'
    itemvalue = 10
    box[itemname] = {itemvalue}
    print('There is a basket with new item: ')
    return(box)

def print_basket_len(box):
    print("Number of items in teh basket: ")
    return(len(box))

def print_basket(box):
    print("There is the basket now: ")
    return(box)


box = {'potato': 20, 'meat':70, 'cheese':35, 'tea':15}

print(print_basket(box))
print(print_basket_len(box))
print(add_bread(box))
print(print_item(box, 'meat'))

if __name__ == '__main__':
    app.run(debug=True)