import psycopg2
# database is using PostgreSQL so importing it


# assigning database
databasename = "news"


q1 = dict()
q2 = dict()
q3 = dict()

# query to get the most popular 3 articles
q1['desc'] = "The Most Popular 3 Articles of all time are :"
qry1 = """ select articles.title, count(*) as view
         from articles inner join log on log.path
         like concat('%', articles.slug, '%')
         where log.status like '%200%' group by
         articles.title, log.path order by view desc limit 3"""


# query to get mostpopular article's authors
q2['desc'] = "The Most Popular Article's Author of All Time :"
qry2 = """select authors.name, count(*) as view from articles inner
         join authors on articles.author = authors.id inner join log
         on log.path like concat('%', articles.slug, '%') where
         log.status like '%200%' group
         by authors.name order by view desc"""


# query to get the days on which the requests lead to an error more han 1%
q3['desc'] = "Days on which requests lead with an error more than 1% :"
qry3 = """
    select day, percentage from (
    select day, round((sum(req)/(select count(*) from log where
    substring(cast(log.time as text), 0, 11) = day) * 100), 2) as
    percentage from (select substring(cast(log.time as text), 0, 11) as day,
    count(*) as req from log where status like '%404%' group by day)
    as final_percentage group by day order by percentage desc) as final_query
    where percentage >= 1"""


# function definition to execute queries


def execute_queries(queries):
    db = psycopg2.connect(database=databasename)
    c = db.cursor()
    c.execute(queries)
    answer = c.fetchall()
    db.close()
    return answer

#  function definition to get output


def output_result(question):
    print('\n' + '##############################' + '\n \n' +
          question['desc'] + '\n')
    for row in question['answer']:
        print(str(row[0]) + ' : ' + str(row[1]) + '\n')

if __name__ == '__main__':
    # passing values to run the queries
    q1['answer'] = execute_queries(qry1)
    q2['answer'] = execute_queries(qry2)
    q3['answer'] = execute_queries(qry3)

    # passing values from execute_quries function to output_result
    # to print output
    output_result(q1)
    output_result(q2)
    output_result(q3)
