Fetching Instagram Stories
--------------------------

The `get_instagram_stories` method fetches Instagram stories for a given Instagram account ID.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        stories = fb_client.story_handler.get_instagram_stories(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
        for story in stories:
            print(story.media_url)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_instagram_stories` method fetches stories for the given Instagram account ID.
- If the operation fails, it raises an appropriate error.
