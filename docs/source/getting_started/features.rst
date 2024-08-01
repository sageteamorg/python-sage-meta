Features
========

The **sage_meta** package offers a variety of features to help manage Facebook and Instagram operations efficiently:

- **Account Management**: Manage Facebook and Instagram accounts.
- **Media Management**: Upload and handle Instagram photos, videos, and carousels.
- **Comment Management**: Manage Instagram comments, mentions, and replies.
- **Hashtag Management**: Search and retrieve hashtag information.
- **Content Publishing**: Publish photos, videos, and carousels to Instagram.
- **Product Tagging**: Tag products in Instagram media.

Account Management for Facebook and Instagram
---------------------------------------------

The `AccountHandler` class provides methods to manage Facebook accounts and their linked Instagram business accounts. It allows you to fetch account information and handle various account-related operations.

Media Management for Instagram
------------------------------

The `MediaHandler` class offers comprehensive media management for Instagram. It supports uploading photos and videos, handling carousels, and retrieving media information.

Comment Management for Instagram
--------------------------------

The `CommentHandler` class enables the management of Instagram comments, including fetching comments, replying to mentions, and handling comment mentions.

Hashtag Management for Instagram
--------------------------------

The `HashtagHandler` class allows searching for hashtags, retrieving hashtag information, and fetching recent and top media for a given hashtag.

Content Publishing to Instagram
-------------------------------

The `ContentPublishing` class provides methods for publishing photos, videos, and carousels to Instagram. It handles media creation, publication, and status retrieval.

Product Tagging for Instagram Media
-----------------------------------

The `InstagramProductTagging` class supports tagging products in Instagram media, managing product tags, and retrieving product information.

Examples
--------

Account Management Example
---------------------------

.. code-block:: python

    from sage_meta.services.base import FacebookClient

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    fb_client = FacebookClient(access_token=ACCESS_TOKEN)
    accounts = fb_client.account_handler.get_accounts()
    for account in accounts:
        print(account.name)

Media Management Example
------------------------

.. code-block:: python

    from sage_meta.services.base import FacebookClient

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    fb_client = FacebookClient(access_token=ACCESS_TOKEN)
    media_items = fb_client.media_handler.get_instagram_media(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
    for media in media_items:
        print(media.caption)

Comment Management Example
--------------------------

.. code-block:: python

    from sage_meta.services.base import FacebookClient

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    fb_client = FacebookClient(access_token=ACCESS_TOKEN)
    comments = fb_client.comment_handler.get_instagram_comments(media_id="MEDIA_ID")
    for comment in comments:
        print(comment.text)

Hashtag Management Example
--------------------------

.. code-block:: python

    from sage_meta.services.base import FacebookClient

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    fb_client = FacebookClient(access_token=ACCESS_TOKEN)
    hashtag_id = fb_client.hashtag_handler.search_hashtag(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID", query="example")
    hashtag_info = fb_client.hashtag_handler.get_hashtag_info(hashtag_id=hashtag_id)
    print(hashtag_info)

Content Publishing Example
--------------------------

.. code-block:: python

    from sage_meta.services.base import FacebookClient

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    fb_client = FacebookClient(access_token=ACCESS_TOKEN)
    publish_response = fb_client.content_publisher.publish_photo(
        image_url="https://example.com/image.jpg",
        caption="This is an example caption."
    )
    print(publish_response)

Product Tagging Example
-----------------------

.. code-block:: python

    from sage_meta.services.base import FacebookClient

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
    fb_client = FacebookClient(access_token=ACCESS_TOKEN)
    product_tagging = fb_client.product_tagging

    # Example of creating a tagged container
    response = product_tagging.create_tagged_container(
        ig_user_id="INSTAGRAM_BUSINESS_ACCOUNT_ID",
        media_type="IMAGE",
        media_url="https://example.com/product.jpg",
        product_tags=[{"product_id": "123456789", "x": 0.5, "y": 0.5}],
        caption="Check out this product!"
    )
    print(response)

These examples demonstrate how to use the `sage_meta` package to manage various aspects of Facebook and Instagram operations effectively.
