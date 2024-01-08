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
| Rooms Page    |                        |                  |      |             |
| 1          | Enter "Search Rooms" in the Search Field | Redirects user to Search Result Rooms page | Y |          |
| 2          | Click "Create Room Button" | Redirects user to Create Room Form Page | Y |          |
| 3          | Click "Room Host Avatar or @name link" | Redirects user to Host Profile Page | Y |          |
| 4          | Click "Room Name Link" | Redirects user to Room Page | Y |          |
| 5          | Click "Edit Room Link" | Redirects user to Edit Room Page | Y |          |
| 6          | Click "Delete Room Link" | Redirects user to Confirm Delete Page | Y |          |
| Create Room Page     |                        |                  |      |             |
| 1          | Enter "Name Field" | Takes User Text input in field | Y |          |
| 2          | Select "Topic Field" | Lets User Select Rooms Topic | Y |          |
| 3          | Enter "Description Field" | Takes User Text Input in Text field | Y |          |
| 4          | Select "Access Field" | Lets User Select Public or Friends Only | Y |          |
| 5          | Click "Go Back Button" | User redirected to previous page without submitting form | Y |          |
| 6          | Click "Submit Button" | Room is created - succes message is displayed - user is redirected to new room page| Y |          |

| Room Page     |                        |                  |      |             |
| 1          | Enter "Search Rooms" in the Search Field | Redirects user to Search Result Rooms page | Y |          |
| 2          | Click "Create Post Button" | Redirects user to Create Post Form Page | Y |          |
| 3          | Click "Host Avatar" | Redirects user to Profile Page | Y |          |
| 4          | Click "Comment Icon" | Drops down comment Form | Y |          |
| 5          | Click "Send Button" | Submits a Comment Form and reloads the page with updated comment and scrolls back to previous position | Y |          |
| 6          | Click "Like Post Icon" | Reloads page with updated Like Post Count | Y |          |
| 7          | Click "Dislike Post Icon" | Reloads page with updated Dislike Post Count | Y |          |
| 8          | Click "Like Comment Icon" | Reloads page with updated Like Comment Count | Y |          |
| 9          | Click "Dislike Comment Icon" | Reloads page with updated Dislike Comment Count | Y |          |
| Create Post Page     |                        |                  |      |             |
| 1          | Enter "Content Field" | Takes User Text input in field | Y |          |
| 2          | Click "Choose Image Button" | Lets User Select Post Image | Y |          |
| 3          | Click "Go Back Button" | User redirected to previous page without submitting form | Y |          |
| 5          | Click "Submit Button" | Submits a Post Form and redirects the user to the Room Page | Y |          |
| Friends List Page  |                        |                  |      |             |
| 1          | Enter "Search Users" in the Search Field | Reloads page with search results | Y |          |
| 2          | Click "Avatar" in Search results| Redirects User to user profile page of clicked user| Y |          |
| 3          | Click "View Profile Button" in Friends List| Redirects User to user profile page of clicked user| Y |          |
| 4          | Click "Remove Button" in Friends List| Redirects User to the Confirm Delete Page| Y |          |
| 5          | Click "View Profile Button" in Pending List| Redirects User to user profile page of clicked user| Y |          |
| 6          | Click "Remove Button" in Pending List| Redirects User to the Confirm Delete Page| Y |          |
| Profile Page  |                        |                  |      |             |
| 1          | Click "Remove Button" | Redirects User to the Confirm Delete Page | Y |          |
| 2          | Click "Friends List Button" | Redirects User to the Friends List Page | Y |          |
| Non Friend Profile Page  |                        |                  |      |             |
| 1          | Click "Friend Request Button" | Sends a Friend Request - Request is displayed under the Pending Request List of both users - Redirects to Friendslist| Y |          |
| 2          | Click "Friends List Button" | Redirects User to the Friends List Page | Y |          |
| Confirm Delete Page  |                        |                  |      |             |
| 1          | Click "Go Back Button"| Redirects User Back to Previous Page | Y |          |
| 2          | Click "Confirm Button"| Deletes the Instance - Redirects User Back to Previous Page | Y |          |




