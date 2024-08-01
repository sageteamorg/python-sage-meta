Fetching Instagram Media
------------------------

The `get_instagram_media` method fetches Instagram media for a given Instagram account ID.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        media_items = fb_client.media_handler.get_instagram_media(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
        for media in media_items:
            print(media.caption)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_instagram_media` method fetches media items for the given Instagram account ID.
- If the operation fails, it raises an appropriate error.

.. note::
    
    In the previous example, it is shown how to get the Instagram business account ID.
