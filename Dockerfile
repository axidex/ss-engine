FROM python:3.10-bullseye

USER 0

RUN mkdir /var/log/ss-enigne

RUN chown -R 1001:0 /tmp && \
    chmod -R g=u /tmp

RUN chown -R 1001:0 /var && \
    chmod -R g=u /var

RUN chown -R 1001:0 /opt/ss-engine && \
    chmod -R g=u /opt/ss-engine

USER 1001

WORKDIR /opt/ss-engine

RUN python3 -m venv .venv
RUN python3 -m venv .venv_deepsecrets

COPY requirements.txt requirements.txt

RUN .venv_deepsecrets/bin/python -m pip install deepsecrets

RUN .venv/bin/python -m pip install --no-cache-dir -r requirements.txt

COPY src src
COPY entrypoint.py entrypoint.py

COPY bin bin

ENTRYPOINT[".venv/bin/python", "entrypoint.py"]
