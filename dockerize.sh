#!/bin/zsh

export $(cat .env | xargs)

docker buildx build --debug -t love_letter:v1 .

docker run \
           -e "MY_NAME=$MY_NAME" \
           -e "WIFE_NAME=$WIFE_NAME" \
           -e "GEMINI_API_KEY=$GEMINI_API_KEY" \
           -e "MY_EMAIL=$MY_EMAIL" \
           -e "MY_EMAIL_KEY=$MY_EMAIL_KEY" \
           -e "MY_WIFE_EMAIL=$MY_WIFE_EMAIL" \
           love_letter:v1
