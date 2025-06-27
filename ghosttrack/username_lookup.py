import requests

def lookup_username(username):
    """
    Search for a username across multiple social media platforms.
    
    Parameters:
        username (str): The username to search for
        
    Returns:
        dict: Dictionary with platform names and URLs where username was found
    """
    results = {}

    social_media = [
        {"url": "https://www.facebook.com/{}",    "name": "Facebook"},
        {"url": "https://www.twitter.com/{}",    "name": "Twitter"},
        {"url": "https://www.instagram.com/{}",  "name": "Instagram"},
        {"url": "https://www.linkedin.com/in/{}",  "name": "LinkedIn"},
        {"url": "https://www.github.com/{}",     "name": "GitHub"},
        {"url": "https://www.pinterest.com/{}",  "name": "Pinterest"},
        {"url": "https://www.tumblr.com/{}",     "name": "Tumblr"},
        {"url": "https://www.youtube.com/{}",    "name": "YouTube"},
        {"url": "https://soundcloud.com/{}",     "name": "SoundCloud"},
        {"url": "https://www.snapchat.com/add/{}",  "name": "Snapchat"},
        {"url": "https://www.tiktok.com/@{}",    "name": "TikTok"},
        {"url": "https://www.behance.net/{}",    "name": "Behance"},
        {"url": "https://www.medium.com/@{}",    "name": "Medium"},
        {"url": "https://www.quora.com/profile/{}",  "name": "Quora"},
        {"url": "https://www.flickr.com/people/{}",  "name": "Flickr"},
        {"url": "https://www.periscope.tv/{}",   "name": "Periscope"},
        {"url": "https://www.twitch.tv/{}",      "name": "Twitch"},
        {"url": "https://www.dribbble.com/{}",   "name": "Dribbble"},
        {"url": "https://www.stumbleupon.com/stumbler/{}",  "name": "StumbleUpon"},
        {"url": "https://www.ello.co/{}",        "name": "Ello"},
        {"url": "https://www.producthunt.com/@{}",  "name": "Product Hunt"},
        {"url": "https://www.telegram.me/{}",    "name": "Telegram"},
        {"url": "https://www.weheartit.com/{}",  "name": "We Heart It"}
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0 Safari/537.36"
    }

    for site in social_media:
        url = site['url'].format(username)
        try:
            response = requests.get(url, headers=headers, timeout=10)

            # Skip blocked or error pages
            if response.status_code == 200:
                content = response.text

                # Known error patterns from your knowledge base
                if 'Temporarily Blocked' in content or \
                   'Some privacy related extensions may cause issues' in content or \
                   'This page is unavailable' in content:
                    results[site['name']] = None
                else:
                    results[site['name']] = url
            else:
                results[site['name']] = None

        except requests.exceptions.RequestException:
            results[site['name']] = None

    return {
        "username": username,
        "found_on": [name for name, link in results.items() if link],
        "links": {name: link for name, link in results.items() if link}
    }