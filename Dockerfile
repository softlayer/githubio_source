FROM icr.io/ibm/alpine
RUN mkdir -p /home/sldn/html
COPY ./  /home/sldn
WORKDIR "/home/sldn"
EXPOSE 1313
RUN ./bin/hugo -d html -b http://localhost:1313
WORKDIR "/home/sldn/html"
RUN apk add mini_httpd
RUN chown minihttpd /home/sldn/html
CMD mini_httpd -C "/home/sldn/min_http.conf" -D -l stdout