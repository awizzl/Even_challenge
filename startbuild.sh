#!/bin/bash

docker-compose up -d  --build app
echo "bulding app container Complete"
docker-compose up -d  --build db
echo "bulding db container Complete"
docker-compose up -d  --build trainer
echo "bulding training container Complete"