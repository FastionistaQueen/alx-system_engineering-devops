import requests

def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "subreddit-subscriber-counter"}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code != 200:
            return 0
        
        data = response.json().get('data')
        if data:
            return data.get('subscribers', 0)
        return 0
    except Exception:
        return 0

