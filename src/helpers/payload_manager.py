import random

# Payload for creating a new user
create_user_payload = {
    "name": "John Doe",
    "email": "john.doe@example.com"
}

# Payload for updating an existing user
update_user_payload = {
    "name": "Updated Name",
    "email": "updated@test.com"
}



names = [
    "John Doe",
    "Jane Smith",
    "Michael Johnson",
    "Emily Davis",
    "Robert Brown",
    "Sophia Wilson",
    "David Miller",
    "Olivia Taylor",
    "James Anderson",
    "Emma Thomas"
]

def generate_user_payload():
    name = random.choice(names)
    
    # short random number (2 digits)
    random_num = random.randint(10, 99)

    email = name.lower().replace(" ", ".") + f"{random_num}@yopmail.com"

    payload = {
        "name": name,
        "email": email
    }

    return payload