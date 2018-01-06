# Project 3: Logs Analyst for Udacity's Full Stack Developer Nanodegree
## ABOUT

An internal reporting tool written in Postgresql and Python (3.6) which uses stored information on a database to
discover most popular articles, authors, and a request error log from a news reporting website.

## VIEWS CREATED

- Top Three Articles

```
SELECT articles.title,
    count(*) AS views
   FROM articles,
    log
  WHERE concat('/article/', articles.slug) like log.path
  GROUP BY articles.title
  ORDER BY (count(*)) DESC
 LIMIT 3;
 ```
 
 - Most Popular Authors
 
 ```
 SELECT authors.name,
    count(*) AS views
   FROM articles,
    authors,
    log
  WHERE authors.id = articles.author AND concat('/article/', arti
cles.slug) like log.path
  GROUP BY authors.name
  ORDER BY (count(*)) DESC;
  ```
  
  - Error Log Greater Than 1%
  
  ```
  SELECT to_char(log."time", 'DD Mon YYYY'::text) AS date,
    round(count(*)::numeric * 100.0 / sum(count(*)) OVER (), 1) A
S error_percent
   FROM log
  WHERE log.status = '404 NOT FOUND'::text
  GROUP BY (to_char(log."time", 'DD Mon YYYY'::text))
  ORDER BY (round(count(*)::numeric * 100.0 / sum(count(*)) OVER
(), 1)) DESC;
```



  

