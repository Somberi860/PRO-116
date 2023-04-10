# importing modules from flask library
from flask import Flask, render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'


@app.route("/")
def home():

    name = "Charan"  # write your name
    age = "16"  # write your age

    return render_template('index.html', name=name, age=age)

# define the route to father webpage


@app.route("/father")
def father():

    father_name = "Sasi"  # write your father's name
    father_age = "45"  # write your father's age

    return render_template('father.html', father_name=father_name, father_age=father_age)


# define the route to mother webpage
@app.route("/mother")
def mother():

    mother_name = "Uma"  # write your mother's name
    mother_age = "42"  # write your mother's age

    return render_template('mother.html', mother_name=mother_name, mother_age=mother_age)


# define the route to friends webpage
@app.route("/friends")
def friends():

    friend1 = "Luis"  # write your friend's name

    return render_template('friends.html', friend1=friend1)


# run the file
if __name__ == '__main__':
    app.run(debug=True)
