Method: `get_instagram_comments`
--------------------------------

This method fetches comments for a given Instagram media ID.

**Purpose:**
Fetches comments for a specified Instagram media.


.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        media_items = fb_client.media_handler.get_instagram_media(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
        for media in media_items:
            print(media.id)
        comments = fb_client.comment_handler.get_instagram_comments(media_id="MEDIA_ID")
        for comment in comments:
            print(dir(comment))
            print(comment.id)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_instagram_comments` method fetches comments for the given Instagram media ID.
- If the operation fails, it raises an appropriate error.

.. note::

    In the example 2 , it is shown how to get the Instagram business account ID.
