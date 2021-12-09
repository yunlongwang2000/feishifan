from urllib.request import urlopen


def get(config, inf):
    url = 'http://{ip}:{port}/login?name={name}&pwd={pwd}&information={inf}'.format(**config, inf=inf)
    result_origin = urlopen(url).read().decode('utf8')
    result = eval(result_origin)
    return result
