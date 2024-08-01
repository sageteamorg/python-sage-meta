Managing Copyright Information
------------------------------

The `CopyrightManager` class manages copyright information via the Facebook Graph API.

**Initialization:**

.. code-block:: python

    from sage_meta.services.copyright import CopyrightManager

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    copyright_manager = CopyrightManager(access_token=ACCESS_TOKEN)

**Checking Copyright Status of Unpublished Videos:**

.. code-block:: python

    try:
        container_id = "YOUR_CONTAINER_ID"
        status = copyright_manager.check_copyright_status_unpublished(container_id=container_id)
        print(status)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Checking Copyright Status of Published Videos:**

.. code-block:: python

    try:
        media_id = "YOUR_MEDIA_ID"
        status = copyright_manager.check_copyright_status_published(media_id=media_id)
        print(status)
    except Exception as e:
        logging.critical("An error occurred: %s", e)

**Explanation:**
- The `CopyrightManager` class manages copyright information via the Facebook Graph API.
- The `check_copyright_status_unpublished` method checks the copyright status of an uploaded but not yet published video using the given container ID.
- The `check_copyright_status_published` method checks the copyright status of a published video using the given media ID.
- If the operation fails, it raises an appropriate error.
