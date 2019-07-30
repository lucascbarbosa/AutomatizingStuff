from os import system 

libs = input("Cole aqui todas as linhas de código com imports")
libraries=[]
imps = libs.split('import')
imps = ' '.join(imps)
imps = imps.split('from')
for imp in imps:
    if imp != '' or imp != '\n':
        
        libs= imp.split(' ')
        
        for lib in libs:
            if lib != 'as' and lib != '' and lib != '\n' :
                if lib[len(lib)-1] == '\n' or lib[len(lib)-1] == ',':
                    lib = lib[:len(lib)-1]
                libraries.append(lib)
for lib in libraries:
    system('pip freeze | findstr '+lib)