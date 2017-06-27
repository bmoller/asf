import urllib.parse


def build_card(text: str, title: str=None, small_image: str=None,
               large_image: str=None) -> dict:
    """ Create a card object that can be included in an Alexa skill response.
    Cards can be simple text with no formatting, or text with an image
    displayed above. Supported image formats are JPEG and PNG, with a max file
    size of 2 MB. Per Amazon docs, images must be loaded over SSL.

    :param text: Formatted text content to display for standard card types
    :param title: Optional title of the card displayed in the Alexa app
    :param small_image: URL of an image to display on small-format devices;
                        Amazon-recommended size is 720x480
    :param large_image: URL of an image to display on large-format devices;
                        Amazon-recommended size is 1200x800

    :return: Properly structured card object for an Alexa response

    :raises: TypeError, ValueError
    """

    if type(text) != str:
        raise TypeError('Card text must be passed as a string; received {type}'.format(type=type(text)))
    if title is not None and type(title) != str:
        raise TypeError('Card title must be passed as a string; received {type}'.format(type=type(title)))
    if small_image is not None and type(small_image) != str:
        raise TypeError('Small image URL must be passed as a string; received {type}'.format(type=type(small_image)))
    if large_image is not None and type(large_image) != str:
        raise TypeError('Large image URL must be passed as a string; received {type}'.format(type=type(large_image)))

    if small_image or large_image:
        card = {
            'type': 'Standard',
            'text': text,
        }
    else:
        card = {
            'type': 'Simple',
            'content': text,
        }

    if title:
        card['title'] = title

    if small_image:
        try:
            check_image_url(small_image)
        except ValueError:
            raise

        card['image'] = {}
        card['image']['smallImageUrl'] = small_image

    if large_image:
        try:
            check_image_url(large_image)
        except ValueError:
            raise

        if 'image' not in card:
            card['image'] = {}
        card['image']['largeImageUrl'] = large_image

    return card


def check_image_url(url: str):
    """ Check that an image URL meets the requirements of images for cards in
    the Alexa app. Specifically, the scheme must be 'https', URL's must be
    absolute, and only JPEG and PNG images are supported.

    :param url: URL to be checked

    :raises: ValueError
    """

    parsed_url = urllib.parse.urlparse(url)

    if parsed_url.scheme == '' or parsed_url.scheme != 'https':
        raise ValueError('Invalid image URL for large image; received: {url}'.format(url=url))

    if parsed_url.netloc == '' or '.' not in parsed_url.netloc:
        raise ValueError('Invalid image URL for large image; received: {url}'.format(url=url))

    if (not parsed_url.path.endswith('.jpg')
            and not parsed_url.path.endswith('.jpeg')
            and not parsed_url.path.endswith('.png')):
        raise ValueError('Only JPEG and PNG image types are supported for cards')
