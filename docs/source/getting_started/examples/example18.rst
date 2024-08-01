Fetching Instagram Account Insights
-----------------------------------

The `get_instagram_insights` method fetches insights for a given Instagram account ID.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        insights = fb_client.media_handler.get_instagram_insights(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")

        for insight in insights:
            print(f"{insight.name}: {insight.values}")
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_instagram_insights` method fetches insights for the given Instagram account ID.
- If the operation fails, it raises an appropriate error.
