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

import psycopg2

def db_query(query):
    psycopg2.connect("dbname=news")     # connect to db "news" on localhost
    cursor = conn.cursor()      # assign conn.cursor() object to var, "cursor"

    cursor.execute(query)

    conn.commit()
    conn.close()

def query1():
    print("Query 1")


if __name__ == '__main__':
    main()
