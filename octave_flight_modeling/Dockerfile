FROM python:3.11

WORKDIR /octave_flight_modeling

COPY ./requirements.txt /octave_flight_modeling/requirements.txt
COPY ./rest_interface.py /octave_flight_modeling/rest_interface.py
COPY ./flight_velocity_modeling.m /octave_flight_modeling/flight_velocity_modeling.m
RUN pip install -r requirements.txt

COPY . .

RUN apt-get update && apt-get install -y octave

RUN addgroup --gid 10016 choreo && \
    adduser --disabled-password --no-create-home --uid 10016 --ingroup choreo choreouser

USER 10016

EXPOSE 5000

ENV FLASK_APP=rest_interface.py

CMD ["flask", "run", "--host=0.0.0.0"]
