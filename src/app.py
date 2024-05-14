from flask import Flask, render_template
import os 

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir,'src', 'templates','Page')

app = Flask(__name__,template_folder=template_dir, static_folder='/' )


#Rutas de la aplicacion
@app.route('/')
def login():
    return render_template('index.html')
@app.route('/')
def main():
    return render_template('main.html')



@app.route('/IX')
def home():
    return render_template('main.html')

@app.route('/MR')
def mentores():
    return render_template('mentores.html')


@app.route('/RH')
def resorcehuman():
    return render_template('rh.html')

@app.route('/TR')
def traineePage():
    return render_template('trainers.html')




if __name__ == '__main__':
    app.run(debug=True, port=4000)