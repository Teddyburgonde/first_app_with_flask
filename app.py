from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')
    
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
  