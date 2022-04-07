import instaloader  # https://instaloader.github.io/module/instaloader.html?highlight=caption
from pathlib import Path

"""
Instaloader (Main Class)
:param post_metadata_txt_pattern = "": comment on the post
:param download_geotags = False
:param save_metadata = False
:param save_metadata_json = False
:param download_comments = False
"""

L = instaloader.Instaloader()

L.save_metadata = False  # json file
L.post_metadata_txt_pattern = ''  # post caption off (подпись поста)
L.download_geotags = False
L.download_comments = False
L.download_pictures = True
L.download_videos = True

d_path = Path.home() / 'Downloads' / 'Instaloader_downloads'
d_path.mkdir(parents=True, exist_ok=True)
L.dirname_pattern = str(d_path) + '/{target}'


def login(log, pas):
    print('Logging into the instagramm account....')
    L.login(log, pas)
    print('Login successful! \n-------------')


def download_post_shortcode(url_of_the_post):  # Enter the URL of the post:url_of_the_post
    """
    Download everything associated with one instagram post node, i.e. picture, caption and video.

    post: Post to download.
    target: Target name, i.e. profile name, #hashtag, :feed; for filename.
    :return: True if something was downloaded, False otherwise, i.e. file was already there
    """
    post_target = url_of_the_post.split('/')[4]
    # post_target = input('Enter the URL of the post: ').split('/')[4]
    # print("Searching and downloading, plz wait...")
    post = instaloader.Post.from_shortcode(L.context, post_target)
    L.download_post(post=post, target=post_target)
    print('Finished')


def download_profile(url_of_the_profile):
    # profile_name = input('Enter the Username of the target: ')
    # print("Searching and downloading, plz wait...")
    profile_name = url_of_the_profile.split('/')[3]
    print(profile_name)
    L.download_profile(profile_name=profile_name)


def update_profile(url_of_the_profile):
    # profile_name = input('Enter the Username of the target: ')
    # print("Searching and downloading, plz wait...")
    profile_name = url_of_the_profile.split('/')[3]
    L.download_profile(profile_name=profile_name, fast_update=True)


def download_top_x_posts(url_of_the_profile):
    """ It is easy to download the few most-liked posts. """
    t = 0
    profile_name = url_of_the_profile.split('/')[3]
    profile = instaloader.Profile.from_username(L.context, profile_name)
    posts_sorted_by_likes = sorted(profile.get_posts(), key=lambda p: p.likes, reverse=True)

    x = 5  # top 5
    while x != t:
        for post in posts_sorted_by_likes:
            L.download_post(post, profile_name)
            t += 1

