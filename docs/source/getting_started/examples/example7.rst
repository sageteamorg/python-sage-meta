Fetching Comment Mentions
-------------------------

The `get_comment_mentions` method fetches data about comments in which the account has been mentioned.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        comment_mention = fb_client.comment_handler.get_comment_mentions(insta="INSTAGRAM_ACCOUNT_ID", comment_id="COMMENT_ID")
        if comment_mention:
            print(comment_mention.text)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_comment_mentions` method fetches data about comments in which the account has been mentioned.
- If the operation fails, it raises an appropriate error.
