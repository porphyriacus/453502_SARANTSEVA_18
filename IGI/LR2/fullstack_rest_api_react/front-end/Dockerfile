#FROM node:14-alpine
FROM node:18

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY . .

RUN npm install react-scripts --save

EXPOSE 3000

CMD ["npm", "start"]
