#!/usr/bin/env bash

# Clone frontend from Gitbub and build it
if [ ! -e IOT_Frontend ] || [ "$#" -ne 0 ] && [ "$1" = "rebuild" ];  then
    git clone git@github.com:garyparrot/IOT_Frontend.git
    cd IOT_Frontend 
    git pull origin master
    npm install
    npx react-scripts build
    cd ..
fi

# Setup linkage to build file
cp    IOT_Frontend/build/index.html  application/dashboard/templates/
cp    IOT_Frontend/build/index.css   application/dashboard/static/
cp -r IOT_Frontend/build/static/     application/dashboard/static/

# Start it
/usr/bin/env python3 wsgi.py
