set :beat_length, {{ project.beat_length_seconds }}

{% for track in project.get_flat_list_of_generator_tracks() %}
    {%- with track=track %}
        {%-  include 'track_source.template.rb' %}
    {%- endwith %}
{% endfor %}

{% include "processing_block.template.rb" %}

{%  include 'metronomes.template.rb' %}