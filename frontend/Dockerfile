# Use official Node.js image
FROM node:18-alpine

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the project files
COPY . .

# Expose frontend on 8073
EXPOSE 8073

# Build the app
RUN npm run build

# Serve the app using Vite (with --host)
CMD ["npm", "run", "preview", "--", "--port", "8073", "--host"]

