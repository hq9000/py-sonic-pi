set :beat_length, {{ project.beat_length_seconds }}

{% include "source_block.template.rb" %}

{% include "processing_block.template.rb" %}

{% include "control_block.template.rb" %}

{%  include 'metronomes.template.rb' %}