FROM node:25-alpine AS build

# Set working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY react-app/package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the React app
COPY react-app/ ./

# Setup of API URL
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

# Build the React app
RUN npm run build

####### Stage 2: Serve the app with nginx
FROM node:25-alpine AS run

# Copy build output to nginx html directory
COPY --from=build /app/dist ./dist

# Expose port 80
EXPOSE 5173

# Start nginx
CMD ["npx", "serve", "-s", "dist", "-l", "5173"]


