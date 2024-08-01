Configuration Guide
===================

Configuration
-------------

The sage_meta package requires certain configuration variables to establish and manage interactions with the Facebook Graph API effectively.

This library offers flexibility to accommodate both single-user and multi-user scenarios:

- **Single User Configuration**: If you are integrating this library into a Django application or any other single-user setup, you can define the necessary variables within your application's settings. This approach ensures that the configuration behaves as a single user, maintaining a consistent and straightforward setup.

- **Multi-User Configuration**: For applications requiring support for multiple users, such as a web application with various user accounts, the library allows you to dynamically change the configuration variables upon each instantiation. This flexibility ensures that each user can have their own Facebook Graph API settings, enabling personalized social media management.

Configuration Variables

To configure the sage_meta package, you need to set the following variables:

- **Access Token**: The Facebook Graph API access token used for authentication.

Example Configuration

Here is an example of how to set up these variables in your project:

.. code-block:: python

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

Single User Configuration

For a single-user setup, you can configure the sage_meta package as follows:

.. code-block:: python

    import sage_meta

    ACCESS_TOKEN = "YOUR_ACCESS_TOKEN"

    fb_client = sage_meta.FacebookClient(
        access_token=ACCESS_TOKEN
    )

Multi-User Configuration

For multi-user applications, you can dynamically configure the sage_meta package upon each instantiation:

.. code-block:: python
    
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

This example demonstrates how to dynamically configure the package for different users, ensuring personalized management of Facebook and Instagram operations for each user.

Ensure that your configuration is securely managed, especially the access tokens, to prevent unauthorized access to your Facebook and Instagram accounts.
