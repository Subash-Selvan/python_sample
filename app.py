from fastapi import FastAPI

app = FastAPI()

# Sample data (to simulate a database)
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Data Science Essentials", "author": "Jane Smith"},
]

# Define routes
@app.get("/books")
async def get_books():
    return books

@app.get("/books/{book_id}")
async def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@app.post("/books")
async def add_book(title: str, author: str):
    book_id = max(book["id"] for book in books) + 1
    new_book = {"id": book_id, "title": title, "author": author}
    books.append(new_book)
    return new_book

@app.put("/books/{book_id}")
async def update_book(book_id: int, title: str, author: str):
    for book in books:
        if book["id"] == book_id:
            book["title"] = title
            book["author"] = author
            return {"message": "Book updated successfully"}
    return {"error": "Book not found"}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    global books
    initial_length = len(books)
    books = [book for book in books if book["id"] != book_id]
    if initial_length == len(books):
        return {"error": "Book not found"}
    return {"message": "Book deleted successfully"}
