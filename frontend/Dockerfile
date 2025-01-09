# Use an nginx base image
FROM nginx:alpine

# Remove the default nginx index page
RUN rm /usr/share/nginx/html/*

# Copy the index.html file to the nginx folder
COPY index.html /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start nginx
CMD ["nginx", "-g", "daemon off;"]
