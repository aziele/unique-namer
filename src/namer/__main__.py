import argparse
import sys
from typing import Optional

import namer

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog='namer',
        description=f'namer v.{namer.__version__}: Generate unique, '
        'human-readable, and memorable names or identifiers',
        add_help=False
    )
    parser.add_argument(
        '-v', '--version',
        action='version',
        version=namer.__version__,
        help="Show the tool's version and exit"
    )
    parser.add_argument(
        '-h', '--help',
        action='help',
        help='Show this help message and exit'
    )
    # Subparsers
    subparsers = parser.add_subparsers(dest='command')
    # Stats subparser
    stats_parser = subparsers.add_parser(
        'stats',
        help='Show statistics on available categories and number of name '
            'combinations',
        add_help=False
    )
    # Generate subparser
    generate_parser = subparsers.add_parser(
        'generate',
        help='Generate unique names/IDs',
        add_help=False
    )
    generate_parser.add_argument(
        'count',
        type=int,
        help='Number of unique names/IDs to generate'
    )
    generate_parser.add_argument(
        '--category',
        action='append',
        choices=namer.list_categories(),
        metavar='<str>',
        default=[],
        help='Category to generate names from. Can be specified multiple '
            'times. Default to all categories.'
    )
    generate_parser.add_argument(
        '--suffix_length',
        type=int,
        metavar='<int>',
        default=0,
        help='Length of the optional random suffix. Set to 0 for no suffix '
           '[default: %(default)s]'
    )
    generate_parser.add_argument(
        '--separator',
        metavar='<str>',
        default='-',
        help='Separator between the words in name/ID '
            '[default: %(default)s]'
    )
    generate_parser.add_argument(
        '--style',
        choices=('lowercase', 'uppercase', 'title'),
        default='lowercase',
        help='Text style for the generated name [default: %(default)s]'
    )
    # Show help message if the script is run without any arguments.
    if len(sys.argv[1:]) == 0:
        parser.print_help()
        parser.exit()

    # Show the generate subparser help message
    # if it is run without any arguments.
    if sys.argv[-1] == 'generate':
        generate_parser.print_help()
        parser.exit()

    return parser


def print_stats_table(column_separator: Optional[str] = '  ') -> None:
    """
    Print a table with statistics for each category.

    Args:
        separator (str, optional): Separator used to separate columns in 
            the table. Defaults to two spaces.
    """
    # Get stats
    stats = namer.stats()

    # Determine column widths
    category_width = max(len(category) for category in stats)
    example_name_width = max(len(stat.example_name) for stat in stats.values())
    nouns_width = 5
    combinations_width = 10

    # Table header
    header = [
        f"{'Category':{category_width}}",
        f"{'Nouns':{nouns_width}}",
        f"{'Example':{example_name_width}}",
        f"{'Name_combs':>{combinations_width}}",
        f"{'ID_combs (4-char suffix)':}"
    ]
    print(column_separator.join(header))

    # Table body
    for category, stat in stats.items():
        row = [
            f"{category:{category_width}}",
            f"{stat.noun_count:{nouns_width}}",
            f"{stat.example_name:{example_name_width}}",
            f"{stat.name_combinations:>{combinations_width},}",
            f"{stat.id_combinations:.0e}"
        ]
        print(column_separator.join(row))


def main():
    parser = get_parser()
    args = parser.parse_args()

    if args.command == 'stats':
        print_stats_table()
    elif args.command == 'generate':
        for i in range(args.count):
            name = namer.generate(
                category=args.category,
                suffix_length=args.suffix_length,
                separator=args.separator,
                style=args.style
            )
            print(name)



if __name__ == '__main__':
    main()