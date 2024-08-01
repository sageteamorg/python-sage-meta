Publishing a Story
------------------

The `publish_story` method publishes a story to Instagram.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        fb_client.account_handler.get_accounts()
        image_url = "https://example.com/story.jpg"
        publish_response = fb_client.content_publisher.publish_story(image_url=image_url)
        print(publish_response)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `publish_story` method publishes a story to Instagram using the provided image URL.
- If the operation fails, it raises an appropriate error.
