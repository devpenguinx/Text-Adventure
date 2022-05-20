from pip import main
import intro_screen
import main_menu
import first_scene

intro_screen.printintro()

# function therefore returned new game (right arrow key was pressed)
if main_menu.displaymainmenu() == 'new game':
    first_scene.main()
    
