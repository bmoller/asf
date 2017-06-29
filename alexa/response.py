import json
import urllib.parse

PLAIN_TEXT = 'PlainText'
SSML = 'SSML'


def build_response(
        response_type: str, response_text: str, session_attributes: dict=None,
        should_end_session: bool=True) -> dict:
    """ Builds a dict structure that can be returned as an Alexa skill response

    :param response_type: Using the module attributes, specify whether the
                          response is plain text to be read or speech markup
    :param response_text: The actual response for Alexa to speak
    :param session_attributes: Key/value pairs that will be stored in the
                               user's session
    :param should_end_session: Determines if Alexa should listen for a response
                               or the conversation is over

    :return: An Alexa skill response
    """

    response = {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': response_type,
            },
            'shouldEndSession': should_end_session,
        },
    }

    if response_type == SSML:
        response['response']['outputSpeech']['ssml'] = response_text
    else:
        response['response']['outputSpeech']['text'] = response_text

    if session_attributes:
        response['session_attributes'] = session_attributes

    return response


class Card:

    def __init__(
            self, text: str, title: str=None, small_image: str=None,
            large_image: str=None):
        """Cards can be simple text with no formatting, or text with an image
        displayed above. Supported image formats are JPEG and PNG, with a max
        file size of 2 MB. Per Amazon docs, images must be loaded over SSL.

        :param text: Formatted text content to display for standard card types
        :param title: Optional title of the card displayed in the Alexa app
        :param small_image:
            URL of an image to display on small-format devices;
            Amazon-recommended size is 720x480
        :param large_image:
            URL of an image to display on large-format devices;
            Amazon-recommended size is 1200x800

        :raises: ValueError
        """

        text_is_not_str = not type(text) == str
        title_is_not_str = (
            not type(title) == str and title is not None)
        small_image_is_not_str = (
            not type(small_image) == str and small_image is not None)
        large_image_is_not_str = (
            not type(large_image) == str and large_image is not None)
        if (text_is_not_str or title_is_not_str or small_image_is_not_str
                or large_image_is_not_str):
            raise TypeError('Cards can only be built from strings')

        self.text = text

        if title:
            self.title = title

        if small_image:
            try:
                self._check_image_url(small_image)
            except ValueError:
                raise
            else:
                self.small_image = small_image

        if large_image:
            try:
                self._check_image_url(large_image)
            except ValueError:
                raise
            else:
                self.large_image = large_image

    @staticmethod
    def _check_image_url(url: str):
        """Verify an image URL meets the requirements of the Alexa app.

        Specifically, the scheme must be 'https', URL's must be absolute, and
        only JPEG and PNG images are supported.

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

    def __str__(self) -> str:
        """Return proper JSON-formatted text representation of this card.

        :return: JSON output
        """

        if (
                hasattr(self, 'small_image') and self.small_image
                or hasattr(self, 'large_image') and self.large_image):

            output = {
                'image': {},
                'text': self.text,
                'type': 'Standard',
            }
            if hasattr(self, 'small_image') and self.small_image:
                output['image']['smallImageUrl'] = self.small_image
            if hasattr(self, 'large_image') and self.large_image:
                output['image']['smallImageUrl'] = self.large_image

        else:

            output = {
                'content': self.text,
                'type': 'Simple',
            }

        if hasattr(self, 'title') and self.title:
            output['title'] = self.title

        return json.dumps(sorted(output))
