arr = {"email": "test@test.com", "name": "John", "picture": "url"}
columns = ", ".join(arr.keys())

print(columns)  # Вывод: 'email, name, picture' (это строка с кавычками для отображения)

query = f"INSERT INTO users ({columns}) VALUES (%s, %s, %s)"
#print(query)  # Вывод: INSERT INTO users (email, name, picture) VALUES (%s, %s, %s)