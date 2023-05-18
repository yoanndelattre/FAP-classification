import requests
import os
from dotenv import dotenv_values

def download(query, output_folder):
    # Define the number of tweets to retrieve
    tweet_count = 100

    # Load variables from .env file
    env_vars = dotenv_values(".env")

    # Check if API_KEY is not None
    twitter_bearer_token = env_vars.get("TWITTER_BEARER_TOKEN")

    if twitter_bearer_token is not None:

        # Twitter API endpoint for v2 search
        endpoint = "https://api.twitter.com/2/tweets/search/recent"

        # Set request parameters
        params = {
            "query": query,
            "max_results": tweet_count,
            "tweet.fields": "attachments,public_metrics",
            "expansions": "attachments.media_keys",
            "media.fields": "url",
        }

        # Set authorization header (optional if using bearer token)
        headers = {}
        headers["Authorization"] = f"Bearer {twitter_bearer_token}"

        # Send request to Twitter API
        response = requests.get(endpoint, params=params, headers=headers)

        # Process response
        if response.status_code == 200:
            data = response.json()

            # Sort tweets by retweet count in descending order
            tweets = data["data"]
            sorted_tweets = sorted(tweets, key=lambda x: x["public_metrics"]["retweet_count"], reverse=True)

            # Create a folder to store the downloaded images
            output_folder = os.path.join(output_folder, query)
            os.makedirs(output_folder, exist_ok=True)

            # Download images
            if "includes" in data:
                media = data["includes"]["media"]
                for tweet in sorted_tweets:
                    if "attachments" in tweet and "media_keys" in tweet["attachments"]:
                        media_keys = tweet["attachments"]["media_keys"]
                        for media_info in media:
                            if media_info["media_key"] in media_keys:
                                if "url" in media_info:
                                    media_url = media_info["url"]
                                elif "media_url_https" in media_info:
                                    media_url = media_info["media_url_https"]
                                else:
                                    print("Media URL not found:", media_info)
                                    continue
                                image_filename = media_url.split("/")[-1]
                                image_path = os.path.join(output_folder, image_filename)
                                # Download the image
                                response = requests.get(media_url, stream=True)
                                if response.status_code == 200:
                                    with open(image_path, "wb") as file:
                                        file.write(response.content)
                                    print(f"Downloaded: {image_filename}")
                                else:
                                    print(f"Error downloading: {image_filename}")
                                break  # Break the loop after finding the media for the tweet
        else:
            print("Error accessing Twitter API:", response.text)
    else:
        print("TWITTER_BEARER_TOKEN is not defined or is None.")