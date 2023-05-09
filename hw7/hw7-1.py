from setuptools import setup


def do_setup(args_dict): 
    setup()
    setup(name = args_dict.get("name"),
          version = args_dict.get("version"),
          description = args_dict.get("description"),
          url = args_dict.get("url"),
          author = args_dict.get("author"),
          author_email = args_dict.get("author_email"),
          license = args_dict.get("license"),
          packages = args_dict.get("packages"))

          
args_dict = {
    "name": "useful",
    "version": "1",
    "description": "Very useful code",
    "url": "http://github.com/dummy_user/useful",
    "author": "Flying Circus",
    "author_email": "flyingcircus@example.com",
    "license": "MIT",
    "packages": ["useful"],
    }
          
do_setup(args_dict)          
          
          