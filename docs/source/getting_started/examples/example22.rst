Replying to a Comment
---------------------

The `reply_to_comment` method replies to a comment.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        comment_id = "YOUR_COMMENT_ID"
        message = "This is a reply."
        reply = fb_client.content_publisher.reply_to_comment(comment_id=comment_id, message=message)
        print(reply)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `reply_to_comment` method replies to a given comment ID.
- If the operation fails, it raises an appropriate error.
