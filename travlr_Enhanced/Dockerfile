FROM node:24

WORKDIR /app

COPY package*.json .

RUN npm install

COPY . .

EXPOSE 8080

CMD node ./app_api/models/seed.js && npm start