AUTHOR = 'Ata Sattari'
SITENAME = 'Ata Sattari'
SITEURL = ""

PATH = "content"
ARTICLE_PATHS = ['posts']

TIMEZONE = 'America/Toronto'

THEME = '/home/ata/my_website/pelican-themes/pelican-bootstrap3'
DEFAULT_LANG = 'en'
BOOTSTRAP_THEME = 'flatly'
# LOAD_CONTENT_CACHE = False
DISPLAY_PAGES_ON_MENU = True
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
# HIDE_SITENAME =True
# ABOUT_ME = '1232342354353465346'
BANNER = './content/posts/pictures/image.png'
BANNER_SUBTITLE = 'This is my subtitle'
HIDE_SIDEBAR = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
PLUGIN_PATHS = ['../pelican-plugins'] 
PLUGINS = ['i18n_subsites',"render_math"]
STATIC_PATHS = ['pictures']
# MATH_JAX = {'color':'black','align':'center'}

# Blogroll
LINKS = (
    ("LinkdIN", "www.linkedin.com/in/ata-sattari"),
    # ("Python.org", "https://www.python.org/"),
    # ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    # ("You can modify those links in your config file", "#"),
)

# Social widget
# SOCIAL = (
#     ("You can add links in your config file", "#"),
#     ("Another social link", "#"),
# )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True