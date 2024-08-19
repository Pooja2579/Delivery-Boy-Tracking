from confluent_kafka import Producer
import json
import os

conf = {'bootstrap.servers':'localhost:9092'}
producer = Producer(**conf)

start_latitude = 19.0760
starting_longitude = 72.8777
end_latitude = 18.5204
end_longitude = 73.8567

num_steps = 1000
step_size_lat = (end_latitude- start_latitude)/ num_steps
step_size_lon = (end_longitude - starting_longitude)/ num_steps
current_steps = 0

while True:
    latitude = start_latitude + starting_longitude