# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 09:54:14 2024

@author: TejasReddy_od7b

Audio Personal Project

pip install soundfile sounddevice
"""

import soundfile as sf
import sounddevice as sd
import pyannote.audio.signal
from pyannote.audio.pipelines import SpeakerDiarization


#### HELPER FUNCTIONS
def play_wav(waveform, playback_duration = 10):
    # Define the duration to play (in seconds)
    playback_duration = 10  # seconds
    num_samples_to_play = int(playback_duration * sample_rate)
    waveform_to_play = waveform[:num_samples_to_play]
    
    
    # Play audio
    sd.play(waveform_to_play, sample_rate)
    sd.wait()
    pass
    








# File path to the audio file
file_path = "C:/Users/TejasReddy_od7b/Downloads/PersonalJob/Personal/multiple_voice.wav"

# Read and play the audio file
waveform, sample_rate = sf.read(file_path)
play_wav(waveform, playback_duration = 4)


audio = pyannote.audio.signal.Audio(waveform.numpy().squeeze(), sample_rate=sample_rate)

# Perform speaker diarization
diarization_pipeline = SpeakerDiarization()
diarization = diarization_pipeline(audio)

# Extract speaker segments
for segment, track, label in diarization.itertracks(yield_label=True):
    speaker_id = label
    speaker_waveform = waveform[:, int(segment.start * sample_rate):int(segment.end * sample_rate)]
    

























Voice.py
Displaying Voice.py.