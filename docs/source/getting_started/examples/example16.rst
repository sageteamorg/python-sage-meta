Publishing a Video to Instagram
-------------------------------

The `publish_video` method publishes a video to Instagram.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        fb_client.account_handler.get_accounts()
        publish_response = fb_client.content_publisher.publish_video(
            video_url="https://example.com/video.mp4",
            caption="This is an example caption."
        )
        print(publish_response)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `publish_video` method publishes a video to Instagram using the provided video URL and caption.
- If the operation fails, it raises an appropriate error.
