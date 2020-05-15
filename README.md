# Mapserver in Docker

This is an Ubuntu-derived image containing [MapServer](http://www.mapserver.org/) running under the Nginx web server as a FastCGI service.
 
We've adapted the geo-data/mapserver-docker repository to use mapserver and GDAL from the UbuntuGIS stable channel.

## Usage

The HTTP endpoint for the MapServer `mapserv` CGI binary is the root URL at `/`. This can be tested by mapping the web server's port `80` on the container to port `8080` on the host:

    docker run -p 8080:80 mymapserver:latest

You can then test using the included example mapfile by pointing your browser at
<http://localhost:8080/?map=/usr/local/share/mapserver/examples/test.map&mode=map>.
    
Other than the test mapfile located at `/usr/local/share/mapserver/examples/test.map` no other MapServer configuration is provided: you will need to provide appropriate mapfiles and ancilliary configuration files (e.g. templates) for running Mapserver, either via volume or bind mounts or in a derived image.  E.g. assuming you have the mapfile 'my-app.map' in the current working directory, you could mount it as:

    docker run -v $(pwd):/maps:ro -p 8080:80 myaccount/mapserver

You will then be able to access the map from your host machine at <http://localhost:8080/?map=/maps/my-app.map&mode=map>.
