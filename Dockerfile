# Serve the static Calculus 1 course with busybox httpd (tiny image).
FROM busybox:musl

# Copy the course pages into the web root, force them world-readable (host
# files are mode 0600), and make the index the "/" default.
COPY src/*.html /www/
RUN chmod 644 /www/*.html \
 && ln -sf calc1_00_index.html /www/index.html

EXPOSE 80
CMD ["httpd", "-f", "-v", "-p", "80", "-h", "/www"]
