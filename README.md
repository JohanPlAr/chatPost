# chatPost Social Network

![login page](documentation/features/home_page.png)

## About

The live website can be accessed by visiting this [link](https://chatPost.onrender.com).

This web application is a social network for groups of individuals who wish to share their knowledge and experiences. As admin you can choose the topics to set the discussions are expected. The app can be adjusted for family, friends, students or any other groups that wish to stay connected. The platform enables users to engage with each other by creating rooms, posts, commenting, and reacting to the content shared by others. By becoming friends you can restrict or allow access to your rooms.

## User Experience Design

### Strategy
The purpose of this application is to facilitate smooth and enjoyable communication. It is designed to enhance the user experience and encourage users to spend more time on the site.

### Target Audience
People who find the complexity of modern social media apps overwhelming and prefer a straightforward and user-friendly interface.

### User Stories

#### First Time Visitor Goals
- As a First Time Visitor, I want to quickly grasp the primary function of the app, so that I'm able to explore its features and learn more about it.
- As a First Time Visitor, I want an intuitive interface that, so that I can effortlessly navigate through the app and locate the presented content.
- As a First Time Visitor, I want the ability to create an account, so that I can unlock the app's full potential and allow me to experience its benefits as a user.
- As a First Time Visitor, I expect the app to be user-friendly and useful, so that I can cater my needs and preferences.

#### Frequent Visitor Goals
- As a Frequent User, I want to be able to log into my account, so that I can access my personalized content.
- As a Frequent User, I want to be able to easily navigate through the app, so that I can find the content without additional efforts.
- As a Frequent User, I want to be able to easily log in and log out, so that I can access my personal account information.
- As a Frequent User, I want to be able to update my personal data, so that I can keep my account up to date.
- As a Frequent User, I want to be able to update my avatar, so that I can keep my avatar up to date.
- As a Frequent User, I want to be able to add friends, so that I can communicate with my friends.
- As a Frequent User, I want to be able to delete friends, so that I can feel safe in this social network.
- As a Frequent User, I want to be able to easily navigate through the app, so that I can find the content without additional efforts.
- As a Frequent User, I want to be able to easily log in and log out, so that I can access my personal account information.
- As a Frequent User, I want to be able to update my personal data, so that I can keep my account up to date.
- As a Frequent User, I want to be able to update my avatar, so that I can keep my avatar up to date.
- As a Frequent User, I want to be able to add friends, so that I can communicate with my friends.
- As a Frequent User, I want to be able to delete friends, so that I can feel safe in this social network.
- As a Frequent User, I want to be able to search through the users of the social network, so that I can find people who I am interested in.
- As a Frequent User, I want to be able to search people by their names, so that I can find people who I know.
- As a Frequent User, I want to be able to create my own discussion rooms, so that I can create the conversations that I want.
- As a Frequent User, I want to be able to browse other discussion rooms, so that I can participate in the conversations that I want.
- As a Frequent User, I want to be able to delete the discussion rooms that I created, so that I can remove my community from the app.
- As a Frequent User, I want to be able to add a new post on my page or my friends' pages, so that I can share my knowledge and experiences with others.
- As a Frequent User, I want to be able to add a new comment on my post, so that I can share my knowledge and experiences with others.
- As a Frequent User, I want to be able to add a new comment to other people's post, so that I can share my knowledge and experiences with others.
- As a Frequent User, I want to be able to react to my post, so that I can share my knowledge and experiences with others.
- As a Frequent User, I want to be able to react to other people's post, so that I can share my knowledge and experiences with others.
- As a Frequent User, I want to be able to be able to edit/delete my posts, so that I can change my knowledge and experiences.
- As a Frequent User, I want to be able to share my experiences with other users, so that I can share my knowledge and experiences with others.

## Technologies used
- ### Languages:
    + [Python](https://www.python.org/downloads/release/python-385/): the primary language used to develop the server-side of the website.
    + [JS](https://www.javascript.com/): the primary language used to develop interactive components of the website.
    + [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML): the markup language used to create the website.
    + [CSS](https://developer.mozilla.org/en-US/docs/Web/css): the styling language used to style the website.
- ### Frameworks and libraries:
    + [Django](https://www.djangoproject.com/): python framework used to create all the backend logic of the website.

- ### Databases:
    + [SQLite](https://www.sqlite.org/): was used as a database during the development stage of the website.
    + [PostgreSQL](https://www.postgresql.org/): the database used to store all the data.
- ### Other tools:
    + [Github Projects and kanban boards](https://github.com/lexach91/Django-social-network-PP4/projects) was used to track the progress of the project in general and of every application in the project.
    + [Git](https://git-scm.com/): the version control system used to manage the code.
    + [Pip3](https://pypi.org/project/pip/): the package manager used to install the dependencies.
    + [ElephantSQL](https://www.elephantsql.com/docs/index.html): the webserver used to run the website.
    + [Cloudinary](https://cloudinary.com/): the image hosting service used to upload images and other media.
    + [Psycopg2](https://www.python.org/dev/peps/pep-0249/): the database driver used to connect to the database.
    + [Django-allauth](https://django-allauth.readthedocs.io/en/latest/): the authentication library used to create the user accounts.
    + [Render](https://render.com/): the hosting service used to deploy the website.
    + [GitHub](https://github.com/): used to host the website's source code.
    + [VSCode](https://code.visualstudio.com/): the IDE used to develop the website.
    + [Chrome DevTools](https://developer.chrome.com/docs/devtools/open/): was used to debug the website.
    + [Bootstrap](https://bootstrap.com/): .
    + [W3C Validator](https://validator.w3.org/): was used to validate HTML5 code for the website.
    + [W3C CSS validator](https://jigsaw.w3.org/css-validator/): was used to validate CSS code for the website.
    + [JShint](https://jshint.com/): was used to validate JS code for the website.
    + [PEP8](https://pep8.org/): was used to validate Python code for the website.


## Features


**Log in Page**


When the user is logged out, the website will redirect the home page and display the login view with Username and password fields Clicking the sign up link will display the Sign Up Page.

![Home page](documentation/features/log_in_page.png)

**Sign Up Page**

Sign up page has a box for the user to enter their username, password and password confirmation. After the user clicks the sign up button.

![Sign up page](documentation/features/sign_up_page.png)

**Home Page/Logged in User**

When the user enters the correct username/email and password succes message will be displayed and redirects to home page. Home Page contains a list of rooms whith room-details.
- Host
- Room Name
- Access: Public/Friendsonly
- Topic
- Number of Posts
- Edit/Delete buttons: If User is Room Host

![Home page](documentation/features/signed_in_home_page.png)


**Navbar/Sidebar**

Navbar/Navbar Tablet/Navbar Mobile

![Navbar](documentation/features/navbar.png)![Navbar_tablet](documentation/features/navbar_tablet.png)![Navbar_Mobile](documentation/features/navbar_mobile.png)

Navbar is located on the left side of the screen and has the following buttons. For the mobile and Tablet versions, the navbar will be also on the left side of the screen but will show only icons.:

- Logo and Home button, leads to the home.html page showing all rooms.
![Navbar Logo and Home](documentation/features/navbar_logo_home.png)
- Topics button, which will drop down a menu containing the topics chosen by the admin.
![Navbar Topics](documentation/features/navbar_topics.png)
- Your Rooms button, which will drop down a list of the rooms hosted by logged in user.
![Navbar Your Rooms](documentation/features/navbar_your_rooms.png)
- Friends button, which leads to the Friends list page.
![Navbar Friends List](documentation/features/navbar_friends_list.png)
- Profile button, which will expand a menu with Logout, Manage Profile or View Profile.
![Navbar Profile Menu](documentation/features/navbar_profile_menu.png)


**Manage Profile Page**
This page has a main container with the input choices of the profile details. Allows the user to share their profile with friends.
- Avatar
- Bio
- First Name
- Last Name
- Email
- Save Button

![Manage Profile page](documentation/features/manage_profile_page.png)

**Profile Page**
This page has a main container in which the user can see their profile information.

![Profile page](documentation/features/profile_page.png)

**Friends List Page**
![Friends page](documentation/features/profile_page.png)

This page displays the following features:
- Search User Bar - allows logged in user to search all registered users by Username
- Number of friends counter
- List of friends
    - Avatar
    - View profile button
    - Remove friend button
- Pending requests list
    - Avatar
    - View profile button
    - Remove friend request button

**Room page**

![Create Room](documentation/features/room_page_create.png)

Clicking on the create room button found on the homepage displays the create room view.
The view contains a card with following inputs:
- Name 
- Topic
- Description
- Access - Public or Friends Only

Topics are set by admin and and must be chosen for each room created. 
Description allows the user to describe the purpose of the room.
Access are either public or friends only.

![Room](documentation/features/room_page.png)
When user has access to the room - either the room is public or the user is allowed as a friend of the host. Following features are displayed:
- Room Name
- Access
- Room Host
    - Avatar
    - Host Username
- Room Description
- List of Posts
- Contributors (right sidebar)

![Posts container](documentation/features/wall_posts.png)

Each post has author's name, how long ago the post was made, and the post itself with Image and statistics. if the user is online, the user will see the following:

![Post](documentation/features/user_online.png)

The statistics consist of the number of likes, comments, and dislikes.

![Post](documentation/features/post_statistics.png)

If the user clicks on the comments icon, the comments will be displayed if there are any.

![Post](documentation/features/post_wall_comments_all.png)

if the user wants to add comments to the post, the user will see the following:

![Comment](documentation/features/post_wall_comments_all.png)
Each comment has author's name, how long ago the comment was made, and the statistics of likes/dislikes. If comment was created by logged in user an edit and a delete button are displayed.

**Footer**

At the bottom of each page below the fold, the user can see a the name of the coder and links to the coder's email, linkedin, and github.
![Footer](documentation/features/footer.png)

**404 Error Page**

This page is shown when the user tries to access a page that doesn't exist.
It may contain a navbar if the user is logged in.

![404 error page](documentation/features/error_page_404_logged_in.png)

Or just an error message if the user is not logged in.

![404 error page](documentation/features/error_page_404.png)

**500 Error Page**

This page is shown when the server is not able to process the request.

![500 error page](documentation/features/error_page_500.png)

---

## Future Improvements and Features

**Sign-up and Login options**

- Add sign-up and login with Facebook, Google, and other social media platforms.
- Add e-mail confirmation and reset password options to improve security.
- Also, I would like to add an option to use a phone number instead of an email and send a verification code to the user's phone.

**Chat-functionality**

- Let users that are online chat in a chat-window using websocket technology.

**Full asynchronous functionality**

In the future I would like to make the application fully asynchronous. So all elements in the frontend will be updated real-time as soon as the backend sends the data.

**Security improvements**

In the future I would like to make the application foolproof against attacks and security vulnerabilities.

**User settings**

In the future I would like to more customization options for the user.

**Group chatting**

In the future I would like to add group chatting for friends.

**Moderation**

In the future I would like to add host moderation options.

---

## Design

The design of the application is based on the Material Design principles.
The central theme of the application is the simplicity of use. It was aimed to guide the user to the best experience.

### Color Scheme

The color scheme of the application is based on the primary colors of Bootstrap library:

  ![Color Scheme](documentation/design/color_palette.png)

The decision to use this color palette was made due to the trend in the modern web design.


### Typography

The main font used in the application is Roboto. The use of this font is consistent with the color scheme. Needless to say, the Segoe UI was chosen due to its readability, which increases user experience.

  ![Typography](documentation/design/Roboto.png)



- The main part is allocated to the use of icons from the [Bootstrap Icons](https://icons.getbootstrap.com/) website. The use of icons is essential for the user experience when it comes to multifunctional websites.


### Wireframes

- [Wireframes can be accessed here](documentation/design/wireframes.pdf).

---

## Information Architecture

### Database

* During the earliest stages of the project, the database was created using SQLite.
* The database was then migrated to PostgreSQL.

### Data Modeling

**Entity relationship diagram**

![Entity relationship diagram](documentation/design/entity_relational_diagram.png)

1. **Allauth User Model**
    - The user model was created using [Django-allauth](https://django-allauth.readthedocs.io/en/latest/).
    - The user model was then migrated to PostgreSQL.

2. **Profile Model**

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| User          | user          | OneToOneField | User, on_delete=models.CASCADE, related_name='profile'    |
| First Name    | first_name    | CharField    | max_length=25, null=True, blank=True      |
| Last Name     | last_name     | CharField    | max_length=25, null=True, blank=True      |
| Bio           | bio           | TextField    | max_length=100, null=True, blank=True      |
| Avatar        | avatar        | CloudinaryField    | folder='avatars', null=True, blank=True      |

3. **Room Model**

STATUS = ((0, "Public"),(1, "Friends Only"))

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| host          | host          | ForeignKey    | User, on_delete=models.CASCADE|
| topic        | topic        | ForeignKey    | Topic, on_delete=models.CASCADE|
| name       | name | TextField    |   max_length=50 |
| description      |	description | TextField | null=True, max_length=150, blank=True |
| status    | status | IntegerField | choices=STATUS, default=0 |
| participants  | participants| ManyToManyField | User, related_name='participants', blank=True|
| updated  |updated| DateTimeField | auto_now=True    |
| created  | created| DateTimeField | auto_now_add=True    |

4. **Post Model**

STATUS = ((0, "Draft"),(1, "Published"))

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| author          | author          | ForeignKey    | User, on_delete=models.CASCADE, related_name='posts'    |
| room        | room        | ForeignKey    | Room, on_delete=models.CASCADE, related_name='post_room'    |
| content       | content | TextField    |   max_length=550 |
| edited      |	edited | BooleanField | default=False      |
| image    | image| CloudinaryField | 'post-image default='https://res.cloudinary.com/ddurovnhl/image/upload/v1700729202/samples/l83wf54aeup6jmn0xbou.png' |
| created  | created| DateTimeField | auto_now_add=True    |
| updated  |updated| DateTimeField | auto_now=True    |
| status  | status| IntegerField | choices=STATUS, default=0    |
| likes  | likes| ManyToMany | User, related_name="post_like", blank= True    |
| dislikes  | dislikes | ManyToMany| User, related_name="post_dislike", blank= True  |

5. **Comment Model**

STATUS = ((0, "Draft"),(1, "Published"))

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| author          | author          | ForeignKey    | User, on_delete=models.CASCADE, related_name='commentsAuthor'    |
| post        | post        | ForeignKey    | Room, on_delete=models.CASCADE, related_name='commentsPost'    |
| content       | content | TextField    |   max_length=550 |
| edited      |	edited | BooleanField | default=False      |
| created  | created| DateTimeField | auto_now_add=True    |
| updated  |updated| DateTimeField | auto_now=True    |
| status  | status| IntegerField | choices=STATUS, default=0    |
| likes  | likes| ManyToMany | User, related_name="post_like", blank= True    |
| dislikes  | dislikes | ManyToMany| User, related_name="post_dislike", blank= True  |

5. **Friend request Model**

STATUS = ((0, "Pending"),(1, "Accepted"))

| Name          | Database Key  | Field Type    | Validation |
| ------------- | ------------- | ------------- | ---------- |
| sender          | sender          | ForeignKey    | User, on_delete=models.CASCADE, related_name='outgoing_friend_request'    |
| receiver          | receiver          | ForeignKey    | User, on_delete=models.CASCADE, related_name='incoming_friend_request'    |
| status  | status| IntegerField | choices=STATUS|

---
## Testing
Please refer to the [TESTING.md](TESTING.md) file for all test-related documentation.
---
## Deployment
