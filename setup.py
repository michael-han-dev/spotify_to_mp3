from setuptools import setup, find_packages

requires = [
    'flask',
    'spotipy',
    'html5lib',
    'requests',
    'requests_html',
    'beautifulsoup4',
    'youtube_dl',
    'pathlib',
    'pandas'
]

setup(
    name='SpotifyToYoutubeMP3',
    version='1.0',
    description='An application that gets your Spotify songs and downloads the Youtube MP3 version',
    author='Michael Han',
    author_email='hanmichael82@gmail.com',
    keywords='web flask',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requires
)