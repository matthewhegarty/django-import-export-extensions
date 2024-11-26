FROM python:3.12.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app
RUN groupadd app && useradd --shell /bin/bash -g app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/server
RUN mkdir $APP_HOME

RUN apt-get -q update && apt-get -qy install netcat-traditional

COPY pyproject.toml $APP_HOME/
COPY test_project $APP_HOME/test_project/
WORKDIR $APP_HOME

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install poetry django-import-export-extensions
RUN poetry install --with dev

COPY docker/server/wait-for /usr/local/bin/wait-for
COPY docker/server/start-server.sh $APP_HOME/

RUN chown -R app:app $HOME
USER app

ENTRYPOINT ["/home/server/start-server.sh"]
