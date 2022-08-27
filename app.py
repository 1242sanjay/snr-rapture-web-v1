from flask import Flask, render_template

app = Flask(__name__)

courses = [
  {
    'id' : 1,
    'title' : 'Data Analysis',
    'price' : 'Rs. 2000',
    'description': 'After doing this course you will be able to apply for a data analyst role in any company',
    'image' : '1.jpg'
  },
  {
    'id' : 2,
    'title' : 'Data Science',
    'price' : 'Rs. 4000',
    'description' : 'This course is designed by our top data scientist having 10+ year of experience in field of data science.',
    'image' : '2.jpg'
  },
  {
    'id' : 3,
    'title' : 'Machin Learning',
    'price' : 'Rs. 5000',
    'image' : '3.jpg'
  },
  {
    'id' : 4,
    'title' : 'Deep Learning',
    'price' : 'Rs. 5000',
    'description' : 'This course is provide a practical understanding of deep learning model used in real life.',
    'image' : '4.jpg'
  }
]


@app.route("/")
def hello_world():
    return render_template('index.html', courses = courses)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
