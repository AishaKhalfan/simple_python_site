# simple_python_site
A simple Flask web application showcasing various features and functionalities.

The repository contains a simple Python web application using Flask framework. It consists of the following files:

+ ```app.py```: This file is the main application file where the Flask app is defined and configured.

+ ```static```: This directory is used to store static files such as CSS, JavaScript, or images for the web application.

+ ```templates```: This directory contains HTML templates that are used to render dynamic content for different routes of the web application.

+ ```views```: This directory contains various endpoints for our Site

+ ```README.md```: This is the readme file that provides information about the project. However, the content of the readme is not specified in the given information.


## Installation

To install the project, run the following command:
```git clone https://github.com/AishaKhalfan/simple_python_site.git```


## Usage

To run the project, run the following command:

```python3 app.py```


The project will be hosted at `localhost:5000`.

## Contributing

To contribute to the project, fork it on GitHub and make your changes. Then, submit a pull request.

## License

The project is licensed under the MIT License.

### To run the Flask app, follow these steps:

- Make sure you have Flask installed. You can install it using pip: 
	```pip install flask.```

- Create a Python file (e.g., app.py) and import the necessary modules:

## Create the Flask application object
```app = Flask(__name__)```
- Define routes and functions for your app. For example:
	- @app.route('/')
	def home():
	    return 'Hello, World!'

	@app.route('/about')
	def about():
	    return 'This is the about page.'
- At the end of your file, add the following code to run the Flask development server:

	if __name__ == '__main__':
	    app.run()
- Save the file and navigate to the directory containing your Python file using the command line.

- Run the Flask app by executing the Python file: python app.py.

- Flask will start the development server, and you'll see output indicating that the app is running.

- Open your web browser and enter http://localhost:5000 (or http://127.0.0.1:5000) in the address bar.

- You should see "Hello, World!" displayed on the page. You can also visit http://localhost:5000/about to see the about page. Remember to modify the code to suit your specific application.
