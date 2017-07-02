import json
import urllib.parse

_MAX_CARD_LENGTH = 8000
PLAIN_TEXT = 'PlainText'
SSML = 'SSML'


def build_response(
        response_type: str, response_text: str, session_attributes: dict=None,
        should_end_session: bool=True) -> dict:
    """Builds a dict structure that can be returned as an Alexa skill response

    :param response_type: Using the module attributes, specify whether the
                          response is plain text to be read or speech markup
    :param response_text: The actual response for Alexa to speak
    :param session_attributes: Key/value pairs to store in the user's session
    :param should_end_session:
        Should Alexa listen for a response, or is the conversation over

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

    MAX_CARD_LENGTH = _MAX_CARD_LENGTH

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

        try:
            self._check_attribute_types(text, title, small_image, large_image)
        except TypeError:
            raise
        try:
            self._check_card_length(text, title, small_image, large_image)
        except ValueError:
            raise

        self.text = text
        if title:
            self.title = title

        try:
            if small_image:
                self._check_image_url(small_image)
                self.small_image = small_image
            if large_image:
                self._check_image_url(large_image)
                self.large_image = large_image
        except ValueError:
            raise

    @staticmethod
    def _check_attribute_types(
            text: str, title: str, small_image: str, large_image: str):
        """Verify all Card initialization parameters are of the correct types.

        :param text: Card's text
        :param title: Card's title, if any
        :param small_image: Card's small image URL, if any
        :param large_image: Card's large image URL, if any

        :raises: TypeError
        """

        text_is_not_str = type(text) != str
        title_is_not_str = title is not None and type(title) != str
        small_image_is_not_str = (
             small_image is not None and type(small_image) != str)
        large_image_is_not_str = (
            large_image is not None and type(large_image) != str)

        if (text_is_not_str or title_is_not_str or small_image_is_not_str
                or large_image_is_not_str):
            raise TypeError('Cards can only be built from strings')

    @classmethod
    def _check_card_length(
            cls, text: str, title: str, small_image: str, large_image: str):
        """Verify total length of all card text is less than the allowed max.

        The Alexa API limits the combined length of all text fields and URL's
        on a single card, see
        https://developer.amazon.com/public/solutions/alexa/alexa-skills-kit/docs/alexa-skills-kit-interface-reference#response-format

        :param text: Card's text
        :param title: Card's title, if any
        :param small_image: Card's small image URL, if any
        :param large_image: Card's large image URL, if any

        :raises: ValueError
        """

        total_length = len(text)
        if title:
            total_length += len(title)
        if small_image:
            total_length += len(small_image)
        if large_image:
            total_length += len(large_image)

        if total_length > cls.MAX_CARD_LENGTH:
            raise ValueError(
                'Total length of all card items cannot exceed {max_length} characters.'.format(
                    max_length=cls.MAX_CARD_LENGTH))

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

    def get_response_data(self) -> dict:
        """Return properly-structured object for use in a Response

        :return: dict representation of this Card instance
        """

        if hasattr(self, 'small_image') or hasattr(self, 'large_image'):
            output = {
                'image': {},
                'text': self.text,
                'type': 'Standard',
            }
        else:
            output = {
                'content': self.text,
                'type': 'Simple',
            }

        if hasattr(self, 'title'):
            output['title'] = self.title
        if hasattr(self, 'small_image'):
            output['image']['smallImageUrl'] = self.small_image
        if hasattr(self, 'large_image'):
            output['image']['smallImageUrl'] = self.large_image

        return output

    def __set
