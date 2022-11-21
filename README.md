# Welcome to the Mass Effect 1 Planet Tracker!
The purpose of this site is to help Mass Effect 1 (ME1) players track which planets they have visited or scanned, and log any discoveries they've made there. 

As someone who just played ME1 for the first time, one of the pieces of functionality I missed was a way to keep track of systems and planets I'd visited. In Mass Effect 2, each system is labelled with a percentage, telling you how much of that system you've visited. All unvisited planets are also clearly labelled. Unfortunately, this does not exist in ME1, so I (along with many other players) resorted to using a pen and a notepad. This was very manual, and involved a lot of flipping pages and rereading lists to see if I'd been to a particular planet before - there are 39 systems in the game, and each one has 3-6+ planets, so it's hard to remember them all!

The alternative was to download a checklist created by other players, with a list of all planets you can visit or scan and what you can find on each one, checking off the list as you go. However, this spoiled the surprise - I didn't want to know what I could find where!

The planet tracker allows players to sign up for an account, and create a personal list of visited planets as they play through the game. The user can check off items they've discovered on each planet (like Asari Writings, Valuable Minerals, or Prothean Data Discs) without knowing they're there ahead of time. There is also a free text "Notes" section for any reminders or notes the user would like to write (for example, a reminder to revisit a planet, or complete a specific side quest).

The site is fully responsive, so users can play the game on desktop or console, and have their phone or tablet next to them open to the Planet Tracker while they play. 

## User Experience

### User Stories
As I began planning and ideating this project, I broke down the functionality of the project into Epics and User Stories as below:

**Epic: Account Management**

**User Stories**:
- As a **user** I can **sign up for an account** so that I can **track the planets I have visited**
- As a **user** I can **log in and out of my account** so that **I can access my 'visited planets' dashboard**
- As a **user** I can **set a profile photo** so that **I can customize my version of Commander Shepard to match the character in the game**
- As a **user** I can **request to reset my password via email** so that **I can log back in to my account if I don't remember my login details**
- As a **user** I can **delete my account** so that **my details are deleted when I have finished playing the game, or don't want to use the tracker anymore**
- As a **user** I can **update my email address or password** so that **I can keep my account secure and up to date**

**Epic: Managing the Planet Dashboard**

**User Stories**: 
- As a **user** I can **add a visited planet to my dashboard** so that **I can keep track of all planets and what I found there**
- As a **user** I can **edit my visited planets** so that **I can make changes as I make more discoveries, or fix mistakes**
- As a **user** I can **delete planets** so that **I can remove any planets I added by mistake, or that I may want to revisit**
- As a **user** I can **view my visited planet list** so that **I can see which planets I have visited and what I found there**
- As a **user** I can **see the percentage of planets I have visited at a glance** so that **I understand how much progress I have made in the game**
- As a **user** I can **upload an image to each planet's card** so that **I can customize my dashboard and record images of every planet I've visited**

**Epic: Admin Capabilities**

**User Stories**:
- As a **site admin** I can **track the number of users and the number of planets visited by each user** so that **I can share this information on the home page, and award progress badges to users**
- As a **site admin** I can **create and edit the list of planets users can choose from** so that **only planets from Mass Effect 1 can be added to users' dashboards**

**Epic: Rewards & Badges**

**User Stories**:
- As a **user** I can **win a badge when I visit a certain number of planets** so that **I feel a sense of accomplishment and progress as I add planets to my dashboard**
- As a **user** I can **see previous badges I have won** so that **I can look back at the progress I have made**
- As a **site admin** I can **award badges to users when they visit a certain number of planets** so that **users will feel accomplished and stay engaged with the site**
- As a **user** I can **see statistics on the home page that display how many users have visited 25%, 50%, 75%, and 100% of planets** so that **I can feel motivated and compare my own progress to other users'**

These user stories are being tracked using GitHub Projects, and tagged as either Must Have (features which the site requires in order to function), Should Have (features which the site should have in order to be fully functional, but could still run without), and Nice To Have (features which are not necessary for the functionality of the site, but would improve the user experience). See a screenshot below:

![User stories on GitHub Projects](static/readme/UserStoriesGithubProject.jpg)

### Wireframes
During the design stage of the project, I created wireframes for desktop, tablet, and mobile versions of the site:

- [Desktop](static/readme/WireframesDesktop.pdf)
- [Tablet](static/readme/WireframesTablet.pdf)
- [Mobile](static/readme/WireframesMobile.pdf)

### Entity Relationship Diagram
I have also created an Entity Relationship Diagram (ERD) showing the relationship between the Planets model (a custom model which stores all the information entered by the user relating to a specific planet on their dashboard) and the User model (imported from Django):

![ME1 Planet Tracker ERD](static/readme/ERD.jpeg)

## Features 

### Existing Features

- __Navigation Bar__

- __The Landing Page Image__

- __The Sign Up Page__


### Features Left to Implement

- Another feature idea

## Testing 

In this section, you need to convince the assessor that you have conducted enough testing to legitimately believe that the site works well. Essentially, in this part you will want to go over all of your project’s features and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

In addition, you should mention in this section how your project looks and works on different browsers and screen sizes.

You should also mention in this section any interesting bugs or problems you discovered during your testing, even if you haven't addressed them yet.

If this section grows too long, you may want to split it off into a separate file and link to it from here.


### Validator Testing 

- HTML
  - No errors were returned when passing through the official [W3C validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fcode-institute-org.github.io%2Flove-running-2.0%2Findex.html)
- CSS
  - No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fvalidator.w3.org%2Fnu%2F%3Fdoc%3Dhttps%253A%252F%252Fcode-institute-org.github.io%252Flove-running-2.0%252Findex.html&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#css)

### Unfixed Bugs

You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. 

## Deployment

This section should describe the process you went through to deploy the project to a hosting platform (e.g. GitHub) 

- The site was deployed to GitHub pages. The steps to deploy are as follows: 
  - In the GitHub repository, navigate to the Settings tab 
  - From the source section drop-down menu, select the Master Branch
  - Once the master branch has been selected, the page will be automatically refreshed with a detailed ribbon display to indicate the successful deployment. 

The live link can be found here - https://code-institute-org.github.io/love-running-2.0/index.html 


## Credits 

### Content 

- [Code Institute's Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as the starting workspace template for this project.
- [Code Institute's README Template](https://github.com/Code-Institute-Solutions/readme-template) was used to structure this README.
- [Balsamiq](https://balsamiq.com/) to create wireframes during the design phase.  
- [Lucidchart](https://lucid.app/) to create the Entity Relationship Diagram.

### Media


## Other General Project Advice

Below you will find a couple of extra tips that may be helpful when completing your project. Remember that each of these projects will become part of your final portfolio so it’s important to allow enough time to showcase your best work! 

- One of the most basic elements of keeping a healthy commit history is with the commit message. When getting started with your project, read through [this article](https://chris.beams.io/posts/git-commit/) by Chris Beams on How to Write  a Git Commit Message 
  - Make sure to keep the messages in the imperative mood 

- When naming the files in your project directory, make sure to consider meaningful naming of files, point to specific names and sections of content.
  - For example, instead of naming an image used ‘image1.png’ consider naming it ‘landing_page_img.png’. This will ensure that there are clear file paths kept. 

- Do some extra research on good and bad coding practices, there are a handful of useful articles to read, consider reviewing the following list when getting started:
  - [Writing Your Best Code](https://learn.shayhowe.com/html-css/writing-your-best-code/)
  - [HTML & CSS Coding Best Practices](https://medium.com/@inceptiondj.info/html-css-coding-best-practice-fadb9870a00f)
  - [Google HTML/CSS Style Guide](https://google.github.io/styleguide/htmlcssguide.html#General)

Getting started with your Portfolio Projects can be daunting, planning your project can make it a lot easier to tackle, take small steps to reach the final outcome and enjoy the process! 