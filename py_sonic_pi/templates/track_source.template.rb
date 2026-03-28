def {{ track.id }}_loop()
    print "{{ track.name }} loop"
    live_loop :"{{ track.id }}_loop" do
        

    end
end