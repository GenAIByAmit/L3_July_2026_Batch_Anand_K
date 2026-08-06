from fastmcp import FastMCP

mcp = FastMCP("Shopping MCP Server")

books = [
    {"id": "1", "title": "Panch tantra", "price": 100},
    {"id": "2", "title": "Socialism", "price": 150},
    {"id": "3", "title": "The Story of My Life", "price": 50},
    {"id": "4", "title": "Malgudi Days", "price": 200},
    {"id": "5", "title": "The God of Small Things", "price": 500}
]

@mcp.prompt
def get_book_price_prompt(book_name: str):
    """
    This prompt is used to get the price of a book given its name.
    """
    return f"What is the price of the book '{book_name}'?"

@mcp.tool
def get_all_books():
    return books

@mcp.resource("book://{book_id}")
def get_book(book_id: str):
    for book in books:
        if book["id"] == book_id:
            return book
    return {"error": "Book not found"}

@mcp.tool
def get_book_price(book_name: str):
    for book in books:
        if book["title"] == book_name:
            return {"price": book["price"]}
    return {"error": "Book not found"}

if __name__ == "__main__":
    mcp.run(transport="http", port=8000) #default protocol is shttp
