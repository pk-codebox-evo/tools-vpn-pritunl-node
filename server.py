import pritunl_node

print '##############################################################'
print '#                                                            #'
print '#                      /$$   /$$                         /$$ #'
print '#                     |__/  | $$                        | $$ #'
print '#   /$$$$$$   /$$$$$$  /$$ /$$$$$$   /$$   /$$ /$$$$$$$ | $$ #'
print '#  /$$__  $$ /$$__  $$| $$|_  $$_/  | $$  | $$| $$__  $$| $$ #'
print '# | $$  \ $$| $$  \__/| $$  | $$    | $$  | $$| $$  \ $$| $$ #'
print '# | $$  | $$| $$      | $$  | $$ /$$| $$  | $$| $$  | $$| $$ #'
print '# | $$$$$$$/| $$      | $$  |  $$$$/|  $$$$$$/| $$  | $$| $$ #'
print '# | $$____/ |__/      |__/   \___/   \______/ |__/  |__/|__/ #'
print '# | $$                                                       #'
print '# | $$                                         /$$           #'
print '# |__/                                        | $$           #'
print '#                    /$$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$  #'
print '#                   | $$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ #'
print '#                   | $$  \ $$| $$  \ $$| $$  | $$| $$$$$$$$ #'
print '#                   | $$  | $$| $$  | $$| $$  | $$| $$_____/ #'
print '#                   | $$  | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$ #'
print '#                   |__/  |__/ \______/  \_______/ \_______/ #'
print '#                                                            #'
print '##############################################################'

pritunl_node.app_server.conf_path = './tools/development_pritunl_node.conf'
pritunl_node.app_server.run_server()
