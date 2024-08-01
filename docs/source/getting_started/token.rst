Obtaining an Access Token
=========================

To use the functionalities of Facebook and Instagram, you need to obtain an access token. Follow these steps to get started.

.. warning::
   Your Instagram account **must** be a business account; otherwise, it will not work with this package.

.. warning::
   Your both facebook and instagram accounts **must** be verified by facebook.


Step-by-Step Guide
------------------

1. **Go to the Graph API Explorer**

   - Navigate to the `Facebook for Developers <https://developers.facebook.com/>`_ website and log in.
   - In the top navigation bar, click on **Tools** and then select **Graph API Explorer**.
   - or Go to the Instagram product settings in your app dashboard.
   - Click on Generate Token to start the token generation process.

2. **Select Your App**

   - In the Graph API Explorer, select your app from the dropdown menu.

3. **Generate Access Token**

   - Click on **Get Token**.
   - Select **Get User Access Token**.
   - In the popup, select the necessary permissions for your app's functionality:
   - instagram_basic**
   - instagram_manage_insights
   - instagram_manage_comments
   - pages_show_list
   - pages_read_engagement
   - Click **Generate Access Token**.
   
   .. note::
      For detailed information on the permissions required, refer to the :ref:`permissions`.


4. **Complete Authorization**

   - You will be redirected to a Facebook login page.
   - Log in with the Facebook account that has the necessary permissions.
   - Follow the prompts to grant the requested permissions.

5. **Retrieve Access Token**

   - After authorization, you will receive an access token.
   - Copy and save this token securely as it will be used to authenticate API requests.

.. note::
   By following these steps, you will have successfully obtained an access token that you can use to integrate your app with Facebook and Instagram.

Managing Permissions
--------------------

Permissions define what data and actions your app can access. Here are some key permissions and their purposes:

.. list-table:: Key Permissions
   :widths: 20 80
   :header-rows: 1

   * - Permission
     - Description
   * - **instagram_basic**
     - Allows reading of basic Instagram account information.
   * - **instagram_manage_insights**
     - Provides access to insights data, including metrics for media and stories.
   * - **instagram_manage_comments**
     - Grants the ability to manage comments on media.
   * - **pages_show_list**
     - Lists all the Facebook pages managed by the user.
   * - **pages_read_engagement**
     - Accesses engagement metrics for pages, such as likes, comments, and shares.

.. important::
   Request only the permissions necessary for your app's functionality to ensure user trust and compliance with Facebook policies.
