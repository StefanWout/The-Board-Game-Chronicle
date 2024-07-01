# The Board Game Chronicle

(A platform to track played games and discuss your experience with other users)

# Problem Statement:

I need to track my thoughts about the games I play and find new games to play from other users.

## Target Audience: 

- People who want to track their board gaming habits
- All age groups
- Experienced and novice players
- Players looking for a recommendation

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
- Users can browse through game reviews by game
- Ability for users to remove or add reviews on their profile

## Additional Features:

- List of game libraries available at local board game cafes
- Quiz with a clear set of multiple choice questions that narrows down game options in a particular venue’s library to one that is best suited to the group.
- User profile that lists the chosen games from each time the user goes through the quiz

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



To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you, so do not share it. If you accidentally make it public, you can create a new one with _Regenerate API Key_.

### Connecting your Mongo database

- **Connect to Mongo CLI on a IDE**
- navigate to your MongoDB Clusters Sandbox
- click **"Connect"** button
- select **"Connect with the MongoDB shell"**
- select **"I have the mongo shell installed"**
- choose **mongosh (2.0 or later)** for : **"Select your mongo shell version"**
- choose option: **"Run your connection string in your command line"**
- in the terminal, paste the copied code `mongo "mongodb+srv://<CLUSTER-NAME>.mongodb.net/<DBname>" --apiVersion 1 --username <USERNAME>`
  - replace all `<angle-bracket>` keys with your own data
- enter password _(will not echo **\*\*\*\*** on screen)_

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
