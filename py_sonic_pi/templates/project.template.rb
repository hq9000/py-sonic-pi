set :beat_length, {{ beat_length_seconds }}
# =========================================
# state declaration
# =========================================
{% include "state_declaration_block.template.rb" -%}

# =========================================
# source block
# =========================================
{% include "source_block.template.rb" %}

# =========================================
# processing block
# =========================================
{% include "processing_block.template.rb" %}

# =========================================
# fx control block
# =========================================
{% include "fx_control_block.template.rb" %}

# =========================================
# state control block
# =========================================
{% include "state_control_block.template.rb" %}

# =========================================
# metronomes
# =========================================
{%  include 'metronomes.template.rb' %}