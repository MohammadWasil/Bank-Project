#python file
import pandas as pd
from flask import Flask

app = Flask(__name__)


#data = pd.read_excel ("D:/My budget/Groceries with card.xlsx")
#data.set_index(keys="S. No", inplace = True)

#print(data.head())

data=[
    {
        'name':'Audrin',
        'place': 'kaka',
        'mob': '7736'
    },
    {
        'name': 'Stuvard',
        'place': 'Goa',
        'mob' : '546464'
    }
]


@app.route('/')
def display_transaction():
    return render_template(render_template("bank.html"), data=data)
    
    
if __name__ == "__name__":
    app.run(debug=True)
    
    