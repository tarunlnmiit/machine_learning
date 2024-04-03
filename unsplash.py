import random
import requests
import streamlit as st

UNSPLASH_ACCESS_KEY = "<API KEY GOES HERE>"
UNSPLASH_PHOTOS_URL = "https://api.unsplash.com/search/photos?"

def main():
    st.title('Social Media Magic')
    with st.form(key='unsplash_images', clear_on_submit=True):
        user_input = st.text_input('Enter a keyword or phrase to search for images: ')
        st.form_submit_button(label='Get Unsplash Images')

    if user_input:
        metadata_url = f'{UNSPLASH_PHOTOS_URL}client_id={UNSPLASH_ACCESS_KEY}&query={user_input}'
        get_query_unsplash_metadata = requests.get(metadata_url).json()

        total_images = get_query_unsplash_metadata['total']
        total_pages = get_query_unsplash_metadata['total_pages']
        page_number = random.randint(1, total_pages)

        final_url = f'{UNSPLASH_PHOTOS_URL}client_id={UNSPLASH_ACCESS_KEY}&query={user_input}&page={page_number}'
  
        unsplash_images_data = requests.get(final_url).json()
        user_input = None
        
        images = [result['urls']['regular'] for result in unsplash_images_data['results']]
        for image in images:
            st.image(image)

if __name__ == '__main__':
    st.set_page_config(page_title="Social Media Magic", page_icon="🪄", layout='wide')
    main()
