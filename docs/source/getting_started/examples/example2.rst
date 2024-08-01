Method: `get_accounts`
----------------------

This method fetches the user's Facebook pages and their linked Instagram business accounts.

**Purpose:**
Fetches the user's Facebook pages and automatically retrieves the linked Instagram business account IDs.


.. code-block:: python

    try:
        from sage_meta.services.base import FacebookClient

        ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
        fb_client = FacebookClient(access_token=ACCESS_TOKEN)
        accounts = fb_client.account_handler.get_accounts()
        for account in accounts:
            if account.instagram_business_account:
                print(f"Instagram Business Account ID for {account.name}: {account.instagram_business_account.id}")
            else:
                print(f"No Instagram Business Account linked for {account.name}")
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `get_accounts` method fetches the user's Facebook pages and retrieves the linked Instagram business account IDs.
- If the operation fails, it raises an appropriate error.
