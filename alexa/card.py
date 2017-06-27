import urllib.parse


def build_card(
        text: str, title: str=None, small_image: str=None,
        large_image: str=None) -> dict:
    """Create a card object that can be included in an Alexa skill response.

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
    if type(title) != str and title is not None:
        raise TypeError('Card title must be passed as a string; received {type}'.format(type=type(title)))
    if type(small_image) != str and small_image is not None:
        raise TypeError('Small image URL must be passed as a string; received {type}'.format(type=type(small_image)))
    if type(large_image) != str and large_image is not None:
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
            _check_image_url(small_image)
        except ValueError:
            raise

        card['image'] = {}
        card['image']['smallImageUrl'] = small_image

    if large_image:
        try:
            _check_image_url(large_image)
        except ValueError:
            raise

        if 'image' not in card:
            card['image'] = {}
        card['image']['largeImageUrl'] = large_image

    return card


def _check_image_url(url: str):
    """Verify an image URL meets the requirements of images for the Alexa app.

    Specifically, the scheme must be 'https', URL's must be absolute, and only
    JPEG and PNG images are supported.

    :param url: URL to be checked

    :raises: ValueError
    """

    parsed_url = urllib.parse.urlparse(url)

    bad_netloc = parsed_url.netloc == '' or '.' not in parsed_url.netloc
    bad_scheme = parsed_url.scheme == '' or parsed_url.scheme != 'https'
    if bad_scheme or bad_netloc:
        raise ValueError('Invalid image URL; received: {url}'.format(url=url))

    not_a_jpeg = not url.lower().endswith('.jpeg')
    not_a_jpg = not url.lower().endswith('.jpg')
    not_a_png = not url.lower().endswith('.png')
    if not_a_jpeg and not_a_jpg and not_a_png:
        raise ValueError('Only JPEG and PNG image types are supported for cards')
