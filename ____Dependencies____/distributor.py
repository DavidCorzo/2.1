import os,shutil,time,yaml,sys


def check_dirs():
    with open("dependencies/dependencies.yaml") as file:
        F = yaml.full_load(file)
        file.close()
        return F 

        
        
def main():
    DirsForTex = None # Open dirs or excecutables destination
    with open("dirs_for_tex.yaml") as file:
        DirsForTex = yaml.full_load(file)
        file.close()

    Executables = None # Open dirs of excecutables source 
    with open("executables.yaml") as file:
        Executables = yaml.full_load(file)
        file.close()
    

    for dir_name in Executables.items():
        for inner_dir_name in DirsForTex.items():
            with open(DirsForTex[inner_dir_name[0]] + "/dependencies/dependencies.yaml", mode='r', encoding='UTF-8') as file: 
                T = yaml.full_load(file) 
                file.close()

                try:
                    if (T[dir_name[0]]):
                        try:
                            os.remove(inner_dir_name[1] + "/" + dir_name[1][1])
                        except:
                            print("|!| already deleted, moving on")
                        try:
                            shutil.copy(Executables[dir_name[0]][0],inner_dir_name[1])
                        except:
                            print("|!| Error copying from source to dest.")

                except KeyError as e:
                    print(f"No key {e}, dgcm")
                    continue 

    

if __name__ == "__main__":
    try:
        main()
        print("|!| Succesful in creating the excecutables in working directory. ")
        time.sleep(2) 
    except Exception as e:
        print("|!| DGCM:" + e)
        time.sleep(10)

