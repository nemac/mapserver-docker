FROM ubuntu:18.04

MAINTAINER Matthew Geiger <mgeiger@unca.edu>

USER root

EXPOSE 80

ADD . /tmp/build/

RUN /tmp/build/build.sh

# Start the fcgi and web servers.
CMD ["/usr/local/bin/run.sh"]
