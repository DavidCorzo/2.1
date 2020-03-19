import dependency_functions,time

if __name__ == "__main__":
    try:
        print("\n",dependency_functions.git_push(dependency_functions.get_message()))
        print("-"*20 + "Done" + "-"*20)
    except Exception as e:
        print(e)
        time.sleep(10)
