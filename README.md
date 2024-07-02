# Rule34 API

A Python wrapper for the Rule34 API, supporting both synchronous and asynchronous requests.

## Installation

Install the package using pip:

```bash
$ python3 -m pip install git+https://github.com/cardisnotvalid/rule34-api.git
```

## Usage

### Synchronous Usage

```python
from rule34 import Rule34

# Initialize the client
r34 = Rule34()

# Get a random post
random_post = r34.get_random_post()
print(random_post)

# Search for posts with specific tags
posts = r34.search("python")
print(posts)

# Get a specific post by its ID
post = r34.get_post(12345678)
print(post)

# Get comments for a specific post by its ID
comments = r34.get_comments(12345678)
print(comments)
```

### Asynchronous Usage

```python
import asyncio
from rule34 import AsyncRule34

async def main() -> None:
    # Initialize the asynchronous client
    r34 = AsyncRule34()

    # Get a random post
    random_post = await r34.get_random_post()
    print(random_post)

    # Search for posts with specific tags
    posts = await r34.search("python")
    print(posts)

    # Get a specific post by its ID
    post = await r34.get_post(12345678)
    print(post)

    # Get comments for a specific post by its ID
    comments = await r34.get_comments(12345678)
    print(comments)

asyncio.run(main())
```

## Using Context Managers

The `Rule34` and `AsyncRule34` classes support context managers for automatic resource management.

### Synchronous Context Manager

```python
from rule34 import Rule34

# Using a context manager
with Rule34() as r34:
    random_post = r34.get_random_post()
    print(random_post)
```

### Asynchronous Context Manager

```python
import asyncio
from rule34 import AsyncRule34

async def main() -> None:
    # Using an asynchronous context manager
    async with AsyncRule34() as r34:
        random_post = await r34.get_random_post()
        print(random_post)

asyncio.run(main())
```

### Manual Resource Management

If you prefer not to use context managers, ensure proper resource management by manually closing the client.

#### Synchronous

```python
from rule34 import Rule34

r34 = Rule34()
try:
    random_post = r34.get_random_post()
    print(random_post)
finally:
    r34.close()
```

#### Asynchronous

```python
import asyncio
from rule34 import AsyncRule34

async def main() -> None:
    r34 = AsyncRule34()
    try:
        random_post = await r34.get_random_post()
        print(random_post)
    finally:
        await r34.close()

asyncio.run(main())
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
