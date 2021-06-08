# build stage
FROM node:9.11.1-alpine as build-stage
WORKDIR /app/
COPY client/package.json /app/
RUN npm cache verify
RUN npm install
COPY client /app/
RUN npm run build

# production stage
FROM nginx:1.13.12-alpine as production-stage
COPY nginx/prod.conf /etc/nginx/nginx.conf
COPY backend/static /usr/src/app/static/
COPY --from=build-stage /app/dist /dist/
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]