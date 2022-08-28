from setuptools import setup
# read the contents of your README file
with open("C:\\Users\\Harry\\Desktop\\abcdefgh\\TextEditor\\PrintWithColor" + "\\ReadMe.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()
    

setup(
    name='PrintWithColor',
    # other arguments omitted
    long_description=long_description,
    long_description_content_type='text/markdown'
)