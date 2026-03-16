import requests

def get_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    
    response = requests.get(url)

    if response.status_code != 200:
        print("User not found or API error")
        return

    data = response.json()
    file_name = f"{username}_activity.txt"

    with open(file_name, "w", encoding="utf-8") as file:
        file.write(f"GitHub Activity for {username}\n")
        file.write("="*40 + "\n\n")

        for event in data:
            event_type = event["type"]
            repo = event["repo"]["name"]
            created = event["created_at"]

            activity = f"Event: {event_type}\nRepository: {repo}\nDate: {created}\n\n"
            print(activity)
            file.write(activity)

    print(f"Activity saved in {file_name}")


username = input("Enter GitHub username: ")
get_github_activity(username)