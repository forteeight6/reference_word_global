"""
Testando o uso de variaveis globais e o comceito de importação dinamica com atualização.

Testing the use of global variables and the concept of dynamic import with update.
"""

from configs import config
from utils import *

def main() -> None:
    # Show somethings configs
    print("<<<<<<<<<<<<<<B E F O R E:>>>>>>>>>>>>>>>>> ")
    print("A fonte é do tipo", config.font_family, '\n')
    print("O atalho para criar novo documento é", config.shortcut_to_new_document, '\n')
    print("A posição da ferramenta 01 é,", config.tool_position_01, '\n')
    print("<<<<<<<<<<<<<<B E F O R E:>>>>>>>>>>>>>>>>> ")
    print()
    
    if config.teste:
        update("font_family", "Arial, Cordova", "configs.config")
        update("shortcut_to_new_document", "Ctrl, N", "configs.config")
        update("tool_position_01", "300px, 350px", "configs.config")
        update("teste", "False", "configs.config")
    else:
        update("font_family", "Teste", "configs.config")
        update("shortcut_to_new_document", "Teste", "configs.config")
        update("tool_position_01", "Teste", "configs.config")
        update("teste", "True", "configs.config")

    # Show Update
    print("<<<<<<<<<<<<<<A F T E R:>>>>>>>>>>>>>>>>> ")
    print("Agora a fonte é do tipo", config.font_family, '\n')
    print("Agora o atalho para criar novo documento é", config.shortcut_to_new_document, '\n')
    print("Agora a posição da ferramenta 01 é,", config.tool_position_01, '\n')
    print("<<<<<<<<<<<<<<A F T E R:>>>>>>>>>>>>>>>>> ")
    print()
    
if __name__ == "__main__":
    main()