set :beat_length, 0.45
# =========================================
# state declaration
# =========================================
set :state_value_test_project_bass_cutoff, 50 if run_count == 1
set :state_value_test_project_internal_master_gain, 1.0 if run_count == 1
# =========================================
# source block
# =========================================
def test_project_bd_loop()
  live_loop :test_project_bd_loop do
      sync :start_1_bars
      if get(:state_value_test_project_internal_master_gain) <= 0.01
        stop
      end
        sample :bd_haus
        sleep 1.0*get(:beat_length)
        sample :bd_haus
        sleep 1.0*get(:beat_length)
        sample :bd_haus
        sleep 1.0*get(:beat_length)
        sample :bd_haus
    end
end
def test_project_bass_loop()
  live_loop :test_project_bass_loop do
      use_synth :tb303
      sync :start_1_bars
      if get(:state_value_test_project_internal_master_gain) <= 0.01
        stop
      end
        sleep 0.25*get(:beat_length)
        play 48, amp: 1.3, cutoff: get(:state_value_test_project_bass_cutoff), cutoff_slide: 20, release: 0.1
        sleep 0.5*get(:beat_length)
        play 60, amp: 1.3, cutoff: get(:state_value_test_project_bass_cutoff), cutoff_slide: 20, release: 0.1
        sleep 0.5*get(:beat_length)
        play 49, amp: 1.3, cutoff: get(:state_value_test_project_bass_cutoff), cutoff_slide: 20, release: 0.1
        sleep 0.5*get(:beat_length)
        play 48, amp: 1.3, cutoff: get(:state_value_test_project_bass_cutoff), cutoff_slide: 20, release: 0.1
    end
end
def test_project_sub_bass_loop()
  live_loop :test_project_sub_bass_loop do
      use_synth :saw
      sync :start_1_bars
      if get(:state_value_test_project_internal_master_gain) <= 0.01
        stop
      end
        play 24, pan: -1, release: 0.6
        sleep 1.5*get(:beat_length)
        play 24, pan: -1, release: 0.6
        sleep 1.0*get(:beat_length)
        play 24, pan: -1, release: 0.6
        sleep 1.0*get(:beat_length)
        play 24, pan: -1, release: 0.6
    end
end
def test_project_crash_loop()
  live_loop :test_project_crash_loop do
      sync :start_2_bars
      if get(:state_value_test_project_internal_master_gain) <= 0.01
        stop
      end
        sample :ride_tri
    end
end
def test_project_snare_loop()
  live_loop :test_project_snare_loop do
      sync :start_1_bars
      if get(:state_value_test_project_internal_master_gain) <= 0.01
        stop
      end
        sleep 1.0*get(:beat_length)
        sample :elec_snare
        sleep 2.0*get(:beat_length)
        sample :elec_snare
    end
end
def test_project_oh_loop()
  live_loop :test_project_oh_loop do
      sync :start_1_bars
      if get(:state_value_test_project_internal_master_gain) <= 0.01
        stop
      end
        sleep 0.5*get(:beat_length)
        sample :drum_cymbal_open
        sleep 1.0*get(:beat_length)
        sample :drum_cymbal_open
        sleep 1.0*get(:beat_length)
        sample :drum_cymbal_open
        sleep 1.0*get(:beat_length)
        sample :drum_cymbal_open
    end
end


# =========================================
# processing block
# =========================================
# Track: internal_master
with_fx :level, amp: get(:state_value_test_project_internal_master_gain) do |fxname_level_test_project_internal_master_gain|
set :fxname_level_test_project_internal_master_gain,fxname_level_test_project_internal_master_gain if run_count == 1
with_fx :pan, pan: 0.0, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_internal_master_gain_and_pan|
set :fxname_pan_test_project_track_internal_master_gain_and_pan,fxname_pan_test_project_track_internal_master_gain_and_pan if run_count == 1
  # Track: master
  with_fx :rhpf, cutoff: 0.0, cutoff_slide: 0.0 do |fxname_rhpf_test_project_masterhpf|
  set :fxname_rhpf_test_project_masterhpf,fxname_rhpf_test_project_masterhpf if run_count == 1
  with_fx :pan, pan: 0.0, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_master_gain_and_pan|
  set :fxname_pan_test_project_track_master_gain_and_pan,fxname_pan_test_project_track_master_gain_and_pan if run_count == 1
    # Track: bass_bd
    with_fx :pan, pan: 0.0, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_bass_bd_gain_and_pan|
    set :fxname_pan_test_project_track_bass_bd_gain_and_pan,fxname_pan_test_project_track_bass_bd_gain_and_pan if run_count == 1
      # Track: bd
      with_fx :pan, pan: 0.0, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_bd_gain_and_pan|
      set :fxname_pan_test_project_track_bd_gain_and_pan,fxname_pan_test_project_track_bd_gain_and_pan if run_count == 1
      test_project_bd_loop()
      end
      # Track: bass
      with_fx :reverb, amp: 1.0, amp_slide: 0.0, amp_slide_shape: 1, mix: 0.5, mix_slide: 0.0, mix_slide_shape: 1, pre_mix: 0.5, pre_mix_slide: 0.0, pre_mix_slide_shape: 1, pre_amp: 1.0, pre_amp_slide: 0.0, pre_amp_slide_shape: 1, room: 0.5, room_slide: 0.0, room_slide_shape: 1, damp: 0.5, damp_slide: 0.0, damp_slide_shape: 1 do |fxname_reverb_test_project_bass_reverb|
      set :fxname_reverb_test_project_bass_reverb,fxname_reverb_test_project_bass_reverb if run_count == 1
      with_fx :pan, pan: -0.47, amp: 0.3, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_bass_gain_and_pan|
      set :fxname_pan_test_project_track_bass_gain_and_pan,fxname_pan_test_project_track_bass_gain_and_pan if run_count == 1
      test_project_bass_loop()
      end
      end
      # Track: sub_bass
      with_fx :pan, pan: 0.0, amp: 1, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_sub_bass_gain_and_pan|
      set :fxname_pan_test_project_track_sub_bass_gain_and_pan,fxname_pan_test_project_track_sub_bass_gain_and_pan if run_count == 1
      test_project_sub_bass_loop()
      end
    end
    # Track: crash
    with_fx :pan, pan: 0.0, amp: 0.5, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_crash_gain_and_pan|
    set :fxname_pan_test_project_track_crash_gain_and_pan,fxname_pan_test_project_track_crash_gain_and_pan if run_count == 1
    test_project_crash_loop()
    end
    # Track: snare
    with_fx :pan, pan: 0.0, amp: 0.4, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_snare_gain_and_pan|
    set :fxname_pan_test_project_track_snare_gain_and_pan,fxname_pan_test_project_track_snare_gain_and_pan if run_count == 1
    test_project_snare_loop()
    end
    # Track: oh
    with_fx :pan, pan: 0.0, amp: 0.2, amp_slide: 0.0, amp_slide_shape: 1, pan_slide: 0.0, pan_slide_shape: 1 do |fxname_pan_test_project_track_oh_gain_and_pan|
    set :fxname_pan_test_project_track_oh_gain_and_pan,fxname_pan_test_project_track_oh_gain_and_pan if run_count == 1
    test_project_oh_loop()
    end
  end
  end
end
end


# =========================================
# fx control block
# =========================================
live_loop :control_loop_test_project do
sync :start_1_bars
      if get(:state_value_test_project_internal_master_gain) <= 0.01
        stop
      end
  if run_count != 1
    fx = get(:fxname_level_test_project_internal_master_gain)
    control fx, amp: get(:state_value_test_project_internal_master_gain)
    fx = get(:fxname_pan_test_project_track_internal_master_gain_and_pan)
    control fx, pan: 0.0
    control fx, amp: 1.0
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
    fx = get(:fxname_rhpf_test_project_masterhpf)
    control fx, cutoff: 0.0
    control fx, cutoff_slide: 0.0
    fx = get(:fxname_pan_test_project_track_master_gain_and_pan)
    control fx, pan: 0.0
    control fx, amp: 1.0
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
    fx = get(:fxname_pan_test_project_track_bass_bd_gain_and_pan)
    control fx, pan: 0.0
    control fx, amp: 1.0
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
    fx = get(:fxname_pan_test_project_track_bd_gain_and_pan)
    control fx, pan: 0.0
    control fx, amp: 1.0
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
    fx = get(:fxname_pan_test_project_track_bass_gain_and_pan)
    control fx, pan: -0.47
    control fx, amp: 0.3
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
    fx = get(:fxname_pan_test_project_track_sub_bass_gain_and_pan)
    control fx, pan: 0.0
    control fx, amp: 1
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
    fx = get(:fxname_pan_test_project_track_crash_gain_and_pan)
    control fx, pan: 0.0
    control fx, amp: 0.5
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
    fx = get(:fxname_pan_test_project_track_snare_gain_and_pan)
    control fx, pan: 0.0
    control fx, amp: 0.4
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
    fx = get(:fxname_pan_test_project_track_oh_gain_and_pan)
    control fx, pan: 0.0
    control fx, amp: 0.2
    control fx, amp_slide: 0.0
    control fx, amp_slide_shape: 1
    control fx, pan_slide: 0.0
    control fx, pan_slide_shape: 1
  sleep 1 * get(:beat_length)
  end
end


# =========================================
# state control block
# =========================================
live_loop :state_management_loop_test_project do
sync :start_1_bars
      if get(:state_value_test_project_internal_master_gain) <= 0.01
        stop
      end
if get(:state_value_test_project_bass_cutoff) < 100
  set :state_value_test_project_bass_cutoff, [get(:state_value_test_project_bass_cutoff) + 5, 100].min
elsif get(:state_value_test_project_bass_cutoff) > 100
  set :state_value_test_project_bass_cutoff, [get(:state_value_test_project_bass_cutoff) - 5, 100].max
end
if get(:state_value_test_project_internal_master_gain) < 0.0
  set :state_value_test_project_internal_master_gain, [get(:state_value_test_project_internal_master_gain) + 0.16666666666666666, 0.0].min
elsif get(:state_value_test_project_internal_master_gain) > 0.0
  set :state_value_test_project_internal_master_gain, [get(:state_value_test_project_internal_master_gain) - 0.16666666666666666, 0.0].max
end
sleep 0.25
end


# =========================================
# metronomes
# =========================================
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
