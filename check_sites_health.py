import requests
import whois
import tldextract
from datetime import datetime
import argparse


MIN_DAY_COUNT = 30


def load_urls4check(path):
    with open(path, 'r') as check_urls:
        urls = check_urls.readlines()
        urls = [url.strip() for url in urls]
    return urls


def is_server_respond_with_200(url):
    responce = requests.get(url=url)
    return responce.status_code == requests.codes.ok


def get_domain_expiration_date(domain_name):
    domain = whois.whois(domain_name)
    expire_date = domain['expiration_date']
    cur_date = datetime.now()
    if isinstance(expire_date, list):
        time_delta = expire_date[0] - cur_date
    else:
        time_delta = expire_date - cur_date
    return time_delta.days >= MIN_DAY_COUNT


def create_parser():
    parser = argparse.ArgumentParser(description='sites monitoring')
    parser.add_argument('path', help='path to urls file')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    path_to_urls_file = args.path
    check_urls = load_urls4check(path_to_urls_file)
    for url in check_urls:
        devided_url = tldextract.extract(url)
        domain_name = '{}.{}'.format(devided_url.domain,
                                     devided_url.suffix)
        if is_server_respond_with_200(url):
            print('\n{} is OK'.format(url))
        else:
            print('\n{} is down'.format(url))
        if get_domain_expiration_date(domain_name):
            print('domain name {} is paid'.format(url))
        else:
            print('{} expired soon'.format(url))
