web: daphne smathchat.asgi:chat -p $PORT -b 0.0.0.0
daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem smathchat.asgi:application