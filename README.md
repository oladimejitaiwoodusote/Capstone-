# Collectorsgramm

Inspired by my personal love of vinyl records and music, Collectorsgramm is a social media application built for react.js and flask for vinyl enthusiasts to show off their collections and connect with other vinyl collectors. 

<img width="448" alt="Screen Shot 2024-01-05 at 4 58 49 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/b88dfd7f-fd0f-4f22-a954-b61bc2dce6a3">

##Technologies Used

### Front End Technologies

- React.js
- Material-UI

### Back End Technologies

- Flask
- Flask-SQL Alchemy
- Flask-Migrate

### Database

-SQLite

## Features

### User Account and Profile Management

- Account Creation: Users can sign up to create personal accounts
<img width="354" alt="Screen Shot 2024-01-18 at 1 19 44 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/ff4d2872-d7a7-45dc-a10c-a26a513f41fa">

- User Authentication
<img width="448" alt="Screen Shot 2024-01-05 at 4 58 49 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/b88dfd7f-fd0f-4f22-a954-b61bc2dce6a3">

- Profile Customization: Users can edit their profiles
<img width="482" alt="Screen Shot 2024-01-18 at 1 22 10 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/53379a80-a210-4ede-8b9d-c7ac0033e0ca">

### Social Interation
- Following System: Users can follow and unfollow other users, creating a personalized feed and network
- Post Interaction: Users can like and comment on posts
- Discovery Page: Users can explore posts from users not currently followed
<img width="575" alt="Screen Shot 2024-01-18 at 1 27 08 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/e467f2b7-a8d0-45f0-9146-1f296ef3ebff">


### Content Creation and Management

- Post Creation: Users can upload new posts
<img width="587" alt="Screen Shot 2024-01-18 at 1 35 45 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/205ac545-6f4b-4882-90c6-b1a9aaae0b92">
<img width="383" alt="Screen Shot 2024-01-18 at 1 36 27 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/5fa81677-3625-4f94-99e9-5e895cc61ffa">
  
- Post Editing and Deleting: Users can edit and delete uploaded posts
<img width="346" alt="Screen Shot 2024-01-18 at 1 36 09 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/f62f829c-ae32-4f06-bebd-52f7eecaa226">

### User Feeds

- Main Feed: A customized feed displaying posts from followers users
- Profile Pages: Dedicated pages for each user, showcasing their individual posts and prpfoile information
<img width="467" alt="Screen Shot 2024-01-18 at 1 42 15 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/68d6c574-c241-48cf-a848-8f1e8351bced">
<img width="906" alt="Screen Shot 2024-01-18 at 1 42 27 PM" src="https://github.com/oladimejitaiwoodusote/Capstone-/assets/79773788/b37cfe99-a965-4b6c-a80b-be8daa1bdbe6">

### Backend (Flask App)

- Clone the repo `https://github.com/oladimejitaiwoodusote/Capstone-`
- Navigate to the server directory `cd server`
- Create a virtual python environment  `python -m venv myenv`
- Activate virtual environment  `source myenv/bin/activate`
- Install required project dependencies  `pip install -r requirements.txt`
- Set up the flask database  `flask db init` `flask db migrate -m 'Initial migration'` `flask db upgrade `
- Run the flask app  `flask run`

### Frontend (React App)

- Open a new terminal and naivagate to the client directory `cd ..` `cd client`
- Install the necessary npm packages `npm install`
- Start the React development server `flask run`
