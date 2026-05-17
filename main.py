import requests
response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(f"상태 코드: {response.status_code}")
data = response.json()
print(f"할 일 제목: {data['title']}")
print(f"완료 여부: {data['completed']}")
if response.status_code == 200:
    print("✅ 성공!")
else:
    print("❌ 뭔가 잘못됐어요")