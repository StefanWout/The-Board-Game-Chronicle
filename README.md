# The Board Game Chronicle

(A board game cafe's platform to allow visitors and regulars to track played games and review the experience for other users)

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

* Macbook Air 2018 13.3-inch screen
* Lenovo Thinkpad 14" screen

 Mobile Devices:
* Google Pixel 4a

 * Browser Compatibility:
 
 I have tested the site using the following browsers:

* Google Chrome

![chrome](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/545ba4e5-c7bc-4fd8-8660-1444dcb3be2a)


* Microsoft Edge

![microsoft edge](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/1570a9cd-6591-45db-840b-ecbe7f7aeb5b)


I can confirm that the site is responsive and looks as expected good on different screen sizes.


Mobile devices:

![Screenshot_20231207-234024](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0f0b0d7d-a72f-43a4-8a57-bc1cf02a1367)

![Screenshot_20231207-234033](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/4c3cc202-b8f6-4f9d-b1bd-cf57c911db65)

![Screenshot_20231207-234013](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/39989e07-4e8d-4faf-8b57-e11686792b38)


![0](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/211095bf-ffac-42ca-b1c8-2a45d8444038)

![Screenshot_20231207-234117 (1)](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e52d022b-d3fb-4f6c-8fcb-092386ce566b)

![Screenshot_20231208-000014](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0cd224f9-b46e-4db9-9260-999cc63fff90)





Tablet Devices:


![homepage](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5e6eb5c7-4aba-434c-8ed8-8bfd56632f8a)

![signup tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/c5f5a237-83ee-4ef3-b9b0-444f648ca225)

![sign in tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9ac1d08b-d4b8-4aa5-a65b-e46040f3b60b)

![books tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/a9c42d34-a49a-48ed-97ba-660c02de3543)

![tabletadd](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/b516d61d-6e21-460a-b7f4-5b18abf41d00)

![bookdetails tablet](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/17a0f099-ae15-4b8a-887b-254beac2dbb0)





# Testing:

## Lighthouse Audit:

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.


* On a laptop:

Home

![homeaudit](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/5fa9bac2-d4bf-47fe-bb4a-50b3b0c4938b)

Books 

![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d6401b01-e4d5-4ed1-b8e9-ff6d5eeb4bd9)

Add a book 
![audit add book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e429ee62-ecbe-4b2f-8521-28da15773a46)

On a mobile device:

Home 
![audit home mobile ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/348889e3-8c4e-41d4-b1c6-2c974780e23b)

Books
![auditbooks](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/fad662af-54da-45d0-b381-c0d70955e4e4)

Add a book 
![audit addbookmobile](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/634965ca-1b9d-4aa1-bd17-bda89f9fbafe)


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
| Modal | A message will appear informing the user of a successful action | Pass | ![modal sign out ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/9e8658e8-f751-4cdf-be3d-ca19ad6c47b2)
| User logged in | Text displays the user logged in with their username | Pass | ![modal sign in name](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/cc4a71db-9962-49c1-b4b6-563000687ad7)
| View books | Users can see available books which have been added | Pass | ![testing books](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/01cc3a5b-db46-4742-a8e1-cf715d78c89b)
| Add a book | Add a book to the book collection that will be available to borrow | Pass | ![addbook](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/82133f44-d43a-4f40-863a-f4e8970057aa)
| Admin has access to crud functionality of all additions | Admin can edit or delete any book addition | Pass | ![admin testing](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/72df0b87-6d4f-4659-9d4f-5e986f88e16c)
| Edit a book | A user can edit the details on the book that they have addded. It will update their addition on the books page | Pass | ![edit book ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/79f6de7e-fd14-4c34-a474-483b7cd5285f)
| Delete a book | A user who added a book OR an admin can delete a book. It will then be deleted from the DB | Pass | ![delete book](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/88275723-e875-404a-b96f-58bac0a4907a)
| Registration | New users can access a registration form from the "Register" link | Pass | ![testing sign up](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/e9e6c4e1-c90a-4854-a11c-014a8fc80043)
| Log in | Users can log in using a form after clicking "Log in" | Pass | ![sign in testing ](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/3fafee34-e6d6-4162-8989-faa78e1bf355)
| Log out | Users get logged out after clicking "Log out" | Pass | ![testing sign out](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/d7d377aa-fc2d-4025-a73e-22d2d81c622a)
| Grid display | A CSS grid will display the books in a clear, responsive format | Pass | N/A
| Functional buttons | Edit, delete, create buttons will be functional throughout the site | Pass | ![edit delete buttons](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/67cfb78d-7d5b-4072-8aa8-812b9c444b67)
| Footer | A footer displays social information | Pass | ![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0879fada-18a4-4363-8257-0af0061cf79f)
| Social links work | The social links will navigate to a new page when they're clicked. They will open in a new tab | Pass | ![footer](https://github.com/hiboibrahim/thebookbooth1/assets/144109298/0879fada-18a4-4363-8257-0af0061cf79f)


# Tools and Technologies Used:
The technologies implemented in this application included HTML5, CSS, Bootstrap, Python and Django.

* Python used as the back-end programming language.
* Git used for version control. (git add, git commit, git push)
* GitHub used for secure online code storage.
* GitHub Pages used for hosting the deployed front-end site.
* Gitpod used as a cloud-based IDE for development.
* Bootstrap used as the front-end CSS framework for modern responsiveness and pre-built components.
* ElephantSQL used as the Postgres database.
* Heroku used for hosting the deployed back-end site.
* Cloudinary used for online static file storage.
* Canva Utilized for collaborative design and prototyping(wireframes).

* Google and Stack Overflow utilized for general research or solving a bug, information gathering, and various online tools.


# Languages Used:
* HTML5
* CSS
* Python

# Deployment :

I used the steps used when deploying our django blog to deploy this application. The instructions for this mainly came from the follow along videos and text-steps provided on the code institute LMS.

# Bugs

All the bugs that occured during the creation of this application have been resolved. There is a section of the application which allows you to reset your password that needs to be implemented, however they were not within the scope of this particular project and will be addressed in the near future along with the other future features.


# Credit: 

* Although I used the django blog resources provided on the LMS, I also received alot of additional clarification by following along with django projects on YouTube. One of the vidoes I found especially helpful was : https://youtu.be/JzDBCZTgVyw?si=w3BBwJswUjBTm1xw

* Stack Overflow was used to solve any smaller bugs and further clarification on errors I was receiving in the terminal.

* I used this site to generate a persona and created user stories: https://founderpal.ai/user-persona-generator

* A special thanks to all the other indivudals in our cohort for their continuous support throughout the course.

* The added book covers and details were taken from the Waterstones Website.

* Font Awesome was used for icons and the fonts used were derived from Google Fonts.

* Wireframes, logo and flowcharts were created using Canva. 

