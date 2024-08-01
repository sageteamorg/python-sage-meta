Fetching Hashtag Information
----------------------------

The `get_hashtag_info` method fetches information about a specific Instagram hashtag.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        hashtag_info = fb_client.hashtag_handler.get_hashtag_info(hashtag_id="HASHTAG_ID")
        print(hashtag_info)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_hashtag_info` method fetches information about the given Instagram hashtag.
- If the operation fails, it raises an appropriate error.
