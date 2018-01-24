#! /usr/bin/env python3
"""An internal reporting tool which uses stored information as views
on a database to discover most popular articles, authors, and an error
log from a news site.

The tools used to build this program is PostgreSQL, Python 3.6 IDLE on
Virtual Box and Git Bash."""

import psycopg2


def get_query_results(query):
    db = psycopg2.connect(database="news")
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def top_articles():
    """Returns the three most viewed articles from 'news' database"""
    query_art = "select * from topthree;"
    articles = get_query_results(query_art)
    print("\nTop Three Articles:\n")
    for a in articles:
        print(str(a[0]) + "\t" + str(a[1]) + " views")


top_articles()


def top_authors():
    """Returns the most popular authors in descending order"""
    query_auth = "select * from top_authors;"
    authors = get_query_results(query_auth)
    print("\nMost Popular Authors:\n")
    for title, views in authors:
        print(title + "\t" + str(views) + " views")


top_authors()


def error_log():
    """Returns an error log in which more than 1% of requests
    lead to errors"""
    query_log = "select * from error_log;"
    errors = get_query_results(query_log)
    print("\nErrors Exceeding 1% and Date:\n")
    for e in errors:
        print(str(e[0]) + "\t" + str(e[1]) + "% errors")


error_log()
