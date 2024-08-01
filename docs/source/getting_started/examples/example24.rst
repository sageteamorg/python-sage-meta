Data Classes Examples
=====================

This section provides examples of how to use the data classes defined in the `sage_meta` package and how they arrange values.

Category
--------

The `Category` class represents a category with an ID and a name.

**Example:**

.. code-block:: python

    from sage_meta.models import Category

    # Creating a Category instance
    category = Category(id="1", name="Technology")
    print(category.id)  # Output: 1
    print(category.name)  # Output: Technology

Insight
-------

The `Insight` class represents an insight with various attributes such as ID, name, period, values, title, and description.

**Example:**

.. code-block:: python

    from sage_meta.models import Insight

    # Creating an Insight instance
    insight = Insight(
        id="insight1",
        name="Audience Insight",
        period="day",
        values=[{"metric": "reach", "value": "1000"}],
        title="Daily Audience Insight",
        description="Insights about daily audience reach."
    )
    print(insight.id)  # Output: insight1
    print(insight.values)  # Output: [{'metric': 'reach', 'value': '1000'}]

Comment
-------

The `Comment` class represents a comment with attributes such as ID, text, username, like count, timestamp, and additional data.

**Example:**

.. code-block:: python

    from sage_meta.models import Comment

    # Creating a Comment instance
    comment = Comment(
        id="comment1",
        text="Nice post!",
        username="user123",
        like_count=5,
        timestamp="2023-07-28T12:34:56Z",
        additional_data={"location": "New York"}
    )
    print(comment.text)  # Output: Nice post!
    print(comment.additional_data)  # Output: {'location': 'New York'}

Media
-----

The `Media` class represents media with attributes such as ID, caption, media type, media URLs, timestamp, like count, comments count, comments, and additional data.

**Example:**

.. code-block:: python

    from sage_meta.models import Media, Comment

    # Creating a Media instance with comments
    comment1 = Comment(id="comment1", text="Great photo!", username="user123")
    comment2 = Comment(id="comment2", text="Love it!", username="user456")
    media = Media(
        id="media1",
        caption="Beautiful sunset",
        media_type="image",
        media_url=["http://example.com/sunset.jpg"],
        timestamp="2023-07-28T18:00:00Z",
        like_count=100,
        comments_count=2,
        comments=[comment1, comment2],
        additional_data={"location": "Beach"}
    )
    print(media.caption)  # Output: Beautiful sunset
    print(media.comments[0].text)  # Output: Great photo!

InstagramAccount
----------------

The `InstagramAccount` class represents an Instagram account with various attributes such as ID, username, follower counts, media, insights, stories, and additional data.

**Example:**

.. code-block:: python

    from sage_meta.models import InstagramAccount, Media, Insight, Story

    # Creating an InstagramAccount instance
    media_item = Media(id="media1", caption="A post", media_type="image", media_url=["http://example.com/image.jpg"])
    insight = Insight(id="insight1", name="Profile Views", period="day", values=[{"metric": "views", "value": "100"}])
    story = Story(id="story1", media_type="image", media_url="http://example.com/story.jpg")

    instagram_account = InstagramAccount(
        id="account1",
        username="my_account",
        follows_count=300,
        followers_count=1500,
        media_count=50,
        profile_picture_url="http://example.com/profile.jpg",
        website="http://example.com",
        biography="This is my bio.",
        media=[media_item],
        insights=[insight],
        stories=[story],
        additional_data={"business_account": True}
    )
    print(instagram_account.username)  # Output: my_account
    print(instagram_account.media[0].caption)  # Output: A post

FacebookPageData
----------------

The `FacebookPageData` class represents a Facebook page with attributes such as ID, name, category, access token, category list, tasks, Instagram business account, and additional data.

**Example:**

.. code-block:: python

    from sage_meta.models import FacebookPageData, Category, InstagramAccount

    # Creating a FacebookPageData instance
    category = Category(id="cat1", name="Tech")
    instagram_account = InstagramAccount(id="account1", username="my_instagram", follows_count=300, followers_count=1500, media_count=50)
    
    facebook_page = FacebookPageData(
        id="page1",
        name="My Facebook Page",
        category="Business",
        access_token="my_access_token",
        category_list=[category],
        tasks=["MANAGE"],
        instagram_business_account=instagram_account,
        additional_data={"verified": True}
    )
    print(facebook_page.name)  # Output: My Facebook Page
    print(facebook_page.instagram_business_account.username)  # Output: my_instagram

UserData
--------

The `UserData` class represents user data with attributes such as ID, name, email, pages, and additional data.

**Example:**

.. code-block:: python

    from sage_meta.models import UserData, FacebookPageData

    # Creating a UserData instance
    facebook_page = FacebookPageData(id="page1", name="My Facebook Page", category="Business", access_token="my_access_token")
    
    user_data = UserData(
        id="user1",
        name="John Doe",
        email="john.doe@example.com",
        pages=[facebook_page],
        additional_data={"premium_member": True}
    )
    print(user_data.name)  # Output: John Doe
    print(user_data.pages[0].name)  # Output: My Facebook Page
