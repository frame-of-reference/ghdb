FROM python:3.10.1-buster

# Install prerequisite
RUN apt-get update


# Scrapy and IPython system deps
RUN apt-get install -y --no-install-recommends gcc libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev


# We want both under Python 3.5+ instead of 2.7
RUN apt-get install -y --no-install-recommends python3 python3-dev python3-pip git


# Pip deps's deps during install
RUN pip3 install -U setuptools wheel


# Copy docker requirements -- # TODO: Switch to poetry
COPY ./requirements-docker.txt .


# Finally the real thing needed
RUN pip3 install -r requirements-docker.txt


# Clean up APT when done
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*


# ENV (map a local folder ./ into this docker by -v $(pwd):/code -e USER=<user>, this folder should contain all of your .py crawlers)
ENV CRAWLER_FOLDER /crawler
ENV USER spider

# Working dir mount
RUN mkdir -p ${CRAWLER_FOLDER}
WORKDIR ${CRAWLER_FOLDER}

# Entrypoint
#ADD scripts/init_crawler.sh ${CRAWLER_FOLDER}/scripts/init_crawler.sh

COPY . ${CRAWLER_FOLDER}

ENTRYPOINT [ "scripts/init_crawler.sh" ]