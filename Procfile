web: daphne -p $PORT -b 0.0.0.0 -smathchat.asgi:application
web: daphne -e ssl:443:privateKey=key.pem:certKey=crt.pem smathchat.asgi:application