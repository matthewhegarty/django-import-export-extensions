FROM python:3.12.7
ARG build_env=local

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/app
RUN groupadd app && useradd --shell /bin/bash -g app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/server
RUN mkdir $APP_HOME
WORKDIR $APP_HOME

ENV CELERY_HOME=/home/celery
RUN mkdir $CELERY_HOME

RUN apt-get -q update && apt-get -qy install make

COPY pyproject.toml $APP_HOME/
COPY test_project $APP_HOME/test_project/

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --upgrade pip
RUN pip install celery poetry django-import-export-extensions
RUN poetry install --with dev

COPY docker/celery/start-celery-worker.sh $CELERY_HOME/

RUN chown -R app:app $HOME $CELERY_HOME/
USER app

ENTRYPOINT ["/home/celery/start-celery-worker.sh"]
