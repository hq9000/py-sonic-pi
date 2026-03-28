live_loop :metronome_loop_1_bars do
    cue :start_1_bars
    sleep 4*get(:beat_length)
end

live_loop :metronome_loop_2_bars do
    cue :start_2_bars
    sleep 2*4*get(:beat_length)
end

live_loop :metronome_loop_4_bars do
    cue :start_4_bars
    sleep 4*4*get(:beat_length)
end

live_loop :metronome_loop_beats do
    cue :beat_start
    sleep get(:beat_length)
end