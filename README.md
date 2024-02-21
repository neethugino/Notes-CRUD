# Notes-CRUD


Steps to run
1- Download the code
2- Unzip the file
3- run command python app.py
    By default, it will be accessible at http://127.0.0.1:5000/ in your web browser.
5- Open Postman
6- Click on the "New" button in the top-left corner to create a new request.
7- Give your request a name
8- Set the request type to "POST"
9- Enter the URL for the signup route, e.g., http://localhost:5000/signup
10- Go to the "Body" tab and choose the "raw" option
11- Set the data format to JSON (application/json)
12- Add request body like given below
    {
      "username": "testuser",
      "password": "testpassword"
    }
13- Change the URL for the login route, e.g., http://localhost:5000/login
14- similar way check all the end points
15- To ensure the functionality and integrity of the API endpoints, run command python -m unittest test.py

