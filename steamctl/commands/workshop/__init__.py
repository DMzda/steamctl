
from steamctl.argparser import register_command
from steamctl.utils.storage import UserDataFile, UserCacheFile
from argcomplete import warn


epilog = """\

Examples:

    Search for any item in the workshop:
        {prog} workshop search dust 2

    Search for Dota 2 custom games:
        {prog} workshop search --appid 570 --tag 'Custom Game' auto chess

    Downlaod workshop files, such as Dota 2 custom maps or CSGO maps:
        {prog} workshop download 12345678

"""

@register_command('workshop', help='Search and download workshop items', epilog=epilog)
def cmd_parser(cp):
    def print_help(*args, **kwargs):
        cp.print_help()

    cp.set_defaults(_cmd_func=print_help)

    sub_cp = cp.add_subparsers(metavar='<subcommand>',
                               dest='subcommand',
                               title='List of sub-commands',
                               description='',
                               )

    scp_q = sub_cp.add_parser("search", help="Search the workshop")
    scp_q.add_argument('--apikey', type=str, help='WebAPI key to use')
    scp_q.add_argument('-a', '--appid', type=int, help='Filter by AppID')
    scp_q.add_argument('-t', '--tag', type=str, action='append', help='Filter by tags')
    scp_q.add_argument('-d', '--downloable', action='store_true', help='Show only downloable results')
    scp_q.add_argument('--match_all_tags', action='store_true', help='All tags must match')
    scp_q.add_argument('-n', '--numresults', type=int, default=20, help='Number of results (default: 20)')
    scp_q.add_argument('search_text', nargs='+', metavar='search_text', type=str, help='Text to search in the workshop')
    scp_q.set_defaults(_cmd_func=__name__ + '.cmds:cmd_workshop_search')

    scp_dl = sub_cp.add_parser("download", help="Download a workshop item")
    scp_dl.add_argument('--apikey', type=str, help='WebAPI key to use')
    scp_dl.add_argument('--anonymous', action='store_true', help='Anonymous Steam login')
    scp_dl.add_argument('--user', type=str, help='Username for Steam login')
    scp_dl.add_argument('--cell_id', type=int, help='Cell ID to use for download')
    scp_dl.add_argument('-o', '--output', type=str, default='', help='Path to directory for the downloaded files (default: cwd)')
    scp_dl.add_argument('-nd', '--no-directories', action='store_true', help='Do not create directories')
    scp_dl.add_argument('-np', '--no-progress', action='store_true', help='Do not create directories')
    scp_dl.add_argument('id', type=int, help='Workshop item ID')
    scp_dl.set_defaults(_cmd_func=__name__ + '.gcmds:cmd_workshop_download')
