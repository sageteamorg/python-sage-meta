Searching for a Hashtag
-----------------------

The `search_hashtag` method searches for a hashtag.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        hashtag_id = fb_client.hashtag_handler.search_hashtag(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID", query="example")
        print(hashtag_id)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `search_hashtag` method searches for a hashtag.
- If the operation fails, it raises an appropriate error.
