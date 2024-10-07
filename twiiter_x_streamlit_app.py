import streamlit as st
import tweepy


def main():
    API_KEY = ""
    API_KEY_SECRET = ""
    ACCESS_TOKEN = ""
    ACCESS_TOKEN_SECRET = ""

    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)

    client = tweepy.Client(consumer_key=API_KEY, consumer_secret=API_KEY_SECRET,
                           access_token=ACCESS_TOKEN, access_token_secret=ACCESS_TOKEN_SECRET)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)

    with st.form('Twitter Bot'):
        tweet_text = st.text_input('Put in tweet text')

        tweet_media = st.file_uploader(
            'Upload tweet media', type=['png', 'jpg', 'mp4'])

        send_tweet_btn = st.form_submit_button('Send Tweet')

    if send_tweet_btn:
        if tweet_media:
            with open(f'uploads/{tweet_media.name}', 'wb') as f:
                f.write(tweet_media.getbuffer())
            media = api.media_upload(f'uploads/{tweet_media.name}')
            media_id = media.media_id

            response = client.create_tweet(
                text=tweet_text, media_ids=[media_id])
        else:
            response = client.create_tweet(text=tweet_text)

        st.success("Tweet created successfully")
        st.write(response)


if __name__ == '__main__':
    main()
