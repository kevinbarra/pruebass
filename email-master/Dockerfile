FROM node:20.11-alpine

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 5000

ENV SENDGRID_PORT=5000

CMD ["node", "app.js"]
