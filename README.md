# FastAPI Books API

This is a **FastAPI-based application** that provides a RESTful API for managing books. The API supports CRUD operations for books, user authentication using JWT tokens, and real-time updates via Server-Sent Events (SSE).

## Features

- Full CRUD operations for managing books.
- User authentication with JWT tokens.
- Pagination support for retrieving books.
- Real-time updates using SSE.
- Automatically generated API documentation available at `/docs`.

## Deployment
The app is deployed on Heroku and can be accessed at:

```
https://fast-api-books-436e421e6217.herokuapp.com/
```

## API Endpoints

### **Authentication**

#### Register a User
- **Endpoint**: `POST /api/v1/register`
- **Description**: Register a new user and receive a JWT token.
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "password": "testpass123"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "<JWT_TOKEN>",
    "token_type": "bearer"
  }
  ```

#### Login for Token
- **Endpoint**: `POST /api/v1/token`
- **Description**: Authenticate and retrieve a JWT token.
- **Request Body**:
  ```json
  {
    "username": "testuser",
    "password": "testpass123"
  }
  ```
- **Response**:
  ```json
  {
    "access_token": "<JWT_TOKEN>",
    "token_type": "bearer"
  }
  ```

### **Books Management**

#### Create a Book
- **Endpoint**: `POST /api/v1/books`
- **Headers**: `Authorization: Bearer <JWT_TOKEN>`
- **Request Body**:
  ```json
  {
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_date": "1925-04-10",
    "summary": "A novel set in the Jazz Age.",
    "genre": "Classic"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_date": "1925-04-10",
    "summary": "A novel set in the Jazz Age.",
    "genre": "Classic"
  }
  ```

#### Retrieve All Books with Pagination
- **Endpoint**: `GET /api/v1/books`
- **Headers**: `Authorization: Bearer <JWT_TOKEN>`
- **Query Parameters**:
  - `page` (default: 1)
  - `size` (default: 10, max: 100)
- **Response**:
  ```json
  {
    "total": 1,
    "items": [
      {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "published_date": "1925-04-10",
        "summary": "A novel set in the Jazz Age.",
        "genre": "Classic"
      }
    ],
    "page": 1,
    "size": 10,
    "pages": 1
  }
  ```

#### Retrieve a Specific Book
- **Endpoint**: `GET /api/v1/books/{book_id}`
- **Headers**: `Authorization: Bearer <JWT_TOKEN>`
- **Response**:
  ```json
  {
    "id": 1,
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "published_date": "1925-04-10",
    "summary": "A novel set in the Jazz Age.",
    "genre": "Classic"
  }
  ```

#### Update a Book
- **Endpoint**: `PUT /api/v1/books/{book_id}`
- **Headers**: `Authorization: Bearer <JWT_TOKEN>`
- **Request Body**:
  ```json
  {
    "title": "The Great Gatsby Updated"
  }
  ```
- **Response**:
  ```json
  {
    "id": 1,
    "title": "The Great Gatsby Updated",
    "author": "F. Scott Fitzgerald",
    "published_date": "1925-04-10",
    "summary": "A novel set in the Jazz Age.",
    "genre": "Classic"
  }
  ```

#### Delete a Book
- **Endpoint**: `DELETE /api/v1/books/{book_id}`
- **Headers**: `Authorization: Bearer <JWT_TOKEN>`
- **Response**: `204 No Content`

### **Real-Time Updates**

#### Stream Updates
- **Endpoint**: `GET /api/v1/books/stream/updates`
- **Headers**: `Authorization: Bearer <JWT_TOKEN>`
- **Description**: Streams real-time updates using Server-Sent Events (SSE).
- **Response**:
  ```
  event: update
  data: {"timestamp": "2025-01-18T12:34:56.789123"}
  ```

---

## Testing the App

### **1. Swagger UI**
Visit the Swagger UI to interact with the API documentation:
```
https://fast-api-books-436e421e6217.herokuapp.com/docs
```

### **2. Testing with cURL**
Use the following cURL commands for testing:

- **Register a User**:
  ```bash
  curl -X POST https://fast-api-books-436e421e6217.herokuapp.com/api/v1/register \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "testpass123"}'
  ```

- **Login**:
  ```bash
  curl -X POST https://fast-api-books-436e421e6217.herokuapp.com/api/v1/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'username=testuser&password=testpass123'
  ```

### **3. Testing Data**
Use this sample JSON data for testing endpoints:
```json
{
  "title": "1984",
  "author": "George Orwell",
  "published_date": "1949-06-08",
  "summary": "A dystopian social science fiction novel and cautionary tale.",
  "genre": "Dystopian"
}
```

Let me know if you need further assistance or enhancements!
