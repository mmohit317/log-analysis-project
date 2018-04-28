# Log-Analysis-Project
Using Python-DPI

## PROJECT DESCRIPTION:
This project consists of a program which fetches 3 different queries from a database named newsdata.sql.

## DATABASE CONSISTS DETAILS OF:
- NO OF AUTHORS
- NO OF ARTICLES WRITTEN BY THE AUTHORS
- PUBLISHING DATE AND TIME INFORMATION OF THE ARTICLES
- AND MANY MORE DETAILS OF LOG

## REQUIREMENTS TO RUN THE PROJECT:
- Vagrant 
- Virtual Box
- Newsdata.sql database 

## How to run the Project?
- Clone or download the repository
- Copy the files in the vagrant directory
- Launch Vagrant: 
  `vagrant up`
- Load the database:
  `psql -d news -f newsdata.sql`
- Execute the program:
  `python project.py`

  

