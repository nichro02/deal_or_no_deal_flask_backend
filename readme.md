# Project Overview
This is the backend for my React Deal or No Deal frontend. This repo includes my models and RESTful routes needed for the game. 

Here's a [link](https://github.com/nichro02/deal_or_no_deal_react_frontend) to my frontend repo.

One thing to note: Comments are on the roadmap but that functionality is currently not available.

# Tech Stack
## Security and Authentication
- bcrypt: I used bcrypt to hash user passwords so they can be securely stored in the database.

## Framework
- Flask: The backend is built on the Flask framework

## Database
- SQL: I prefer relational databases because they are more structured, although at the cost of some flexibility.
- Psycopg2: I used psycopg2 as a PostgreSQL adapter for Python

## ORM
- Peewee: I like peewee for its simplicity and ease of use.

The ORM I referred to when writing my backend can be seen below.

<img 
    src="https://whimsical.com/embed/SCYBNCovAart56WWgh9zLT@2Ux7TurymMreRJ9CTdGZ" 
    alt="Deal or No Deal Flask ORM"
    width="400"
    height="225"
/>

# Routes
Method | URL | Action
-------|-----|-------
POST | /register | Register new players
POST | /login | Login existing players
GET/POST | /logout | Logout players
GET | /<player_id> | Retrieve a single user
PUT | /<player_id> | Update a player's profile
Delete | /<player_id> | Delete a player's profile
POST | / | Record game results
GET | /top_scores | Retrieve high scores

# Problems/Challenges
* I haven't worked with Flask before so there was a learning curve, but I enjoyed working with it overall.

* One of the bugs that came up during testing was the PUT route to update a user's bio sometimes resulted in an OPTIONS method that had the effect of turning the PUT into a GET. I'm still investigating the cause of this.

# Link to Deployed App
Deployed link to come