import re

def html2markdown(html):
    '''Take in html text as input and return markdown'''
    markdown = re.sub(r'<em>(.*?)</em>', r'*\1*', html)
    markdown = re.sub(r'\s+\n*', ' ', markdown)
    markdown = re.sub(r'</p><p>', r'\n\n', markdown)
    markdown = re.sub(r'</?p>', '', markdown)
    markdown = re.sub(r'<a href="(.*?)">(.*?)</a>', r'[\2](\1)', markdown)

    return markdown