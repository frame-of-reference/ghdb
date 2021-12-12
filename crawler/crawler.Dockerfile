FROM python:3.10.1-buster

SHELL ["/bin/bash", "-c"]

# Install prerequisite
RUN apt-get update


# Scrapy and IPython system deps
RUN apt-get install -y --no-install-recommends gcc libxml2-dev libxslt1-dev zlib1g-dev libffi-dev libssl-dev


# We want both under Python 3
RUN apt-get install -y --no-install-recommends python3 python3-dev python3-pip git




# ENV (map a local folder ./ into this docker by -v $(pwd):/code -e USER=<user>, this folder should contain all of your .py crawlers)
ENV CODE_DIR /ghdb


# Working dir mount
RUN mkdir -p ${CODE_DIR} && mkdir ${CODE_DIR}/crawler
WORKDIR ${CODE_DIR}


# Copy requirements -- # TODO: Switch to poetry
COPY requirements.txt .


# Create venv
RUN python3 -m venv venv


# Upgrade pip
RUN /usr/local/bin/python -m pip install --upgrade pip && \
    source venv/bin/activate && \
    pip3 install -U setuptools wheel && \
    pip3 install -r requirements.txt



# Clean up APT when done
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



# Entrypoint
#ADD scripts/init_crawler.sh ${CODE_DIR}/scripts/init_crawler.sh

COPY . ${CODE_DIR}/crawler

#ENTRYPOINT [ "crawler/scripts/init_crawler.sh" ]