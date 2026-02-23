
name = input("Enter your name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
is_developer_input = input('Are you Developer (True/False): ')
is_developer = is_developer_input.lower() == "true"
if is_developer:
    profession = "developer"
else: 
    profession = input('Write your profession: ')

print(f"My name is {name}. I am {age} years old. I am from {city}. I am a {profession}.")