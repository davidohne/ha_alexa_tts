# Home Assistant: Alexa Device TTS Integration von Text-to-speech

Integration works for Assist pipelines. 

### Requirements:
- Alexa Media Player devices must be configured and working

### Configuration:

Remarks:
- Add your Alexa Media player device entity!!!
- Set the language of the Assist Pipeline
- At the moment there will be an error in the ha logs because no mp3 is returned. Can be ignored

configuration.yaml:


```
tts:
  - platform: alexa_tts
    language: "de-DE"
    alexa_device: alexa_media_example_echo
```




