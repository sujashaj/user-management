# User Management System

## Problem Statement

- Design a user management system that allows users to sign up and log in. 
- Consider features like password hashing for data protection, email verification to ensure user authenticity, the incorporation of Mailjet services to send verification links for user verification process and structured routing ('/signup', '/login') to manage user interactions effectively.
- Implement email authentication using technologies like JSON Web Tokens (JWT).
- Use a relational database to store user information, such as username, email, and hashed passwords.

## High Level Design

### 1. User Registration

![image](https://github.com/sujashaj/user-management/blob/resources/images/user_management_edited.jpg)

  - The user provides details like username, email, and password during registration, the system checks these details to ensure they are valid and unique.
  - If everything is in order, this information is securely stored in the database. 
  - The system further sends an email via Mailjet to the user's provided email address for verification.
  - If the username or email is already taken, it returns a message indicating its unavailability.

### 2. Email Verification

![email_verification_component_diagram](https://github.com/sujashaj/user-management/blob/resources/images/email_verification_component_diagram.jpg))

  - When a user signs up, the verification email sent to the user's email address contains a link with a JWT token. 
  - When a user clicks on the link from email, it triggers a process to check if the token in the link is valid.
  - Firstly, the system decodes this token using a secret key and HS256 algorithm.
  - It then retrieves the username and expiration time from the payload. 
  - Subsequently, it utilizes this username to match it against stored user record.
  - If the user is successfully identified, the system proceeds with access authorization.
  - The user's email is then marked as verified in the database.

### 3. User Login

![login_component_diagram(1)](https://github.com/sujashaj/user-management/blob/resources/images/login_component_diagram.jpg)

  - In the login flow, user enters the username and password and submits a post request to the login API. 
  - The system checks if the user exists in the database.
  - If the user is found, it verifies the provided password against the stored hashed password
  - If the password is correct and the account is verified, the user is authorized to login.

## Technologies Used

### 1. User Creation

 - **SQLAlchemy**: Utilizes SQLAlchemy to define the structure of the User class, mapping class attributes to database columns.
 - **SQLite3**: For interacting with the SQLite database. SQL Lite is easy to use, self-contained, lightweight and doesn't require a separate server process

### 2. User Password Handling

 - **hashlib**: Used for hashing passwords with the SHA-256 (Secure Hash Algorithm 256) algorithm

### 3. Token Generation

 - **jwt**: Handles generation and verification of JSON Web Tokens.
 - Once the user's account is successfully created, the system generates a special code called a verification token. 
 - This token is unique to each user and is used to confirm their email address. 
 - The token payload contains information about a user, such as their username, along with an expiration time. 
 - The token is created by encoding this payload using secret_key and the HS256 (HMAC with SHA-256) algorithm. 
 - The secret key is a confidential piece of information known only to the system.
 - Based on the information within the token, the system determines whether the user is authorized to access .


### 4. Mailjet Integration

 - **mailjet_rest**: Integrates with the Mailjet API for sending emails.
 - **os**: Utilized for accessing environmental variables.
 - **Environmental Variables**: Uses environment variables like API_KEY, API_SECRET, SENDER_EMAIL, and SENDER_NAME for secure configurations.

## Routes

 - **Blueprint Setup**: Defines Flask routes for various functionalities like home, registration, login, and email verification.
 -**Functionalities Overview**: Each route or path corresponds to a specific action:
    - **Home Page**: Renders a simple welcome message to users accessing the root path ("/").
    - **User Registration**: Processes POST requests to "/register_user" containing user details like username, email, and password in JSON format.
    - **User Login**: Manages GET requests to "/login" for user authentication with username and password as query parameters.
    - **Email Verification**: Deals with GET requests to "/verify_email" carrying a verification token as a query parameter, ensuring secure email verification for users.

## Running application

1. Set up environment variables - API key and secret for mailjet server, sender email and name for email verification, app secret key to generate and verify JWT token 
```
export API_KEY=<API_KEY>
export API_SECRET=<API_SECRET>
export SENDER_EMAIL=<SENDER_EMAIL>
export SENDER_NAME=<SENDER_NAME>
export APP_SECRET_KEY=<APP_SECRET_KEY>
```

2. Start flask server
```
python3 app.py
```













