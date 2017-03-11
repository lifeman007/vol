# Endpoints

An overview of the Open Library internal API.

- [Lists](#lists)
  - [Creating Lists](#creating-lists)
  - [Searching for Lists](#searching-for-lists)
- [Works](#works)
- [Editions](#editions)
- [Subjects](#subjects)


## Lists

### Creating Lists

### Addings Seeds to Lists

### Searching for Lists

In openlibrary/plugins/openlibrary/lists.py

    GET /lists/search?q=




## Works

### Creating Works

### Delete

In file openlibrary/plugins/upstream/addbook.py:

   https://openlibrary.org/books/(OL...M)/edit

Parameters:

   name="_delete"

Permissions:

User must be Administrator

## Editions

### Create

### Edit

### Merge

### Delete

In file openlibrary/plugins/upstream/addbook.py:

   https://openlibrary.org/books/(OL...M)/edit

Parameters:

   name="_delete"

Permissions:

User must be Administrator