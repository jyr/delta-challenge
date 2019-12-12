# Delta Docker Compose

|Service| Service Name | Host | Port |
|---|---|---|---|
| Db | db | db.delta-dev.com | 5432 |
| Api | api | api.delta-dev.com | 8000 |

## Setting everything up

1. Add the following entries to your `/etc/hosts` file.

  ```
  # Services

  127.0.0.1  db.delta-dev.com
  127.0.0.1  api.delta-dev.com
  ```

2. Install docker https://www.docker.com/get-docker
3. Install docker-compose https://docs.docker.com/compose/install/
4. Start the **docker-compose** service.

## Basic Usage

- Enter in compose `cd build`

- Build all services `docker-compose up --build`

- Start all services `docker-compose up`

- Stop all services `docker-compose stop`

- Open the shell `docker-compose exec api /bin/sh`

## Data

**create a backup database**

```
docker-compose exec api /bin/sh -c -l "./manage.py dumpdata --natural-foreign --exclude auth.permission --exclude contenttypes --indent 2 > data/initial_to_dev.json""
```

**load initial data**

```
docker-compose exec api /bin/sh -c -l "./manage.py loaddata data/initial_to_dev.json"
```

## Django tests
```
$ docker-compose exec api /bin/sh -c -l "./manage.py test apis"
```

## Run crawler
```
$ docker-compose exec api /bin/sh -c -l "scrapy runspider scrappers/news/spiders/articles.py -o news.csv"
```


## Docs

* **delta API** - http://api.delta-dev.com:8000/docs/
* **HTTP Status Codes** - https://www.restapitutorial.com/httpstatuscodes.html

## Commitizen

1. Install Commitizen https://github.com/commitizen/cz-cli#installing-the-command-line-tool
2. Initialize the Commitize on project

```
$ cd $HOME
$ npm init --yes
$ npm install commitizen -g
$ commitizen init cz-conventional-changelog --save-dev --save-exact
```
3. Run commitizen after create a new changes on the project

```
$ git add .
$ git cz
```
