Posting a Comment
-----------------

The `put_comment` method posts a comment to a post.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        post_id = "YOUR_POST_ID"
        message = "This is a comment."
        media_items = fb_client.media_handler.get_instagram_media(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
        for media in media_items:
            print(media.id)
        comment = fb_client.content_publisher.put_comment(post_id=post_id, message=message)
        print(comment)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `put_comment` method posts a comment to a given post ID.
- If the operation fails, it raises an appropriate error.
