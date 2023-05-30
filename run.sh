#!/bin/bash

DOCKER_FOLDER_DB="utils/docker/vols/db"
DOCKER_FOLDER_MYSQLD="utils/docker/vols/mysqld"
DOCKER_REPO_PATH="cgarvey/django-mywishlist"

function show_help() {
    echo "Usage: call run.sh with the following supported args"
    echo "  [h]elp : Show this help text"
    echo "  [i]nit : Initialise the Docker env for first run"
    echo "  [r]un : Run the previously initialised Docker env"
    echo "  [c]lean : Clean up all Docker env files and volumes to start afresh"
    echo "  [m]ysql : Run MySQL client against the main database"
    echo ""
}

function do_clean() {
    echo "Cleaning/resetting Dev Docker env..."
    if [[ -d "$DOCKER_FOLDER_DB" ]]; then
        REPLY=y
        # read -p "This will DELETE Docker volumes, are you sure you want to continue? " -n 1 -r
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            echo ""
            echo "Deleting..."
            if [[ -d "$DOCKER_FOLDER_DB" ]]; then
                echo "Deleted data volume"
                rm -r "$DOCKER_FOLDER_DB"
            fi
            if [[ -d "$DOCKER_FOLDER_MYSQLD" ]]; then
                echo "Deleted mysql volume"
                rm -r "$DOCKER_FOLDER_MYSQLD"
            fi
            exit
        else
            echo ""
            echo " ...quitting"
            exit
        fi
    else
        echo "No data volumes were present to delete"
    fi
}
function do_init() {
    echo "Iniatialising Dev Docker env..."
    if [[ -d "$DOCKER_FOLDER_DB" ]]; then
        echo "The folder '$DOCKER_FOLDER_DB' already exists, can't proceed. Use the 'clean' argument if you want to reset the env."
    elif [[ -d "$DOCKER_FOLDER_MYSQLD" ]]; then
        echo "The folder '$DOCKER_FOLDER_MYSQLD' already exists, can't proceed. Use the 'clean' argument if you want to reset the env."
    else
        echo "Creating Docker shared volume folders..."
        mkdir "$DOCKER_FOLDER_DB"
        mkdir "$DOCKER_FOLDER_MYSQLD"
        echo ""
        echo ""

        echo "Pulling needed Docker Images"
        # docker pull --platform linux/x86_64 mysql:5.7
        docker pull --platform linux/x86_64 mysql:8
        docker pull python:2.7
        echo ""
        echo ""

        echo "Building Docker app image"
        /usr/local/bin/docker build . -t "$DOCKER_REPO_PATH"
        echo ""
        echo ""

        echo "Starting Environment"
        docker-compose up &
        sleep 45
        echo ""
        echo ""

        echo "Seeding Database"
        docker-compose run --rm web python manage.py migrate
        docker-compose run --rm web python manage.py createsuperuser --username admin --email admin@example.com --noinput
        docker-compose run --rm web python manage.py reset_admin_pwd
        echo ""
        echo ""

        echo "Stopping Environment"
        docker-compose down
        echo ""
        echo ""
    fi
}
function do_run() {
    echo "Running Dev Docker env..."
    if [[ -f "docker-compose.yml" ]]; then
        docker-compose up
    else
        echo "Can't find Docker Compose file, quitting."
        exit -1
    fi
}

function do_mysql_client() {
    echo "Launching MySQL Client..."
    mysql --protocol tcp -h localhost  -P 33306 -uroot -proot mywishlist
}

function do_db_migrate() {
    echo "Running Dev Docker env..."
    if [[ -f "docker-compose.yml" ]]; then
        docker-compose run --rm web python manage.py migrate
    else
        echo "Can't find Docker Compose file, quitting."
        exit -1
    fi
}

if [ -d utils ] && [ -d utils/docker ]; then
    echo -e "Dev Environmnet Runner\n"

    if [[ -z "$1" ]]; then
        show_help
    elif [[ "$1" == "h" ]] || [[ "$1" == "help" ]]; then
        show_help
    elif [[ "$1" == "i" ]] || [[ "$1" == "init" ]]; then
        do_init
    elif [[ "$1" == "c" ]] || [[ "$1" == "clean" ]]; then
        do_clean
    elif [[ "$1" == "m" ]] || [[ "$1" == "mysql" ]]; then
        do_mysql_client
    elif [[ "$1" == "r" ]] || [[ "$1" == "run" ]]; then
        do_run
    else
        echo "Invalid arguments specified. Please call 'run.sh help' for usage help."
    fi
else
    echo "Run from the repo root directory."
fi

