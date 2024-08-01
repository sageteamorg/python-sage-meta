Fetching Top Media for a Hashtag
--------------------------------

The `get_top_media` method fetches top media for a given hashtag.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        top_media = fb_client.hashtag_handler.get_top_media(hashtag_id="HASHTAG_ID", insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
        for media in top_media:
            print(media)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_top_media` method fetches top media for the given hashtag.
- If the operation fails, it raises an appropriate error.
