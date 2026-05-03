import requests

def test_endpoint(name, url):
    print(f"Testing {name}...")
    try:
        res = requests.get(url)
        print(f"Status: {res.status_code}")
        print(f"Response: {res.json()}")
    except Exception as e:
        print(f"Error: {e}")
    print("-" * 20)

test_endpoint("Stats", "http://127.0.0.1:5000/comment_stats")
test_endpoint("Chart Data", "http://127.0.0.1:5000/chart_data")
test_endpoint("Comments", "http://127.0.0.1:5000/comments")
