# Application Server Setup

## Task 0: Set Up Development with Python

This task involves setting up a development environment for the AirBnB clone project on `web-01` server. The development environment will be used to test and debug code before deploying it to production.

### Steps:

1. **Ensure SSH Task Completion**: Verify task #3 of the SSH project is completed for `web-01`.
2. **Install net-tools**: Run `sudo apt install -y net-tools` on the server to install necessary network tools.
3. **Clone the Repository**: Clone the AirBnB_clone_v2 repository using `git clone https://github.com/YOUR_USERNAME/AirBnB_clone_v2.git`.
4. **Configure Flask Application**: Modify `web_flask/0-hello_route.py` to serve content from `/airbnb-onepage/` on port 5000. Ensure the application object is named `app`.
5. **Run the Flask Application**: Start the Flask application using `python3 -m web_flask.0-hello_route`.
6. **Test the Flask Application**: Use `curl 127.0.0.1:5000/airbnb-onepage/` to test if the application is running correctly.

### Example:

```bash
# Window 1
ubuntu@530605-web-01:~/AirBnB_clone_v2$ python3 -m web_flask.0-hello_route
 * Serving Flask app "0-hello_route" (lazy loading)
 * Environment: production
   WARNING: Do not use the development server in a production environment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
54.90.58.13 - - [02/May/2024 22:19:42] "GET /airbnb-onepage/ HTTP/1.1" 200 -

# Window 2
ubuntu@530605-web-01:~/AirBnB_clone_v2$ curl 127.0.0.1:5000/airbnb-onepage/
Hello HBNB!
