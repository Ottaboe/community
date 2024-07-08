


#parrot repeat
parrot(cluck): core.repeat_phrase(1)

#cancel previous command    
#parrot(cluck): user.cancel_command()


# So you can wake Talon with Parrot 

#parrot(cluck):
    user.engine_wake()
    user.ensure_tracking_enabled()






