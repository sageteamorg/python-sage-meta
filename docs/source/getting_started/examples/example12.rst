Fetching Recent Media for a Hashtag
-----------------------------------

The `get_recent_media` method fetches recent media for a given hashtag.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        recent_media = fb_client.hashtag_handler.get_recent_media(hashtag_id="HASHTAG_ID", insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
        for media in recent_media:
            print(media)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_recent_media` method fetches recent media for the given hashtag.
- If the operation fails, it raises an appropriate error.
