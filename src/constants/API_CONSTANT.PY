base_url = "https://jsonplaceholder.typicode.com"
get_all_user_url = f"{base_url}/users"
get_user_by_id_url = f"{base_url}/users/1"
post_user_url = f"{base_url}/users" 
put_user_url = f"{base_url}/users/1"
delete_user_url = f"{base_url}/users/1"



# print(get_all_user_url)

headers = {
  'Content-Type': 'application/json' }