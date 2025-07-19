import requests

# Fake search data for demo purpose
def search_movie(query):
    # Replace this with logic to fetch from @Premiummovies0_bot
    # or manually coded database
    dummy_results = [
        {"title": "Jawan 1080p BluRay", "size": "3.25 GB", "link": "https://example.com/jawan1080"},
        {"title": "Jawan 720p BluRay", "size": "1.54 GB", "link": "https://example.com/jawan720"},
        {"title": "Jawan 480p BluRay", "size": "367 MB", "link": "https://example.com/jawan480"},
    ]
    return dummy_results if query.lower() == "jawan" else []

def shorten_link(original_url):
    api_key = "32974302f4ff563e2a8a47e2b60c1e2e8161c503"
    response = requests.get(f"https://shrinkme.io/api?api={api_key}&url={original_url}")
    
    try:
        return response.json()['shortened
