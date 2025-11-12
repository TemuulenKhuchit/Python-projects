try:
    file = open("data.json")
except FileNotFoundError:
    with open("data.json", "w") as file:
        file.write('{"key": "value"}')
except KeyError as error_message:
    print(f"Key Error: {error_message}")
else:
    content = file.read()
    print(content)
finally:
    file.close()

# Upgraded Day 29 project with error handling and JSON data
