set :beat_length, 0.45

def bd_loop()
  live_loop :bd_loop do
    sync :start_1_bars
    sample :bd_haus
    sleep 1.0*get(:beat_length)
    sample :bd_haus
    sleep 1.0*get(:beat_length)
    sample :bd_haus
    sleep 1.0*get(:beat_length)
    sample :bd_haus
    end
end
def bass_loop()
  live_loop :bass_loop do
    use_synth :tb303
    sync :start_1_bars
    sleep 0.5*get(:beat_length)
    play 48, release: 0.1
    sleep 1.0*get(:beat_length)
    play 60, release: 0.1
    sleep 1.0*get(:beat_length)
    play 49, release: 0.1
    sleep 1.0*get(:beat_length)
    play 48, release: 0.1
    end
end
def crash_loop()
  live_loop :crash_loop do
    sync :start_1_bars
    sample :ride_tri
    end
end


# Track: master
with_fx :rhpf, cutoff: 0.0, cutoff_slide: 0.0 do |rhpf_masterhpf|
set :rhpf_masterhpf,rhpf_masterhpf if run_count == 1
with_fx :pan, pan: 0.0, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |pan_track_master_gain_and_pan|
set :pan_track_master_gain_and_pan,pan_track_master_gain_and_pan if run_count == 1
  # Track: bass_bd
  with_fx :reverb, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, mix: 0.5, mix_slide: 0.0, mix_slide_shape: 1, pre_mix: 0.5, pre_mix_slide: 0.0, pre_mix_slide_shape: 1, pre_amp: 1.0, pre_amp_slide: 0.0, pre_amp_slide_shape: 1, room: 1, room_slide: 0.0, room_slide_shape: 1, damp: 0.5, damp_slide: 0.0, damp_slide_shape: 1 do |reverb_bass_bd_reverb|
  set :reverb_bass_bd_reverb,reverb_bass_bd_reverb if run_count == 1
  with_fx :pan, pan: 0.0, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |pan_track_bass_bd_gain_and_pan|
  set :pan_track_bass_bd_gain_and_pan,pan_track_bass_bd_gain_and_pan if run_count == 1
    # Track: bd
    with_fx :pan, pan: 0.0, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |pan_track_bd_gain_and_pan|
    set :pan_track_bd_gain_and_pan,pan_track_bd_gain_and_pan if run_count == 1
    bd_loop()
    end
    # Track: bass
    with_fx :reverb, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, mix: 0.5, mix_slide: 0.0, mix_slide_shape: 1, pre_mix: 0.5, pre_mix_slide: 0.0, pre_mix_slide_shape: 1, pre_amp: 1.0, pre_amp_slide: 0.0, pre_amp_slide_shape: 1, room: 0.5, room_slide: 0.0, room_slide_shape: 1, damp: 0.5, damp_slide: 0.0, damp_slide_shape: 1 do |reverb_bass_reverb|
    set :reverb_bass_reverb,reverb_bass_reverb if run_count == 1
    with_fx :pan, pan: 0.5, amp: 0.3, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |pan_track_bass_gain_and_pan|
    set :pan_track_bass_gain_and_pan,pan_track_bass_gain_and_pan if run_count == 1
    bass_loop()
    end
    end
  end
  end
  # Track: crash
  with_fx :pan, pan: 0.0, amp: 0.5, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |pan_track_crash_gain_and_pan|
  set :pan_track_crash_gain_and_pan,pan_track_crash_gain_and_pan if run_count == 1
  crash_loop()
  end
end
end


live_loop :control_loop do
sync :start_1_bars
  fx = get(:rhpf_masterhpf)
  control fx, cutoff: 0.0
  control fx, cutoff_slide: 0.0
  fx = get(:pan_track_master_gain_and_pan)
  control fx, pan: 0.0
  control fx, amp: 1.0
  control fx, amp_slide: 0.0
  control fx, amp_slide_shape: 1
  control fx, pan_slide: 0.0
  control fx, pan_slide_shape: 1
  fx = get(:pan_track_bass_bd_gain_and_pan)
  control fx, pan: 0.0
  control fx, amp: 1.0
  control fx, amp_slide: 0.0
  control fx, amp_slide_shape: 1
  control fx, pan_slide: 0.0
  control fx, pan_slide_shape: 1
  fx = get(:pan_track_bd_gain_and_pan)
  control fx, pan: 0.0
  control fx, amp: 1.0
  control fx, amp_slide: 0.0
  control fx, amp_slide_shape: 1
  control fx, pan_slide: 0.0
  control fx, pan_slide_shape: 1
  fx = get(:pan_track_bass_gain_and_pan)
  control fx, pan: 0.5
  control fx, amp: 0.3
  control fx, amp_slide: 0.0
  control fx, amp_slide_shape: 1
  control fx, pan_slide: 0.0
  control fx, pan_slide_shape: 1
  fx = get(:pan_track_crash_gain_and_pan)
  control fx, pan: 0.0
  control fx, amp: 0.5
  control fx, amp_slide: 0.0
  control fx, amp_slide_shape: 1
  control fx, pan_slide: 0.0
  control fx, pan_slide_shape: 1
  sleep 1 * get(:beat_length)
end


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
