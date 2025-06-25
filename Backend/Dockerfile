FROM node:22.15.0

WORKDIR /app

COPY package*.json ./
RUN RUN npm ci --production

COPY . .

EXPOSE 5000
CMD ["node", "server.js"]