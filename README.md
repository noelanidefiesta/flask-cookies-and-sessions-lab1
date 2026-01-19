# Cookies and Sessions Lab

## Scenario

In this lab, you'll be building out a blog paywall feature by using the session
hash to keep track of how many page views a user has made.

## Tools & Resources

- [GitHub Repo](https://github.com/learn-co-curriculum/flask-cookies-and-sessions-lab)
- [API - Flask: class flask.session](https://flask.palletsprojects.com/en/2.2.x/api/#flask.session)

## Set Up

There is some starter code in place for a Flask API backend and a React
frontend. To get set up, run:

```bash
pipenv install && pipenv shell
npm install --prefix client
cd server
flask db upgrade
python seed.py
```

You can work on this lab by running the tests with `pytest -x`. It will also be
helpful to see what's happening during the request/response cycle by running the
app in the browser. You can run the Flask server with:

```bash
python app.py
```

Open a second terminal which will be responsible for running the React app:

```bash
npm start --prefix client
```

You don't have to make any changes to the React code to get this lab working.

If you aren't currently running the Flask app, you may see:

```bash
Proxy error: Could not proxy request /articles from localhost:4000 to http://localhost:5555.
```

That's okay, that just means our Flask API isn't yet running, but the frontend is 
trying to make a request.

## Instructions

### Task 1: Define the Problem

Users are currently limited to seeing 3 articles on the site before hitting a 
paywall, but the logic is only in the frontend, so many tech-savvy users are 
getting around the paywall using browser dev tools.

### Task 2: Determine the Design

Our app will keep track of how many blog posts a user has viewed by using the
`session` object. Each user can view a **maximum of three articles** before
seeing the paywall. This will ensure the logic is on the backend and not as easy
for users to get around.

### Task 3: Develop, Test, and Refine the Code

#### Step 1: Initialize the Session for Page Views

When a user makes a `GET` request to `/articles/<int:id>`:

- If this is the first request this user has made, set `session['page_views']` to
  an initial value of 0.

#### Step 2: Increment the Session on Each Request

For every request to `/articles/<int:id>`, increment the value of 
`session['page_views']` by 1.

#### Step 3: Send Response Based on Session Data

- If the user has viewed 3 or fewer pages, render a JSON response with the
  article data.
- If the user has viewed more than 3 pages, render a JSON response including an
  error message `{'message': 'Maximum pageview limit reached'}`, and a status code
  of 401 unauthorized.

#### Step 4: Test the Endpoint

- In browser, navigate to your React app.
- Click on 4 articles. The first 3 should be visible. The last article should say
"Maximum articles viewed"
- An API endpoint at `/clear` is available to clear your session as needed. Navigate
to http://localhost:5555/clear to reset attempts.
- Run test suite with `pytest` to ensure all tests are passing.
  
#### Step 5: Commit and Push Git History

* Commit and push your code:

```bash
git add .
git commit -m "final solution"
git push
```

* If you created a separate feature branch, remember to open a PR on main and merge.

### Task 4: Document and Maintain

Best Practice documentation steps:
* Add comments to the code to explain purpose and logic, clarifying intent and functionality of your code to other developers.
* Update README text to reflect the functionality of the application following https://makeareadme.com. 
  * Add screenshot of completed work included in Markdown in README.
* Delete any stale branches on GitHub
* Remove unnecessary/commented out code
* If needed, update git ignore to remove sensitive data

## Submit your solution

CodeGrade will use the same test suite as the test suite included.

Once all tests are passing, commit and push your work using `git` to submit to CodeGrade through Canvas.
# flask-cookies-and-sessions-lab
