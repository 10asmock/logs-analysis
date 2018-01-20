#! /usr/bin/env python3
"""An internal reporting tool which uses stored information as views
on a database to discover most popular articles, authors, and an error 
log from a news site.

The tools used to build this program is PostgreSQL, Python 3.6 IDLE on 
Virtual Box and Git Bash."""

import psycopg2

DBNAME = "news"


def top_articles():
    """Returns the three most viewed articles from 'news' database"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query_art = "select * from topthree;"
    c.execute(query_art)
    articles = c.fetchall()

    print("\nTop Three Articles:\n")
    for a in articles:
        print(str(a[0]) + "\t" + str(a[1]) + " views")
    db.close()


top_articles()


def top_authors():
    """Returns the most popular authors in descending order"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query_auth = "select * from top_authors;"
    c.execute(query_auth)
    authors = c.fetchall()

    print("\nMost Popular Authors:\n")
    for au in authors:
        print(str(au[0]) + "  " + str(au[1]) + " views")
    db.close()


top_authors()


def error_log():
    """Returns an error log in which more than 1% of requests
    lead to errors"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    query_log = "select * from error_log;"
    c.execute(query_log)
    errors = c.fetchall()

    print("\nErrors Exceeding 1% and Date:\n")
    for e in errors:
        print(str(e[0]) + "\t" + str(e[1]) + "% errors")
    db.close()


error_log()
