#!/usr/bin/python3

# Logs Analysis project - Robin Edmunds
#
# Dev env Debian/Jessie vagrant/libvirt vm with following software version: -
# - Python 3.4.2
# - pip3 18
# - psycopg2 2.5.4
# - git version 2.1.4

# 1. What are the most popular three articles of all time? Which articles have been accessed the most? Present this information as a sorted list with the most popular article at the top.
#
# Example:
#
# "Princess Shellfish Marries Prince Handsome" — 1201 views
# "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
# "Political Scandal Ends In Political Scandal" — 553 views

import psycopg2, os

def db_query(query):
    """This function receives SQL statements and executes them"""
    conn = psycopg2.connect("dbname=news")     # connect to db "news" on localhost
    cursor = conn.cursor()      # assign conn.cursor() object to var, "cursor"
    cursor.execute(query)       # run passed sql query
    response = cursor.fetchall()        # fetch results, as dict
    conn.close()        # close connection
    return response     # return response dict

def query1():
    """1. What are the most popular three articles of all time? Which articles
    have been accessed the most? Present this information as a sorted list with
    the most popular article at the top."""

    # log.path is first 3 words of title with hyphen seperator

    print("1. What are the most popular three articles of all time? Which articles have been accessed the most?\n")

    # query = "SELECT title FROM articles LIMIT 10;"
    # query = "SELECT articles.title FROM articles;"
    # query = "SELECT articles.title FROM articles LIMIT 10;"
    # query = "SELECT log.path FROM log WHERE log.path LIKE '/article/%' LIMIT 10;"   # logs with artcle in path
    query = "SELECT COUNT(log.path) AS hits, log.path FROM log GROUP BY log.path ORDER BY hits DESC LIMIT 5;"   # count unique paths in article

    # print(" query1 - Raw output:", db_query(query), "\n\n")      # raw output for testing

    output = db_query(query)

    for i, j in enumerate(output):
        print("Title: '{1}'  --  {0} views".format(*j))


if __name__ == '__main__':
    os.system("clear")      # clear console on unix-like systems

    print("\n-----------------------------------\n" +
        "-  Logs Analysis - Robin Edmunds  -\n" +
        "-----------------------------------\n")
    query1()
    # test_query = "SELECT * FROM authors LIMIT 10;"
    # db_query(test_query)
