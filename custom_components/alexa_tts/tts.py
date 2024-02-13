"""
Support for Alexa Device TTS.
"""
import logging
import requests
import voluptuous as vol
from homeassistant.components.tts import CONF_LANG, PLATFORM_SCHEMA, Provider
from homeassistant.core import HomeAssistant
import homeassistant.helpers.config_validation as cv
import asyncio

_LOGGER = logging.getLogger(__name__)

CONF_ALEXA_DEVICE = 'alexa_device'
CONF_ALEXA_LANGUAGE = 'language'
DEFAULT_LANG = 'de-DE'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_ALEXA_DEVICE): cv.string,
    vol.Optional(CONF_LANG, default=DEFAULT_LANG): cv.string,
})


def get_engine(hass, config, discovery_info=None):
    """Set up Alexa Device TTS speech component."""
    alexa_device = config[CONF_ALEXA_DEVICE]
    language = config.get(CONF_LANG, DEFAULT_LANG)

    return AlexaTTSProvider(hass, alexa_device, language)


class AlexaTTSProvider(Provider):
    """The Alexa Device TTS provider."""

    def __init__(self, hass, alexa_device, lang):
        """Initialize Alexa Device TTS provider."""
        self.hass = hass
        self._alexa_device = alexa_device
        self._language = lang

    @property
    def default_language(self):
        """Return the default language."""
        return self._language

    @property
    def supported_languages(self):
        """Return the list of supported languages."""
        return [self._language]

    def get_tts_audio(self, message, language, options=None):

        service_data = {
            "message": message
        }
        coroutine = self.hass.services.async_call('notify', self._alexa_device, service_data, blocking=True)

        asyncio.run_coroutine_threadsafe(coroutine, self.hass.loop).result()

        # There will be an error in the ha logs, because no MP3 file is returned... but it works
        return None, None