"""
Esta função utiliza os elementos import_module e reload do módulo importlib.
This function uses the import_modulo and reload elements of the importlib module.
"""

from typing import Union
from importlib import import_module, reload
import re

def update(config: str, new_config: Union[bool, str], mod_config: str) -> None:
    """ This function makes update in configuration and update the module.
        Esta função faz atualização na configuração e atualiza o modulo.
        
        :param - config: variable that will update | variavel que ira atualizar.
               - new_config: value to new update | valor para nova atualização.
               - mod_config: location where the modulo is located | local onde o módulo está localizado.
        :return - None
    """
    texto = ""
    local = mod_config.replace('.', '/') + ".py"
    # print(local)
    mod = import_module(mod_config)
    with open(local, "r") as file:
        for linha in file:            
            if re.match(r'{}'.format(config), linha):
                try:
                    x = str(linha.split('"')[1])
                except:
                    # O erro é por causa do value ser um bool
                    x = str(linha.split()[2])
                    
                linha = re.sub(r"{}".format(x), new_config, linha)
                texto+=linha
            else:
                texto+=linha
    
    with open("configs/config.py", "w") as file:
        file.write(texto)
    reload(mod)
    
if __name__ == "__main__":
    update("tool_position_01", "teste", "configs.config")