import psycopg2

con = psycopg2.connect(
  database="postgres", # Имя базы данных, к которой нужно подключиться
  user="postgres", # Имя пользователя, которое будет использоваться для аутентификации
  password="Nulla1Rosa88", # Пароль базы данных для пользователя.
  host="127.0.0.1",
  port="5432"
)

print("Database opened successfully")