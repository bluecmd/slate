#!/bin/sh

CURRENT_PATH=`pwd`

source config.sh

echo "\ncd $TINK_BACKEND"
cd $TINK_BACKEND
echo "\n.docs.sh"
./docs.sh

echo "\ncp src/main-api/target/generated/swagger/swagger.json $CURRENT_PATH/"
cp src/main-api/target/generated/swagger/swagger.json $CURRENT_PATH/

echo "\ncd $CURRENT_PATH"
cd $CURRENT_PATH

echo "\n./swagger2markdown.py -s swagger.json -o source/index.html.md"
./swagger2markdown.py -s swagger.json -o source/index.html.md -t source/index.html.md.template

if [ $# -eq 1 ] && [ $1 = "serve" ]; then
    echo "\nbundle exec middleman server"
	bundle exec middleman server
else
	echo "\nbundle exec middleman build --clean"
	bundle exec middleman build --clean
fi

