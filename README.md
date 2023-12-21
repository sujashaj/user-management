# User Management System

## Introduction

![image](https://gist.github.com/assets/135242046/eeb1fba4-41be-4b39-bd00-0b558eb5a35a)
- User management: Design a system that allows users to sign up and log in. 
- Consider features like password hashing for data protection, email verification to ensure user authenticity,the incorporation of Mailjet services to send verification links for user verification process and structured routing ('/signup', '/login') to manage user interactions effectively.
- Use a relational database to store user information, such as username, email, and hashed passwords.
- Implement user authentication using technologies like JSON Web Tokens (JWT).

## User Registration

### Supported Features

### User Creation

Libraries Imported:
- **SQLAlchemy**: Utilized for database interaction and ORM.
- **ORM Structure**: Utilizes SQLAlchemy to define the structure of the User class, mapping class attributes to database columns.
- - **SQLite3**: For interacting with the SQLite database.

- SQL Lite is easy to use, self-contained, lightweight and doesn't require a separate server process

- The user provides details like username, email, and password during registration, the system checks these details to ensure they are valid and unique.
- If everything is in order, this information is securely stored in the database. 
- If the username or email is already taken, it returns a message indicating the unavailability of credentials.


### User Password Handling

Libraries imported:
**hashlib**: Used for hashing passwords with the SHA-256 algorithm

- When a user registers, their password undergoes a process known as hashing. 
- It uses the SHA-256 (Secure Hash Algorithm 256) method for hashing.
- The hashed password is returned in a secure format using the hexdigest() method.

### Token Generation

Libraries Imported:
- **jwt**: Handles JSON Web Tokens for token generation and verification.

- Once the user's account is successfully created, the system generates a special code called a verification token. 
- This token is unique to each user and is used to confirm their email address. 
- Based on the information within the token, the system determines whether the user is authorized to access .
- Token contains information about a user, such as their username, along with an expiration time.
- The token is created by encoding this payload using secret_key and the HS256 (HMAC with SHA-256) algorithm. 
- The secret key is a confidential piece of information known only to the system.

### Mailjet Integration

Libraries Imported:
- **mailjet_rest**: Integrates with the Mailjet API for sending emails.
- **os**: Utilized for accessing environmental variables.
- **Environmental Variables**: Uses environment variables like API_KEY, API_SECRET, SENDER_EMAIL, and SENDER_NAME for secure configurations.

- When a user signs up, the system sends an email via Mailjet to the user's provided email address. 
- This email contains verification token. 
- Clicking on this link ,confirms the user's email, allowing them to complete the registration process securely.
- The email serves as a verification step, ensuring that the user's email is valid.

## Email Verification

- When a user clicks on the link from email, it triggers a process to check if the link is valid and to get important information from it. 
- Firstly, the system decodes this token using a secret key and HS256 algorithm.
- It then retrieves the username and expiration time from the payload. 
- Subsequently, it utilizes this username to match it against stored user record.
- If the user is successfully identified, the system proceeds with access authorization.

## User Login

- It checks if the user exists in the database.
- If the user is found, it verifies the provided password against the stored hashed password
- If the password is correct and the account is verified, the user is authorized to login.

## Routes

- **Blueprint Setup**: Defines Flask routes for various functionalities like home, registration, login, and email verification.
- **Functionalities Overview**: Each route or path corresponds to a specific action:
  - **Home Page**: Renders a simple welcome message to users accessing the root path ("/").
  - **User Registration**: Processes POST requests to "/register_user" containing user details like username, email, and password in JSON format.
  - **User Login**: Manages GET requests to "/login" for user authentication with username and password as query parameters.
  - **Email Verification**: Deals with GET requests to "/verify_email" carrying a verification token as a query parameter, ensuring secure email verification for users.











