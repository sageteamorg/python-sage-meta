Publishing a Carousel to Instagram
----------------------------------

The `publish_carousel` method publishes a carousel to Instagram.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        media_urls = [
            "https://example.com/image1.jpg",
            "https://example.com/image2.jpg"
        ]
        fb_client.account_handler.get_accounts()
        publish_response = fb_client.content_publisher.publish_carousel(
            media_urls=media_urls,
            caption="This is an example carousel."
        )
        print(publish_response)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `publish_carousel` method publishes a carousel to Instagram using the provided media URLs and caption.
- If the operation fails, it raises an appropriate error.
