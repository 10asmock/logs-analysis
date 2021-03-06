# Project 3: Logs Analyst for Udacity's Full Stack Developer Nanodegree
## ABOUT

An internal reporting tool written in Postgresql and Python (3.6) which uses stored information on a database to
discover most popular articles, authors, and request error log from a news reporting website.

## HOW TO USE

- Install [Virtual Box](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) and [Vagrant](https://www.vagrantup.com/downloads.html)

- Download and unzip [FSND-Virtual-Machine.zip](https://d17h27t6h515a5.cloudfront.net/topher/2017/August/59822701_fsnd-virtual-machine/fsnd-virtual-machine.zip) or clone [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm). This will give you a directory called *FSND-Virtual-Machine*.

- Download ```newsdata.py``` from this repository and insert it into the FSND-Virtual-Machine ```vagrant``` directory.

- From your terminal, inside the ```vagrant``` subdirectory, run the command ```vagrant up```. This will cause Vagrant to download the Linux operating system and install it.

- When vagrant up is finished running, you will get your shell prompt back. At this point, you can run ```vagrant ssh``` to log in to your newly installed Linux VM!

- To load the data, ```cd``` into the ```vagrant``` directory and use the command ```psql -d news -f newsdata.sql```. Once set up, you can use the ```psql -d news``` command to re-access the database if you leave.

- In Vagrant, run the command ```python3 newsdata.py``` to view the query.

- Alternatively, you can access ```newsdata.sql``` by entering ```-d news``` and once you're inside the ```news``` database, type in the code below to check out the three most viewed articles of all time, the most popular authors in descending order, and examine user request errors exceeding 1% by date and aggregated error percentage.

## VIEWS CREATED

- Top Three Articles

```
CREATE VIEW topthree as
SELECT articles.title,
    count(*) AS views
   FROM articles,
    log
  WHERE concat('/article/', articles.slug) = log.path
  GROUP BY articles.title
  ORDER BY (count(*)) DESC
 LIMIT 3;
 ```
 
 - Most Popular Authors
 
 ```
 CREATE VIEW top_authors as
 SELECT authors.name,
    count(*) AS views
   FROM articles,
    authors,
    log
  WHERE authors.id = articles.author 
  AND concat('/article/', articles.slug) = log.path
  GROUP BY authors.name
  ORDER BY (count(*)) DESC;
  ```
  
  - Error Log Greater Than 1%
  
  ```
 CREATE VIEW error_log as
 SELECT to_char(totals.date, 'Mon DD, YYYY') AS date,
    100.0 * error_views /
        total_views as error_percentage
 FROM
    (select date(time) as date,
        count(*) as total_views
    FROM log
    GROUP BY date(time)) as totals,
    (select date(time) as date,
        count(*) as error_views
    FROM log
    WHERE status != '200 OK'
    GROUP BY date(time)) as errors
 WHERE totals.date = errors.date
    and 100.0 * error_views / total_views > 1
 ORDER BY totals.date;
```

## TOOLS USED   

- Python 3.6 editor IDLE
- Postgresql



  

