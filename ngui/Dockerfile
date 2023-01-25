FROM node:16.15.0-alpine3.14
WORKDIR /app
COPY package.json ./
COPY package-lock.json ./
COPY ./ ./
RUN npm i
RUN npm dedupe
CMD ["npm", "run", "start"]
