web: daphne smathchat.asgi:application -p $PORT -b 0.0.0.0
daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem smathchat.asgi:application