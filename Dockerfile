FROM python

RUN apt-get update && apt-get install -y nginx
RUN pip install pipenv

RUN adduser user --home=/home/user/
USER user

ADD Pipfile Pipfile.lock /home/user/app/
WORKDIR /home/user/app/

RUN pipenv install --dev

ADD . /home/user/app

ENV DJANGO_SETTINGS_MODULE rsvp_backend.settings.dev_settings

CMD pipenv run uwsgi --http :8000 --chdir $(pwd)/rsvp_backend --module rsvp_backend.wsgi --env DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE --virtualenv=$(pipenv --venv)
