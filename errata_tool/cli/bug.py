from errata_tool.bug import Bug


def add_parser(subparsers):
    """
    Add build parser to this top-level subparsers object.
    """
    group = subparsers.add_parser('bug', help='Bugzilla information')

    # build-level sub-commands:
    sub = group.add_subparsers(dest='bug_subcommand')
    sub.required = True

    # "get"
    get_parser = sub.add_parser('get')
    get_parser.add_argument('id', help='bugzilla id of given '
                                        'bug')
    get_parser.set_defaults(func=get)

    get_all_parser = sub.add_parser('get_all_advisory_ids')
    get_all_parser.add_argument('id', help='bugzilla id of given '
                                        'bug')
    get_all_parser.set_defaults(func=get_all_advisory_ids)


def get(args):
    """
    Get information about build

    :param args: parsed cli arguments
    """
    build = Bug(args.id)
    print(build)


def get_all_advisory_ids(args):
    """
    Get information about build

    :param args: parsed cli arguments
    """
    build = Bug(args.id)
    for id in build.all_advisory_ids:
        print(id)