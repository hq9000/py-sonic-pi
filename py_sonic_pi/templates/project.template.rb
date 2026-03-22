set :beat_length, {{ project.beat_length_seconds }}

{% for track in project.tracks %}
    {%- with track=track %}
        {%-  include 'track_source.template.rb' %}
    {%- endwith %}
{% endfor %}

{%  include 'metronomes.template.rb' %}