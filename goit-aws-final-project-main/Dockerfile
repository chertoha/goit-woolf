FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

RUN npx prisma generate

RUN npm run build

EXPOSE 9000

# CMD ["node", "npx prisma migrate deploy", "dist/main"]
CMD ["sh", "-c", "npx prisma migrate deploy && node dist/main"]