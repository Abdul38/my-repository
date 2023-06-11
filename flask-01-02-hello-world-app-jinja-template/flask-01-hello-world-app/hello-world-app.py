#-Import Flask module.

#- Create an object named `app` from imported Flask module.

#- Create a function `hello` which returns a string `Hello World`.

#- Assign a URL route the `hello` function with decorator `@app.route('/')`.

#- Create a function `second` which returns a string `This is the second page` and assign a URL route the `second` function with decorator `@app.route('/second')`. 

#- Create a function `third` which returns a string `This is the subpage of third page` and assign a URL route the `third` function with decorator `@app.route('/third/subthird')`. 



from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
    return "<h1>Hello World</h1>"


#-Create a function `second` which returns a string `This is the second page` and assign a URL route the `second` function with decorator `@app.route('/second')`. 
@app.route('/second')
def second():
    return "<h2>This is the second page</h2>"




   # Create a function `third` which returns a string `This is the subpage of third page` and assign a URL route the `third` function with decorator `@app.route('/third/subthird')`. 

@app.route('/third/subthird')
def third():
    return "<h3>This is the subpage of the third page</h3>"

@app.route('/forth/<string:id>')
def forth(id):
    return f'This is page id{id}'

if __name__ == '__main__':
    app.run(debug=False)












