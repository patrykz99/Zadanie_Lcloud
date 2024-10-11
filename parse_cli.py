from s3_cli_fcns import list_files_s3,upload_local_file_s3,list_files_with_regex_s3,delete_files_with_regex_s3
import argparse


def parse_cli():
    parser = argparse.ArgumentParser(
        description='CLI to list all files,\
                    upload file from local,\
                    filter with matching patter\
                    and delete with matching pattern')
    
    subparsers = parser.add_subparsers(dest='command')
 
    subparsers.add_parser('list', help='List all files')
    
    upload_parser = subparsers.add_parser('-upload', help='Upload a local file')
    upload_parser.add_argument('-local_file_path', type=str, help='Path to the local file')
    upload_parser.add_argument('-key_file_name', type=str, help='File name to save in the bucket')
    
    filter_list_parser = subparsers.add_parser('-filter-list', help='Filter files')
    filter_list_parser.add_argument('-pattern', type=str, help='Pattern to filter')
    
    delete_parser = subparsers.add_parser('-delete-files', help='Delete files with proper pattern')
    delete_parser.add_argument('-pattern', type=str, help='Pattern to delete')
    
    args = parser.parse_args()
    
    # Call appropriate function based on command
    if args.command == 'list':
        list_files_s3()
    elif args.command == 'upload':
        upload_local_file_s3(args.local_file_path, args.key_file_name)
    elif args.command == 'filter-list':
        list_files_with_regex_s3(args.pattern)
    elif args.command == 'delete-files':
        delete_files_with_regex_s3(args.pattern)
    else:
        parser.print_help()
