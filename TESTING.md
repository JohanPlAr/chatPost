# Testing

## Manual Testing

Testing was done throughout site development, for each feature before it was merged into the master file.

Usability was tested with the below user acceptance testing, sent to new users to ensure testing from different users, on different devices and browsers to ensure issues were caught and where possible fixed during development.


|     | User Actions           | Expected Results | Y/N | Comments    |
|-------------|------------------------|------------------|------|-------------|
| Sign Up     |                        |                  |      |             |
| 1           | Click on Sign Up button | Redirection to Sign Up page | Y |          |
| 2           | Click on the Login link in the form | Redirection to Login page | Y |          |
| 3           | Enter valid Username | Field will only accept a unique username and will be stored in lowercase | Y |          |
| 4          | Enter valid password | Field will only accept secure passwords | Y |          |
| 5          | Enter valid password confirmation | Field will only accept the same password from the previous field | Y | |
| 6          | Click on the Sign Up button | If username and password is valid a success message displays and takes user to all rooms home page| Y |          |
| 7          | Sign In with the same email/username and password | Displays success message - Takes user to all rooms home page  | Y | |
| 8       | Click "Logout" in the profile menu | Logs out user and redirects to All Rooms List Home Page | Y |          |
| 9          | Click browser back button | You are still logged out | Y |          |
| Log In      |                        |                  |      |             |
| 1           | Click on Login button | Redirection to Login page | Y |          |
| 3           | Click on the SignUp link in the form | Redirection to SignUp page | Y |          |
| 4           | Enter valid username | Field is agnostic to lower/uppercase - all usernames are stored in lowercase| Y |          |
| 5           | Enter valid password | Field will only accept secure passwords | Y |          |
| 6           | Click on the Sign In button | If username and password is valid a success message displays and takes user to All Rooms List Home Page | Y |          |
page | Y |          |
| 8           | Click "Logout" in the navbar profile-menu | Logs out user - displays a success message - redirects all rooms home page | Y |          |
| 9          | Click browser back button | You are still logged out | Y |          |
| Navbar     |                        |                  |      |             |
| 1          | Click "Logo" in the navbar | Redirects user to all rooms home page | Y |          |
| 2          | Click "Login" in the navbar | Redirects user to Login/Signup page | Y |          |
| 3          | Click "Home Icon" in the navbar | Redirects user to All Rooms List Home Page | Y |          |
| 4          | Click "Topics Icon" in the navbar | Displays topics menu in navbar | Y |          |
| 5          | Click "Topic List Item" in the navbar | Takes user to Topic Room List page with requested search results| Y |          |
| 6          | Click "Your Rooms Icon" in the navbar | Displays Your Rooms List Menu in Navbar | Y |          |
| 7          | Click "Your Rooms List Item" in the navbar | Takes user to room page| Y |          |
 Y |          |
| 8          | Click "Your Rooms List Item" in the navbar | Takes user to room page| Y |          |
 Y |          |
| 9          | Click "Friends Icon" in the navbar | Takes user Friends List Page| Y |          |
 Y |          |
| 10          | Click "User Avatar" in the navbar | Displays Profile Menu in Navbar| Y |          |
 Y |          |
| 11          | Click "Manage Profile" in the navbar | Redirects User to Edit Profile Page| Y |          |
| 12          | Click "View Profile" in the navbar | Redirects User to Profile Page| Y |          |
 Y |          |
| 13          | Click "Logout" in the navbar | Logs out User - displays success message - redirects to All Rooms Home Page| Y |          |
 Y |          |
| Rooms     |                        |                  |      |             |
| 1          | Enter "Search Rooms" in the Search Field | Redirects user to Search Result Rooms page | Y |          |
| 2          | Click "Create Room Button" | Redirects user to Create Room Form Page | Y |          |
