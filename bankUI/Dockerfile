FROM python:3.9-alpine

RUN pip install pipenv

COPY . .

WORKDIR /app

RUN pipenv install -no-cache-dir --no-use-pep517 --system --deploy

EXPOSE 15001

ENTRYPOINT [ "python" ]

CMD [ "main.py" ]