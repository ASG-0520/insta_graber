import instaloader  # https://instaloader.github.io/module/instaloader.html?highlight=caption
from pathlib import Path

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


def download_post_shortcode(url_of_the_post):
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
    pass

