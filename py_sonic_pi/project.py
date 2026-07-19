import random
import string
from py_sonic_pi.effects import Gain
from py_sonic_pi.inventory import (
    INTERNAL_MASTER_GAIN_EFFECT_ID,
    INTERNAL_MASTER_TRACK_ID,
    EffectInstance,
    GeneratorTrack,
    GroupTrack,
    INTERNAL_MASTER_GAIN_STATE_VALUE_NAME,
    StateValue,
    Track,
)


class Project:
    def __init__(
        self,
        top_level_tracks: list[Track],
        beat_length_seconds: float = 0.5,
        state_values: list[StateValue] = [],
    ):
        self.top_level_tracks = top_level_tracks
        self.beat_length_seconds = beat_length_seconds
        self.state_values = state_values

        master_gain_state_value = StateValue(
            initial_value=1.0,
            target_value=1.0,
            transition_change_per_bar=0,
            name=INTERNAL_MASTER_GAIN_STATE_VALUE_NAME,
        )
        self.state_values.append(master_gain_state_value)

        self.master_track = GroupTrack(
            id=INTERNAL_MASTER_TRACK_ID,
            children=self.top_level_tracks,
            effects=[
                Gain(
                    id=INTERNAL_MASTER_GAIN_EFFECT_ID,
                    controllable=True,
                    gain=master_gain_state_value,
                )
            ],
            amp=1.0,
            pan=0.0,
            muted=False,
            solo=False,
        )

        self.project_id = ''.join(random.choices(string.ascii_lowercase, k=5))

    def get_flat_list_of_generator_tracks(self) -> list[GeneratorTrack]:
        generator_tracks = []

        def _traverse(track: Track):
            if isinstance(track, GeneratorTrack):
                generator_tracks.append(track)
            elif isinstance(track, GroupTrack):
                for child in track.children:
                    _traverse(child)

        _traverse(self.master_track)

        return generator_tracks

    def get_all_controllable_fxs(self) -> list[EffectInstance]:
        controllable_fxs = []

        def _traverse(track: Track):
            for fx in track.get_effects():
                if fx.controllable:
                    controllable_fxs.append(fx)
            if isinstance(track, GroupTrack):
                for child in track.children:
                    _traverse(child)

        _traverse(self.master_track)

        return controllable_fxs

    def fade_out(self, fade_time_bars: float):
        for state_value in self.state_values:
            if state_value.name == INTERNAL_MASTER_GAIN_STATE_VALUE_NAME:
                state_value.target_value = 0.0
                state_value.transition_change_per_bar = 1/fade_time_bars

    def get_master_gain_state_value(self) -> StateValue:
        for state_value in self.state_values:
            if state_value.name == INTERNAL_MASTER_GAIN_STATE_VALUE_NAME:
                return state_value
        raise ValueError("Global gain state value not found in project.")