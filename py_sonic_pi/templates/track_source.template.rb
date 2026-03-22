def {{ track.id }}_loop()
    print "{{ track.name }} loop"
    live_loop :"{{ track.id }}_loop" do
        sync :{{ track.pattern.every_n_bars }}_bars_start
        {% if track.type == TrackType.SAMPLE %}
            {% with events = track.pattern.elements %}
                {%- include 'sample_pattern_events.template.rb' %}
            {% endwith %}
        {% elif track.type == TrackType.SYNTH %}
            {% with events = track.pattern.elements %}
                {%- include 'synth_pattern_events.template.rb' %}
            {% endwith %}
        {% else %}
            {{ undefined_variable_to_force_error }}
        {% endif %}
    end
end