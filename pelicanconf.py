# pelicanconf.py

AUTHOR = 'ThatAuskeGuy'
SITENAME = 'ThatAuskeGuy'
SITEURL = ""  # Empty for local dev

PATH = "content"
ARTICLE_PATHS = ['posts']
PAGE_PATHS = ['pages']

TIMEZONE = 'America/Chicago'
DEFAULT_LANG = 'en'

# Theme settings
THEME = 'themes/thatausketech'

# Site subtitle
SITESUBTITLE = "~/dev_and_stuff $"

# Menu items (edit or remove as you like)
MENUITEMS = (
    ('Home', '/'),
    ('Dev Blog', '/category/dev-blog.html'),
    ('Beyond the Terminal', '/category/beyond-the-terminal.html'),
    ('Projects', '/pages/projects.html'),
    ('About Me', '/pages/about-me.html'),
    ('Contact Me', '/pages/contact-me.html'),
)

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Feed settings (disable locally)
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll / Social (edit or remove as you like)
LINKS = ()
SOCIAL = (
    ('GitHub', 'https://github.com/ThatAuskeGuy'),
)

DEFAULT_PAGINATION = 10

# Static files (CNAME for custom domain goes here later)
STATIC_PATHS = ['extra']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/favicon-16x16.png': {'path': 'favicon-16x16.png'},
    'extra/favicon-32x32.png': {'path': 'favicon-32x32.png'},
    'extra/avatar.png': {'path': 'avatar.png'},
    'extra/404.html': {'path': '404.html'},
}

RELATIVE_URLS = True