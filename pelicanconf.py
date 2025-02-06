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
# BANNER = 'atasattari.github.io/content/pictures/Ata_wide.png'
# BANNER_SUBTITLE = 'This is my subtitle'
HIDE_SIDEBAR = False
# BOOTSTRAP_NAVBAR_INVERSE = True

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
    ("SuperCDMS", "https://supercdms.slac.stanford.edu/"),
    ("SNOLAB", "https://www.snolab.ca/"),
    ("McDonald Institute", "https://mcdonaldinstitute.ca/"),
)

# Social widget
SOCIAL = (
    ("Linkdin", "https://www.linkedin.com/in/ata-sattari"),
    ("Gmail", "mailto:atasattari@gmail.com")
    )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True