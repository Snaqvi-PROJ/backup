FROM hello-world:latest
WORKDIR /app
COPY db.sh db.sh
ENV APP_NAME=db.sh
