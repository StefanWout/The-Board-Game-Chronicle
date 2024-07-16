# The Board Game Chronicle

(A board game cafe's platform to allow visitors and regulars to track played games and review their experiences for other users)

# Problem Statement:

I need users to be able to track what they play at my cafe so that the data can be used to recommend games to new users.

## Target Audience: 

- Board game cafe's looking to engage more with their customers
- People who want to track their board gaming habits
- Players looking for a recommendation
- All age groups
- Experienced and novice players


## MVP Features:

- User registration and login to ensure task privacy and personalized experience
- Nav bar that links to the reviews page and user profile page
- Users can post reviews for the games they play that includes the following information:
  - User
  - Game Name
  - Review
  - Rating out of 5
  - Date Reviewed (auto)
  - Date Played (manual)
  - Game time
  - Number of Players
- Users can browse through game reviews by particular game
- Ability for users to remove or add reviews on their profile
- List of game available at the board game cafe

## Additional Features:

- Quiz with a clear set of multiple choice questions that narrows down game options in a particular venue’s library to one that is best suited to the group.
- Robust search and filtering features

# User Stories

## Guests (Unauthenticated Users)

- I want to browse the list of board games that have been reviewed so that I can explore different games available on the site
- I want to view detailed information about a board game, including its average rating, average no. players & average game duration, so that I can decide if I'm interested in it
- I want to read reviews of board games so that I can see what other players think about the games and how they are rated
- I want to register for an account so that I can participate more fully on the site, such as by writing reviews and rating games

## Registered Users

- I want to log in to my account so that I can access my profile
- I want to log out of my account when I am done using the site for security reasons
- I want to edit my profile information so that I can keep my details up to date
- I want my profile to provide me a way to keep track of the games I have played and when I played them
- I want to be able to add new games to the database
- I want to write and submit a review for a board game so that I can share my opinions with other users
- I want to rate board games on a scale (e.g., 1 to 5 stars) so that I can contribute to the overall rating of the game
- I want to edit or delete my reviews so that I can update my opinions or remove them if needed
- I want to be able to comment on other user’s reviews so I can engage in a discussion

## Administrator

- I want to add, edit, and delete reviews in the system so that I can keep the game database accurate and up to date
- I want to approve or moderate user reviews so that inappropriate content is not displayed on the site
- I want to manage user accounts, including suspending or banning users if necessary, to maintain a safe and respectful community
- I want to view site analytics, such as the number of users, reviews and comments, so that I can understand the site's performance and user engagement

## Wireframe & Initial Design:
### Home Page and Review Page, innitial design ideation
![1](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/Home%20and%20Review%20page%20wireframe.png)

### (Logged in) Profile
![1](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/profile%20page.png)

### Post a Review
![Add a Review wireframe](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/post%20review%20page.png)

### Reviews Page

![Reviews Wireframe](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/reviews%20page.png)

### Review Detail Page (guest)

![Review Details Wireframe](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/reveiw%20detail%20(guest).png)

### Review Detail Page (user)

![Review Details Wireframe](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/reveiw%20detail%20(user).png)
### Games Page

![Games Wireframe](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/games%20page.png)

### Games Detail Page (guest)

![Games Details Wireframe](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/games%20info%20page%20(guest).png)

### Games Detail Page (user)

![Games Details Wireframe](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/games%20info%20page%20(user).png)

## Agile:
Through the use of the kanban board functionality on github i was able to track my progress and outline clear goals to make sure I was staying on track. With hindsight, I would have added more granularity to the board as many of the tasks listed could have been broken down further,

![project board](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/project%20board.png)


# Design Choices:

## Colour scheme:

#780D0D - Header

#D6D9D7 - Header Font and main background

#1FC18E - Footer links

![1](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/color%20scheme.png)

The colours were selected with the intention of not pulling focus from the cards on the page.

## Typography:
The default fonts provided ideal clarity


## Priority Features:

### Home Page:

#### Navbar & Game Cards:
![home](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/Home%20page%20(user).png)

The landing page provides an introduction to the website with a call to action giving a hint at how to go about using the site.

The navigation bar is valuable for users as it provides quick and easy access to important sections of the website. The navigation bar includes links to Reviews and Games and Register. While logging in will bring up the Profile, Post a Review and Logout buttons. Keeping this area clean once again diverts attention to the games below.


#### Registration:

Registration is simple and only requires the user to provde a username, email and password. This is so that future iterations of the site can include a tickbox asking permission to send news to the user. No further details are needed. 

![signup](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/Registration%20page.png)



#### Sign In:

![sign-in](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/Sign%20in%20page.png)


#### Reviews:

![reviews](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/reviews%20page.png)


#### Post a Review:

![add a Review](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/post%20review%20page.png)


The form allows users to easily add the relevant information about their play session here. This data will allow future visitors to make an informed decision about what games to play based on prior experiences. 

#### Games:

![games](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/games%20page.png)

#### Game Details:

![game detail](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/games%20info%20page%20(user).png)

All the information found here, including the image were pulled from the boardgamegeek.com open api and saved in the Game model. The python script ran once and pull all the data for the specific list of games in the cafe's library (games_data_load.py). Adding games to the model from the api would require a change in the list of games being called in the main function. The admin can add games manually as an alternative, especially if they disagree with the information provided by boardgamegeek.com. 

#### Footer:

![footer](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/footer.png)

Links in the footer redirect to respective social media pages. 
It allows users to stay connected with the The Board Game Chronicle on social media platforms, keeping them informed about any changes that may occur over time.


# Future Features:

* Implement a comment system so users can share their thoughts about games that they chose based on previous reviews. 
* Robust review search and filtration.
* Allow users to furhter customize their profile.
* A quiz that can narrow down the list of games to one best suited to the group.
* Provide news and promotional info from the cafe.
* Provide a way for the users to engage and form a secure community.



Database Design:

![ERD](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/Data%20Schema.png)


Entity Relationship Diagrams (ERD) helped me understand the M in MVC framework much better. Despite not building on the comment model, having it included in the innitial planning will make it easier to implement in future. I used dbdiagram.io to create the diagram.


## Data Models:


Table user {
  id integer [primary key]
  username varchar
  email emailfield 
  password varchar
}

Table reviews {
  id integer [primary key]
  user_id integer
  game_id integer
  title text
  review_text text [note: 'Content of the post']
  rating integer [note: '1-5 stars']
  created_at timestamp
  date_played timestamp
  game_duration integer
  player_count integer
}

Table comments {
  id integer [primary key]
  user_id integer
  review_id integer
  body text [note: 'Content of the comment']
  created_at timestamp 
}

Table gamesG {
  id integer [primary key]
  game_name text
  game_description text
  min_players integer
  max_players integer
  playing_time integer
  image image
}


## User Flow Chart:
![Flowchart](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/User%20flow%20chart.png)

Double lines indicate connections to pages that only appear to registered users.

The flowchart helped me track a user journey through the site, allowing me to be sure that they would have access to all fucntionality no matter where they ended up.

# Validation
## HTML

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home (guest) | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2F) | ![home page validate](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20index.png) | As a result of pulling data from the boardgamegeek open API, the game descriptions were filled with html tags. I removed that data when displaying it on my project so the extraneous code does not effect performance |
| Games | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Fgames%2F) | ![Games page](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20games.png) | No Errors, despite displaying much of the same data that is seen on the home page |
| Game Details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Fgames%2F2655%2F) | ![Game Details page](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20game%20info.png) | Same issues with the invisible data tags within game descriptions |
| Reviews | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Freviews%2F) | ![Reviews page](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20reviews.png) | one small positioning error that I wasn't able to root out |
| Review Details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Freviews%2F1%2F) | ![Review Details page](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20review%20info.png) | invisible data tags |
| Post a Review | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Fadd_review%2F) | ![post a review page](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20post%20review.png) | A long series of errors that pertain to summernote. As I have experienced no issues with it as a user, I'll leave them at that. |
| Sign In | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Faccounts%2Flogin%2F) | ![validate sign in](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20sign%20in.png) | Pass: No Errors, error depicted was removed |
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Faccounts%2Fsignup%2F) | ![validate sign up](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20Register.png) | unclosed elements |
| Profile | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Fprofile%2F1) | ![profile page](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/errors%20profile.png) | unclosed main and positioning issues |

 ## CSS

 I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate my CSS file.
 
| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fthe-board-game-chronicle-8588bc8b62ba.herokuapp.com%2Fstatic%2Fcss%2Fstyle.css&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en) | ![validate css](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/css%20errors.png) | Pass: No Errors |

## Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | Screenshot | Notes |
| --- | --- | --- |
| forms.py | ![screenshot]![forms py](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/forms%20valid.png) | Pass: No Errors |
| settings.py | ![screenshot]![settings py](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/settings%20valid.png) | Pass: No Errors |
| views.py | ![screenshot]![views py](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/views%20valid.png) | Pass: No Errors |
| urls.py| ![screenshot]![urls py](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/urls%20valid.png) | Pass: No Errors |
|  models.py | ![screenshot]![models py](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/models%20valid.png) | Pass: No Errors |
|  game_data_load.py | ![screenshot]![game_data_load py](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/load%20game%20data%20script%20valid.png) | Pass: Errors are benign and too fiddly to worry about, ran the script three times over the course of the build and it can be run again as way to add many games at once to the model (especially useful in the type of crisis where there is a need to change database management systems. Most of the content on the site is dependent on the information stored in the game model |

# Responsiveness:
Development tools were used to test responsiveness on varying sized devices including laptop, mobile and tablet size.

Full testing was performed on the following devices:

Laptops:

* Acer Predator Triton 300 15.6-inch screen
  
 Mobile Devices:

* Google Pixel 7
* Samsung Galaxy Tab S9

 * Browser Compatibility:
 
 I have tested the site using the following browsers:

* Google Chrome

![chrome](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/Home%20page%20(user).png)

* Mozilla Firefoz

![Firefox]()


I can confirm that the site is responsive and looks as expected good on different screen sizes.


Mobile devices:

![home](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/mobile%20home.png)

![games](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/mobile%20games.png)

![gamesdetails](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/mobile%20game%20details.png)

![reviews](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/mobile%20reviews.png)

![reviewsdetails](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/mobile%20review%20details.png)

![register](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/mobile%20register.png)

![post review](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/mobile%20post%20a%20review.png)

![profile](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/mobile%20profile.png)

Tablet Devices:


![homepage]()

![signup tablet](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/tablet%20register.png)

![reviews tablet](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/tablet%20reviews.png)

![tabletadd](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/tablet%20post%20a%20review.png)

![games tablet](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/tablet%20games.png)

![games details tablet](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/tablet%20game%20details.png)




# Testing:

## Lighthouse Audit:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.


* On a laptop:

Home

![homeaudit](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/lighthouse%20desktop%20home.png)

Games 

![auditgames](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/lighthouse%20desktop%20games.png)

Revies 

![auditreviews](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/lighthouse%20desktop%20reviews.png)

Post a Review 
![add review](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/lighthouse%20desktop%20add%20review.png)

On a mobile device:

Home 
![home mobile ](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/lighthouse%20mobile%20index.png)

Games
![auditgames](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/lighthouse%20mobile%20games.png)

Reviews
![auditreviews](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/lighthouse%20mobile%20reviews%20.png)

Post a Review 
![audit addreviewmobile](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/lighthouse%20mobile%20add%20review%20.png)


## Links

| Link | Expected Outcome | Grade |
| ------- | ---------------- | ----- |
| Logo | Navigates to the home page when clicked | Fail |
| Home | Navigates to the home page when clicked | Pass |
| Books | Navigates to a book list  page when clicked | Pass |
| Add a Book | Navigates to a form to add a book when clicked | Pass |
| Register | Navigates to a registration form when clicked | Pass |
| Log in | Navigates to a screen where users can log in when clicked | Pass |
| Logout | Navigates to a page confirming for the user to log out | Pass |

## Testing 


| Feature | Expected Outcome | Grade | Screenshots |
| ------- | ---------------- | ----- | --------- |
| Modal | A message will appear asking to confirm if they want to delete | Pass | ![modal delete reveiw ](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/delete%20modal.png)
| View Profile | Users can see the reviews they added | Pass | ![testing profile](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/profile%20page.png)
| Add a review | Add a review | Pass | ![addreview](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/post%20review%20page.png)
| Admin has access to crud functionality of all additions | Admin can edit or delete any book addition | Pass | ![admin testing](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/testing%20admin%20view.png)
| Edit a review | A user can edit the details on the book that they have addded. It will update their addition on the books page | Pass | ![edit review ](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/delete%20modal.png)
| Registration | New users can access a registration form from the "Register" link | Pass | ![testing sign up](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/Registration%20page.png)
| Log in | Users can log in using a form after clicking "Log in" | Pass | ![sign in testing ](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/Sign%20in%20page.png)
| Log out | Users get logged out after clicking "Log out" | Pass | ![testing sign out]()
| Functional buttons | Edit, delete, create buttons will be functional throughout the site | Pass | ![edit delete buttons](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/delete%20modal.png)
| Footer | A footer displays social information | Pass | ![footer](https://github.com/StefanWout/The-Board-Game-Chronicle/blob/main/assets/footer.png)
| Social links work | The social links will navigate to a new page when they're clicked. They will open in a new tab | Pass |


# Tools and Technologies Used:
The technologies implemented in this application included HTML5, CSS, Bootstrap, Javascript, Python and Django.

* Python used as the back-end programming language.
* JS used for the modal confirmation button on delete.
* Git used for version control.
* GitHub used for secure online code storage.
* GitHub Pages used for hosting the deployed front-end site.
* Gitpod used as a cloud-based IDE for development.
* Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
* PostgreSQL used as the Postgres database.
* Heroku used for hosting the deployed back-end site.



* Google and Stack Overflow utilized for general research or solving a bug, information gathering, and various online tools.


# Languages Used:
* HTML5
* Javascript
* CSS
* Python

# Deployment :

Previous Heroku deployments made this a simple process that encountered no issues

# Bugs

All the bugs were squashed. There are features missing like password resets and more to be added to the user model, however this is a solid foundation on which to build future features.


# Credit: 

* I used the django blog resources provided on the LMS to do the innitial set up.

* was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.

* Thanks to my fellow students for their help.

* boardgamegeek.com provided the open API from which I sourced much of my data.

* A special thanks my friend Khalim for walking me through using Xml to write the script that pulled that data.

* Font Awesome was used for icons and the fonts used were derived from Google Fonts.

* Wireframes, logo and flowcharts were created using Balsamiq and Gimp. 

