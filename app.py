from flask import Flask, render_template

app=Flask(__name__)

job=[
    {
        'id':'1',
        'title':'Data Analyst',
        'location':'banglore',
        'salary':'$1200'
    },
    {
        'id':'2',
        'title':'Software Enginerr',
        'location':'Chennai'
    },
    {
        'id':'3',
        'title':'Frontend Engineer',
        'location':'Hyderabad'
    }
]

@app.route('/')
def hello_world():
    return render_template('index.html',JOB=job)
    
    
if __name__=='__main__':
    app.run('0.0.0.0',debug=True)