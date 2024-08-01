# python-sage-meta
![Black](https://img.shields.io/badge/code%20style-black-000000.svg)
![Pylint](https://img.shields.io/badge/pylint-9-brightgreen)
[![codecov](https://codecov.io/gh/sageteamorg/python-sage-meta/graph/badge.svg?token=I10LGK910X)](https://codecov.io/gh/sageteamorg/python-sage-meta)

![PyPI release](https://img.shields.io/pypi/v/python-sage-meta "python-sage-meta")
![Supported Python versions](https://img.shields.io/pypi/pyversions/python-sage-meta "python-sage-meta")
![Documentation](https://img.shields.io/readthedocs/python-sage-meta "python-sage-meta")
![License](https://img.shields.io/badge/license-MIT-red)
![GitHub last commit](https://img.shields.io/github/last-commit/sageteamorg/python-sage-meta)

## Table of Contents
- [python-sage-meta](#python-sage-meta)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Configuration](#configuration)
    - [Single User Configuration](#single-user-configuration)
    - [Multi-User Configuration](#multi-user-configuration)
  - [Examples](#examples)
    - [Example 1: Account Management](#example-1-account-management)
    - [Example 2: Media Management](#example-2-media-management)
    - [Example 3: Content Publishing](#example-3-content-publishing)
  - [License](#license)

## Introduction
`python-sage-meta` is a comprehensive Python package designed to simplify the management of Facebook and Instagram operations through the Facebook Graph API. It provides easy-to-use interfaces for managing accounts, media, comments, hashtags, content publishing, and product tagging. This package is ideal for developers looking to integrate social media functionalities into their applications seamlessly.

## Features
- Account management for Facebook and Instagram accounts
- Media management for uploading and handling Instagram photos, videos, and carousels
- Comment management for Instagram comments, mentions, and replies
- Hashtag management for searching and retrieving hashtag information
- Content publishing for Instagram photos, videos, and carousels
- Product tagging for Instagram media

## Installation
To install `python-sage-meta`, use pip:
```bash
pip install python-sage-meta
```

## Configuration

The sage_meta package requires certain configuration variables to establish and manage interactions with the Facebook Graph API effectively.

This library offers flexibility to accommodate both single-user and multi-user scenarios:

  - **Single User Configuration**: If you are integrating this library into a Django application or any other single-user setup, you can define the necessary variables within your application's settings. This approach ensures that the configuration behaves as a single user, maintaining a consistent and straightforward setup.

 - **Multi-User Configuration**: For applications requiring support for multiple users, such as a web application with various user accounts, the library allows you to dynamically change the configuration variables upon each instantiation. This flexibility ensures that each user can have their own Facebook Graph API settings, enabling personalized social media management.

Configuration Variables

To configure the sage_meta package, you need to set the following variables:

  Access Token: The Facebook Graph API access token used for authentication.

Example Configuration

Here is an example of how to set up these variables in your project:

```python
  ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
```
### Single User Configuration

For a single-user setup, you can configure the sage_meta package as follows:

```python

    import sage_meta

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

    fb_client = sage_meta.FacebookClient(
        access_token=ACCESS_TOKEN
    )
```
### Multi-User Configuration

For multi-user applications, you can dynamically configure the sage_meta package upon each instantiation:

```python

    import sage_meta

    class UserService:
        def __init__(self, user_access_token):
            self.fb_client = sage_meta.FacebookClient(
                access_token=user_access_token
            )

        def get_user_data(self):
            return self.fb_client.get_user_data()

    # Example usage
    user_service = UserService("USER_SPECIFIC_ACCESS_TOKEN")
    user_data = user_service.get_user_data()
```
This example demonstrates how to dynamically configure the package for different users, ensuring personalized management of Facebook and Instagram operations for each user.

Ensure that your configuration is securely managed, especially the access tokens, to prevent unauthorized access to your Facebook and Instagram accounts.


## Examples

### Example 1: Account Management

This example demonstrates how to manage Facebook and Instagram accounts using the `AccountHandler` class.

```python
from sage_meta.services.base import FacebookClient

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
fb_client = FacebookClient(access_token=ACCESS_TOKEN)
accounts = fb_client.account_handler.get_accounts()
for account in accounts:
    print(account.name)
```

### Example 2: Media Management

This example demonstrates how to manage media for Instagram using the `MediaHandler` class.

```python
from sage_meta.services.base import FacebookClient

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
fb_client = FacebookClient(access_token=ACCESS_TOKEN)
media_items = fb_client.media_handler.get_instagram_media(insta_id="INSTAGRAM_BUSINESS_ACCOUNT_ID")
for media in media_items:
    print(media.caption)
```


### Example 3: Content Publishing

This example demonstrates how to publish content to Instagram using the `ContentPublishing` class.

```python
from sage_meta.services.base import FacebookClient

ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"
fb_client = FacebookClient(access_token=ACCESS_TOKEN)
publish_response = fb_client.content_publisher.publish_photo(
    image_url="https://example.com/image.jpg",
    caption="This is an example caption."
)
print(publish_response)
```

## License
This project is licensed under the MIT License.
