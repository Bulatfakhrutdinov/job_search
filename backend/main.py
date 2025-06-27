from flask import Flask, request, render_template


app = Flask(__name__, template_folder='../frontend')  # указываем путь к HTML-файлам

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=["POST"])
def search():
    description = request.form.get("description")
    print(description)
    if not description:
        return 'Description is empty', 400
    return 'Description has been successfully received', 200


if __name__ == '__main__':
    app.run(debug=True)