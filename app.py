from flask import Flask, render_template, request

from api_call import getLiveWeatherOf
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        place_name = request.form['place_str']
        # print(place_name)
        # print(request.form)
        context = getLiveWeatherOf(place=place_name)
        return render_template('index.html', context=context)
    else:

        return render_template('index.html', context=False)


if __name__ == '__main__':
    app.run(debug=True)
