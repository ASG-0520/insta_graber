import instaloader  # https://instaloader.github.io/module/instaloader.html?highlight=caption
from settings import log, pas

"""
:param post_metadata_txt_pattern = "": comment on the post
:param download_geotags = False
:param save_metadata = False
:param save_metadata_json = False
:param download_comments = False
"""

L = instaloader.Instaloader(save_metadata=False)
L.post_metadata_txt_pattern = ""

print('Logging into the instagramm account....')
L.login(log, pas)
# L.interactive_login(log)
print('Login successful! \n-------------')


def download_post_shortcode():
    """
    Download everything associated with one instagram post node, i.e. picture, caption and video.

    post: Post to download.
    target: Target name, i.e. profile name, #hashtag, :feed; for filename.
    :return: True if something was downloaded, False otherwise, i.e. file was already there
    """
    post_target = input('Enter the URL of the post: ').split('/')[4]
    print("Searching and downloading, plz wait...")
    post = instaloader.Post.from_shortcode(L.context, post_target)
    L.download_post(post=post, target=post_target)


def download_update_profile():
    L.post_metadata_txt_pattern = ""
    profile_name = input('Enter the Username of the target: ')
    print("Searching and downloading, plz wait...")
    L.download_profile(profile_name=profile_name, fast_update=True)


def download_top_x_posts():
    """ It is easy to download the few most-liked pictures of a user in percentage of posts. """
    from itertools import islice
    from math import ceil

    profile_to_download_from = input("'Enter the Username profile: ")
    print("Searching and downloading, plz wait...")
    x_percentage = 0.1  # percentage of posts that should be downloaded
    profile = instaloader.Profile.from_username(L.context, profile_to_download_from)
    posts_sorted_by_likes = sorted(profile.get_posts(),
                                   key=lambda p: p.likes + p.comments,
                                   reverse=True)

    for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * x_percentage / 100)):
        L.download_post(post, profile_to_download_from)


if __name__ == '__main__':
    download_update_profile()
  # download_post_shortcode()
  # download_top_x_posts()


