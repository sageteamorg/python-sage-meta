Publishing a Photo to Instagram
-------------------------------

The `publish_photo` method publishes a photo to Instagram.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        fb_client.account_handler.get_accounts()
        publish_response = fb_client.content_publisher.publish_photo(
            image_url="https://example.com/image.jpg",
            caption="This is an example caption."
        )
        print(publish_response)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `publish_photo` method publishes a photo to Instagram using the provided image URL and caption.
- If the operation fails, it raises an appropriate error.

.. note::

    Since we do not provide the Instagram business account ID here, the `get_accounts` method must be executed to ensure the code can retrieve the Instagram account ID.