from flask import Flask, render_template
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


#@app.route('/')
#@app.route('/Post')
class Template(Resource):
    def index(self):
        user = {'username': 'Vinod'}
        return render_template('index.html', title='Home', user=user)


api.add_resource(Template, '/Template')

if __name__ == '__main__':
    app.run(debug=True)
