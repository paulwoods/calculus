# Serve the static Calculus 1 course with nginx.
FROM nginx:alpine

# Copy the course pages into nginx's web root.
COPY src/*.html /usr/share/nginx/html/

# Force the pages world-readable so the unprivileged nginx worker can serve
# them regardless of host file modes, and make the index the "/" default.
RUN chmod 644 /usr/share/nginx/html/*.html \
 && ln -sf calc1_00_index.html /usr/share/nginx/html/index.html
