Fetching User Data
------------------

The user's data from Facebook is fetched by the `get_user_data` method.

**Example:**

.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        user_data = fb_client.get_user_data()
        print(user_data)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The user's data from Facebook is fetched by the `get_user_data` method.
- If the operation fails, an appropriate error is raised.

.. note::

    It will return None because this is done automatically when creating the class.
