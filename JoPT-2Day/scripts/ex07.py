import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
posts = response.json()
for index in range(10):
    print(index+1, ":", posts[index]['title'])