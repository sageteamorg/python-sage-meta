Fetching Post Mentions
----------------------

The `get_post_mentions` method fetches data about media posts where the Instagram user is mentioned in the caption.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        media_items = fb_client.media_handler.get_instagram_media(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
        for media in media_items:
            print(media.id)
    
        post_mention = fb_client.comment_handler.get_post_mentions(insta="INSTAGRAM_ACCOUNT_ID", media_id="MEDIA_ID")
        if post_mention:
            print(post_mention.caption)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_post_mentions` method fetches data about media posts where the Instagram user is mentioned in the caption.
- If the operation fails, it raises an appropriate error.
