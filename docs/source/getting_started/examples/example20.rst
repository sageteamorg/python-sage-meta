Fetching Account Settings
-------------------------

The `get_account_settings` method fetches the settings of an Instagram account.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        settings = fb_client.account_handler.get_account_settings(instagram_account_id="INSTAGRAM_ACCOUNT_ID")
        print(settings)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_account_settings` method fetches the settings of the given Instagram account.
- If the operation fails, it raises an appropriate error.
