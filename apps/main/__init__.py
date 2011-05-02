from django.utils.translation import ugettext_lazy as _

from navigation.api import register_menu

from permissions import role_list

from documents import document_find_all_duplicates
from filesystem_serving import filesystem_serving_recreate_all_links
from ocr import all_document_ocr_cleanup
from user_management import user_list

from main.conf.settings import SIDE_BAR_SEARCH

check_settings = {'text': _(u'settings'), 'view': 'check_settings', 'famfam': 'cog'}
statistics = {'text': _(u'statistics'), 'view': 'statistics', 'famfam': 'table'}
diagnostics = {'text': _(u'diagnostics'), 'view': 'diagnostics', 'famfam': 'pill'}

__version_info__ = {
    'major': 0,
    'minor': 5,
    'micro': 1,
    'releaselevel': 'final',
    'serial': 0
}

def get_version():
    """
    Return the formatted version information
    """
    vers = ["%(major)i.%(minor)i" % __version_info__, ]
    
    if __version_info__['micro']:
        vers.append(".%(micro)i" % __version_info__)
    if __version_info__['releaselevel'] != 'final':
        vers.append('%(releaselevel)s%(serial)i' % __version_info__)
    return ''.join(vers)

__version__ = get_version()


main_menu = [
    {'text': _(u'home'), 'view': 'home', 'famfam': 'house', 'position': 0},
    {'text': _(u'tools'), 'view': 'tools_menu', 'links': [
        document_find_all_duplicates, filesystem_serving_recreate_all_links,
        all_document_ocr_cleanup, statistics, diagnostics,
        ], 'famfam': 'wrench', 'name': 'tools', 'position': 7},

    {'text': _(u'setup'), 'view': 'check_settings', 'links': [
        check_settings, role_list, user_list
        ], 'famfam': 'cog', 'name': 'setup', 'position': 8},

    {'text': _(u'about'), 'view': 'about', 'position': 9},
]

if not SIDE_BAR_SEARCH:
    main_menu.insert(1, {'text': _(u'search'), 'view': 'search', 'famfam': 'zoom', 'position': 2})

register_menu(main_menu)
