from flask import Flask

app = Flask(__name__)

@app.route('/time')
def time():
    return f"Hozir vaqt 10:00"

@app.route('/day')
def day():
    return f"Bugun seshanba"
 
    
if __name__ == '__main__':
    app.run(debug=True)
