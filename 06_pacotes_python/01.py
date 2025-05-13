#pypy repositorio publico oficial de pacotes
# create project -> gerar distribuições (wheel e sdist) -> upload para o pypy (pip install nome_pacote)
'''
ESTRUTURAS:
    PROJECT_NAME/
        README.MD
        REQUIREMENTS.TXT
        PACKAGE_NAME/
            __INIT__.PY
            MODULE1_NAME/
                __INIT__.PY
                FILE1.PY
                FILE2.PY
            MODULE2_NAME/
                __INIT__.PY
                FILE1.PY
                FILE2.PY

    PROJECT2_NAME/
        README.MD
        REQUIREMENTS.TXT
        PACKAGE_NAME/
             __INIT__.PY
                FILE1.PY
                FILE2.PY  


    #EXEMPLO PARA CHAMADA: import package_name.file1_name
    #EXEMPLO PARA CHAMADA (modulo mais complexo): import package_name.module_name1.file1_name   
'''



