from py_sonic_pi.effects import Gain
from py_sonic_pi.inventory import (
    EffectInstance,
    GeneratorTrack,
    GroupTrack,
    MASTER_GAIN_STATE_VALUE_NAME,
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
            transition_time_bars=0,
            name=MASTER_GAIN_STATE_VALUE_NAME,
        )
        self.state_values.append(master_gain_state_value)

        self.master_track = GroupTrack(
            id="master",
            children=self.top_level_tracks,
            effects=[
                Gain(
                    id="master_gain",
                    controllable=True,
                    amp=master_gain_state_value,
                )
            ],
            amp=1.0,
            pan=0.0,
            muted=False,
            solo=False,
        )

    def get_flat_list_of_generator_tracks(self) -> list[GeneratorTrack]:
        generator_tracks = []

        def _traverse(track: Track):
            if isinstance(track, GeneratorTrack):
                generator_tracks.append(track)
            elif isinstance(track, GroupTrack):
                for child in track.children:
                    _traverse(child)

        for top_level_track in self.top_level_tracks:
            _traverse(top_level_track)

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

        for top_level_track in self.top_level_tracks:
            _traverse(top_level_track)

        return controllable_fxs