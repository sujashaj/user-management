# User Management System

## Introduction

-	User management: Design a system that allows users to sign up, log in, and manage their profiles. Consider features like password hashing, email verification, and user roles (e.g., regular users, admins).
-	Use a relational database to store user information, such as username, email, hashed passwords, and user roles.
-	Implement user authentication using technologies like JSON Web Tokens (JWT) or OAuth.
-	Utilize encryption and secure storage practices for sensitive user data.

## User Password Handling

Libraries imported:
**hashlib**: Used for hashing passwords with the SHA-256 algorithm

- **User Representation**: Stores user details such as username, email, password, and verification status.
- **Password Encryption (SHA-256)**: Applies the SHA-256 encryption algorithm to passwords, converting them into a secure hashed format using the `hexdigest()` method. This method helps in securely transforming passwords into a unique series of characters, enhancing security.
- **Password Verification**: Compares the encrypted password provided by the user with the stored encrypted password, ensuring secure user authentication.

Libraries Imported:
- **SQLAlchemy**: Utilized for database interaction and ORM.
- **ORM Structure**: Utilizes SQLAlchemy to define the structure of the User class, mapping class attributes to database columns.
- **Attributes**: Includes username, email, password, and verification status as class attributes.

## User Registration

- **Functionality**: Enables user registration by creating a new user object with provided details.
- **Database Operations**: Checks for existing users, adds new users to the session, and commits changes upon successful registration.

- Libraries Imported:
- **SQLite3**: For interacting with the SQLite database.

## Login

- **Authentication**: Verifies user credentials by checking the user's existence, validating the provided password, and confirming the account's verification status. If successful, the user is authenticated.
- **Session Management**: After authentication, the database session is closed.
 
## Routes

- **Blueprint Setup**: Defines Flask routes for various functionalities like home, registration, login, and email verification.
- **Functionalities Overview**: Each route or path corresponds to a specific action:
  - **Home Page**: Renders a simple welcome message to users accessing the root path ("/").
  - **User Registration**: Processes POST requests to "/register_user" containing user details like username, email, and password in JSON format.
  - **User Login**: Manages GET requests to "/login" for user authentication with username and password as query parameters.
  - **Email Verification**: Deals with GET requests to "/verify_email" carrying a verification token as a query parameter, ensuring secure email verification for users.

## Token Manager

Libraries Imported:
- **jwt**: Handles JSON Web Tokens for token generation and verification.

- **Token Operations**: Generates verification tokens and verifies them using the JWT library.
- **Payload Creation**: Creates a payload with user information and an expiration time for token generation.
- **Token Verification**: Verifies token authenticity and extracts embedded user details.

## Mailjet Integration

Libraries Imported:
- **mailjet_rest**: Integrates with the Mailjet API for sending emails.
- **os**: Utilized for accessing environmental variables.

- **Mail Sending**: Utilizes Mailjet API to send emails.
- **Environmental Variables**: Uses environment variables like API_KEY, API_SECRET, SENDER_EMAIL, and SENDER_NAME for secure configurations.
- **Email Construction**: Constructs email content and sends it via the Mailjet API.







