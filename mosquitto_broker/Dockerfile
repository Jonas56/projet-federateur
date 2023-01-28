FROM eclipse-mosquitto:latest

COPY ./config/mosquitto.conf /mosquitto_temp/config/
#COPY ./config/password.txt /mosquitto/config/

CMD ["mosquitto", "-c", "/mosquitto_temp/config/mosquitto.conf"]