## Book Tracker: A Django ORM Practice Project 📚
This project is a simple web application built with Django, specifically designed for new developers to master the fundamentals and advanced techniques of the Django ORM in a practical, non-shell environment.It allows users to track books and authors, providing hands-on experience with core database interactions.

## Key Learning Objectives (ORM Focus)The primary goal of this project is to implement and understand the following ORM concepts:
1. CRUD Operations: Creating, Retrieving, Updating, and Deleting objects (Authors and Books).
2. Field Lookups (__icontains, __year): Implementing search and advanced filtering.
3. Relationships (Foreign Keys): Querying across related models (e.g., getting all books by a specific author).
4. Performance Optimization: Using $select\_related() and $prefetch\_related() to solve the N+1 query problem.
5. Aggregation & Annotation: Calculating statistics like total books, average publication year, and counting comments per book using $Count(), $Avg(), and `$Annotate()$.

## Models OverviewThe application is structured around two primary models:
1. Author: Stores author details (name, bio).
2. Book: Stores book details (title, publication_year, $ForeignKey$ to Author, and status - Read/Reading/Want to Read).
