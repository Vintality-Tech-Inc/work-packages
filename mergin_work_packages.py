
from workpackages.wp_mergin import run_wp_mergin_with_context, parse_args
from dotenv import load_dotenv  # Note: The standard function name is actually load_dotenv

# Search and load the .env file
load_dotenv() 


if __name__ == "__main__":
    run_wp_mergin_with_context(parse_args())
