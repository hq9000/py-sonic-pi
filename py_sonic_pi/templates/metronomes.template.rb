live_loop :metronome_loop_1_bars do
    cue :1_bars_start
    sleep 4*get(:beat_duration)
end

live_loop :metronome_loop_2_bars do
    cue :2_bars_start
    sleep 2*4*get(:beat_duration)
end

live_loop :metronome_loop_4_bars do
    cue :4_bars_start
    sleep 4*4*get(:beat_duration)
end

live_loop :metronome_loop_beats do
    cue :beat_start
    sleep get(:beat_duration)
end