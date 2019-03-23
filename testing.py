# import applescript
# pause = applescript.AppleScript('tell application "iTunes" to pause')
# pause.run()
#
# applescript is trash because it won't work => go to solution with straight up bash and running it

from subprocess import Popen
pause_apple_script = "osascript -e 'tell application "+'"iTunes"'+" to pause'"
play_apple_script = "osascript -e 'tell application "+'"iTunes"'+" to play'"

Popen(play_apple_script, shell=True) # must add shell=True when adding raw string
