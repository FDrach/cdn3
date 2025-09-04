import os

IGNORE_DIRS = ('.git', '.github')
# --- End Configuration ---

def generate_directory_listing(path):
    try:
        items = sorted(os.listdir(path))

        with open(os.path.join(path, 'index.html'), 'w') as f:
            # HTML Header
            f.write('<!DOCTYPE html>\n<html>\n<head>\n')
            dir_name = os.path.basename(os.path.abspath(path))
            f.write(f'<title>Index of {dir_name}</title>\n')
            f.write('<style>body { font-family: sans-serif; margin: 2em; } ul { list-style-type: none; padding: 0; } li { margin: 0.5em 0; } a { text-decoration: none; } a:hover { text-decoration: underline; }</style>\n')
            f.write('</head>\n<body>\n')
            f.write(f'<h1>Index of {dir_name}</h1>\n<hr>\n<ul>\n')

            if os.path.abspath(path) != os.path.abspath(os.getcwd()):
                f.write('<li><a href="../">../</a> (Parent Directory)</li>\n')

            subdirectories = [item for item in items if os.path.isdir(os.path.join(path, item)) and item not in IGNORE_DIRS]
            files = [item for item in items if not os.path.isdir(os.path.join(path, item))]

            for subdir in subdirectories:
                f.write(f'<li><a href="{subdir}/"><strong>{subdir}/</strong></a></li>\n')
                generate_directory_listing(os.path.join(path, subdir))
            
            for file_item in files:
                if file_item != os.path.basename(__file__) and not file_item.endswith('index.html'):
                    f.write(f'<li><a href="{file_item}">{file_item}</a></li>\n')

            f.write('</ul>\n<hr>\n</body>\n</html>\n')
        
        print(f"Generated index.html for {path}")

    except Exception as e:
        print(f"Could not process directory {path}: {e}")

if __name__ == '__main__':
    start_path = os.getcwd()
    print(f"Starting directory listing generation from: {start_path}")
    generate_directory_listing(start_path)
    print("\nDirectory listing generation complete.")
